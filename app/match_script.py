"""
This script gets dota match stats by its start time.
Input - start time (unix).
Algorithm:
    1) Recieve start time 
    2) API pull dota league matches
    3) Map by start time
    4) API call by match id
    5) Insert into db and make api call to backend
One difficulty is to deal with protobuf messages. (Managed in parsing functions)
"""

import argparse
import sys
from steam import SteamClient
from steam.enums import EResult
from dota2 import Dota2Client
from dota2.enums import ESOType, EGCBaseMsg, EDOTAGCMsg, DOTA_GameMode, EServerRegion
from dota2.enums import DOTAJoinLobbyResult, DOTA_GC_TEAM, DOTABotDifficulty
import dota2.util

import requests
import logging

global start_time
global tournament_id_db
global match_id_db

global accountName
global password
global mongo_url

global db_name

global mongo
global matches

global url_prod

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s %(name)s: %(message)s", level=logging.DEBUG
)
LOG = logging.getLogger()


client = SteamClient()
client.set_credential_location(".")
dota = Dota2Client(client)


"""
listeners
"""


@client.on("error")
def handle_error(result):
    LOG.info("Logon result: %s", repr(result))


@client.on("channel_secured")
def send_login():
    if client.relogin_available:
        client.relogin()


@client.on("connected")
def handle_connected():
    LOG.info("Connected to %s", client.current_server_addr)


@client.on("reconnect")
def handle_reconnect(delay):
    LOG.info("Reconnect in %ds...", delay)


# @client.on("disconnected")
# def handle_disconnect():
#     LOG.info("Disconnected.")

#     if client.relogin_available:
#         LOG.info("Reconnecting...")
#         client.reconnect(maxdelay=30)


@client.on("logged_on")
def handle_after_logon():
    LOG.info("-" * 30)
    LOG.info("Logged on as: %s", client.user.name)
    LOG.info("Community profile: %s", client.steam_id.community_url)
    LOG.info("Last logon: %s", client.user.last_logon)
    LOG.info("Last logoff: %s", client.user.last_logoff)
    LOG.info("-" * 30)
    LOG.info("Press ^C to exit")
    dota.launch()


"""
this is the main function, parsing league matches
"""


@dota.on("ready")
def do_dota_stuff():
    job = dota.request_matches(league_id=11776, matches_requested=50)
    resp = dota.wait_event(job, timeout=5)
    if resp:
        LOG.info("Found league matches!")
        series = resp
        res = mapping(start_time=start_time, series=series)
        # now we have our mapped by start time match_id. Time to find the match details
        match_id = res.match_id
        LOG.info("Match id: %s" % match_id)
        job_match = dota.request_match_details(match_id)
        job_resp = dota.wait_event(job_match, timeout=5)
        for match in job_resp:
            if match:
                LOG.info("Inserting into db!")
                doc = convert_stats_dict(match)
                LOG.info(doc)
                api_call(doc, tournament_id_db, match_id=match_id_db)

        # job_resp = get_foo_match()
        # for match in job_resp:
        #    if match:
        #        LOG.info("Inserting into db!")
        #        doc = convert_stats_dict(match)
        #        LOG.info(doc)
        #        insert_statistics(start_time=start_time, doc=doc)
        #        api_call(doc, tournament_id_db, match_id=match_id_db)
    pass


"""
static
"""


def bot_forever():
    try:
        result = client.cli_login(
            username=LOGON_DETAILS["username"], password=LOGON_DETAILS["password"]
        )

        if result != EResult.OK:
            LOG.info("Failed to login: %s" % repr(result))
            raise SystemExit

        client.run_forever()
    except KeyboardInterrupt:
        if client.connected:
            LOG.info("Logout")
            client.logout()


def mapping(start_time, series):
    LOG.info("Mapping for %s" % start_time)
    for match in series:
        for a in match.series:
            for field in a.matches:
                LOG.info(field.startTime)
                if field.startTime == int(start_time):
                    return field
    LOG.error("could not find a match with this start time")
    client.logout()


def get_foo_match():
    """
    This is a test function. To see how 5vs5 will look like.
    """
    job = dota.request_match_details(5319938577)
    job_resp = dota.wait_event(job, timeout=5)
    return job_resp


def api_call(doc, tournament_id, match_id):

    # base_url = 'http://localhost:5000'
    # url_prod = 'https://api.universityleague.ru'
    # url_prod = base_url
    route = f"api/v1/bracket/{tournament_id}/matches/{match_id}/record"

    players = doc["players"]
    match_outcome = doc["match_outcome"]
    radiant_team_score = doc["radiant_team_score"]
    dire_team_score = doc["dire_team_score"]
    duration = doc["duration"]
    match_id = doc["match_id"]
    try:
        client.logout()
        requests.put(
            f"{url_prod}/{route}",
            json={
                "players": players,
                "match_outcome": match_outcome,
                "radiant_team_score": radiant_team_score,
                "dire_team_score": dire_team_score,
                "duration": duration,
                "match_id": match_id,
                "token": "CiNaegh7kush7shei4Ee",
            },
        )
    except requests.exceptions.HTTPError as errh:
        return "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "An Unknown Error occurred" + repr(err)
    pass


def convert_stats_dict(resp_proto):
    LOG.info("Converting protobuf to dict with only neccessary data")

    def convert_players_stat(proto):
        players = resp_proto.match.players
        res_players = []
        for player in players:
            res_players.append(
                {
                    "account_id": player.account_id,
                    "hero_id": player.hero_id,
                    "kills": player.kills,
                    "deaths": player.deaths,
                    "assists": player.assists,
                    "gold": player.gold,
                    "last_hits": player.last_hits,
                    "denies": player.denies,
                    "gold_per_min": player.gold_per_min,
                    "XP_per_min": player.XP_per_min,
                    "hero_damage": player.hero_damage,
                    "tower_damage": player.tower_damage,
                    "level": player.level,
                    "player_name": player.player_name,
                    "net_worth": player.net_worth,
                    "item_0": player.item_0,
                    "item_1": player.item_1,
                    "item_2": player.item_2,
                    "item_3": player.item_3,
                    "item_4": player.item_4,
                    "item_5": player.item_5,
                    "item_6": player.item_6,
                    "item_7": player.item_7,
                    "item_8": player.item_8,
                    "seconds_dead": player.seconds_dead,
                    "gold_lost_to_death": player.gold_lost_to_death,
                }
            )
        return res_players

    res = {
        "duration": resp_proto.match.duration,
        "startTime": resp_proto.match.startTime,
        "players": convert_players_stat(resp_proto),
        "match_id": resp_proto.match.match_id,
        "leagueid": resp_proto.match.leagueid,
        "game_mode": resp_proto.match.game_mode,
        "radiant_team_score": resp_proto.match.radiant_team_score,
        "dire_team_score": resp_proto.match.dire_team_score,
        "match_outcome": resp_proto.match.match_outcome,
    }
    return res


if __name__ == "__main__":
    LOG.info(sys.argv)

    start_time = sys.argv[1]
    tournament_id_db = sys.argv[2]
    match_id_db = sys.argv[3]

    accountName = sys.argv[4]
    password = sys.argv[5]
    url_prod = sys.argv[6]

    LOG.info(start_time)

    LOGON_DETAILS = {
        "username": accountName,
        "password": password,
    }

    bot_forever()
