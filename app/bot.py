"""
This module contains Steam bot.
"""

import gevent
from typing import Iterable, Any, Dict, Tuple
from queue import Queue

from steam.client import SteamClient
from steam.core.msg import MsgProto
from steam.enums.emsg import EMsg
from steam.utils.proto import proto_to_dict

from dota2.client import Dota2Client

from .settings import SteamConfig
from .exceptions import BotError

import logging
from rich.logging import RichHandler

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

LOG = logging.getLogger(__name__)

import time


class MatchStatsBot(object):
    """
    Represents a Bot.

    ...

    Attributes:
    ----------
    username: str
        Steam username
    password: str
        Steam password
    logged_on_once: bool
        From https://github.com/ValvePython/steam/blob/master/recipes/2.SimpleWebAPI/steam_worker.py
    steam: :class:`SteamClient`
        Steam client from steam lib
    dota: :class:`Dota2Client`
        Dota client from dota lib
    q: :class:`Queue`
        Queue to manage communication from callback to api

        .. note::
            Messages to the Queue are sent in the form of Tuple.

            :Example:

            >>> q.put("name_of_callback", callback_result)

    Methods:
    ----------
    __init__(self)
        Basically here the bot is launched and main events are registered.

    Main events:
        - client.on('logged_on')
            Steam Client is set up. Now we launch dota client.
        - dota.on('get_tournament_matches')
            Event wich is fired up by self.get_tournament_matches().
            Which itself is fired by api.


    """

    def __init__(self):
        self.username = SteamConfig.STEAM_LOGIN
        self.password = SteamConfig.STEAM_PASSWORD
        self.q = Queue()  # To contain results from callbacks

        self.logged_on_once = False

        self.steam = client = SteamClient()
        self.dota = dota = Dota2Client(client)

        client.set_credential_location("app/sentry")

        @client.on("error")
        def handle_error(result):
            LOG.info("Logon result: %s", repr(result))

        @client.on("connected")
        def handle_connected():
            LOG.info("Connected to %s", client.current_server_addr)

        @client.on("channel_secured")
        def send_login():
            if self.logged_on_once and self.steam.relogin_available:
                self.steam.relogin()

        @client.on("logged_on")
        def handle_after_logon():
            self.logged_on_once = True

            LOG.info("-" * 30)
            LOG.info("Logged on as: %s", client.user.name)
            LOG.info("Community profile: %s", client.steam_id.community_url)
            LOG.info("Last logon: %s", client.user.last_logon)
            LOG.info("Last logoff: %s", client.user.last_logoff)
            LOG.info("-" * 30)

            dota.launch()  # Launch dota

        @client.on("disconnected")
        def handle_disconnect():
            LOG.info("Disconnected.")

            if self.logged_on_once:
                LOG.info("Reconnecting...")
                client.reconnect(maxdelay=30)

        @client.on("reconnect")
        def handle_reconnect(delay):
            LOG.info("Reconnect in %ds...", delay)

        @dota.on("ready")
        def ready():
            LOG.info("Dota is ready")

        @dota.on("get_tournament_matches")
        def handle_get_tournament_matches(league_id) -> Tuple:
            """
            !!!DEPRECATED!!!
            Fires after api calls `worker.get_tournament_matches()`

            Puts result to the queue as a Tuple.
            raises BotError if couldn't get tournament matches.
            """
            LOG.info("Caught a get_tournament_matches event")
            try:
                job = dota.request_matches(
                    league_id=league_id, matches_requested=25
                )  # 25 is max
                tournament_matches: Iterable = dota.wait_msg(job, timeout=10)
            except Exception:
                LOG.exception()
                raise
            else:
                # check if result exists
                if tournament_matches:
                    LOG.info("Putting matches in queue")
                    # Put result with identificator to Queue
                    self.q.put(("tournament_matches", tournament_matches))
                else:
                    LOG.warning(
                        "Could not find matches in tournament: {}".format(league_id)
                    )

        @dota.on("get_detailed_match")
        def handle_get_detailed_match(match_id) -> Tuple:
            """
            !!!DEPRECATED!!!
            Fires after api calls `worker.get_detailed_match()`

            Puts result to the queue as a Tuple.
            raises BotError if couldn't get match.
            """
            LOG.info("Caught a get_detailed_match event")
            try:
                job = dota.request_match_details(match_id)
                match: Iterable = dota.wait_msg(job, timeout=10)
            except Exception:
                LOG.exception()
                raise
            # check if result exists
            else:
                if match:
                    LOG.info("Putting matches in queue")
                    # Put result with identificator to Queue
                    self.q.put(("detailed_match", match))
                else:
                    LOG.exception()
                    raise BotError(
                        "Could not find matches in tournament: {}".format(match_id)
                    )

        @dota.on("get_profile_card")
        def handle_get_profile_card(steam_id: int) -> Tuple:
            """
            !!!DEPRECATED!!!
            Fires after api calls `worker.get_profile_card()`

            Puts result to the queue as a Tuple.
            raises BotError if couldn't get profile.
            """
            LOG.info("Caught a get_profile_stats event")
            try:
                # Profile card for medal
                job = dota.request_profile_card(steam_id)
                profile_card: Iterable = dota.wait_msg(job, timeout=10)
            except Exception:
                LOG.exception()
                raise
            else:
                # check if result exists
                if profile_card:
                    LOG.info("Putting profile card in queue")
                    # Put result with identificator to Queue
                    self.q.put(("profile_card", profile_card))
                else:
                    LOG.exception()
                    raise BotError("Could not find profile: {}".format(steam_id))

        @dota.on("get_profile_stats")
        def handle_get_profile_stats(steam_id: int) -> Tuple:
            """
            !!!DEPRECATED!!!
            Fires after api calls `worker.get_profile_stats()`

            Puts result to the queue as a Tuple.
            raises BotError if couldn't get profile.
            """
            LOG.info("Caught a get_profile_stats event")
            try:
                # Profile stats for in game stats
                job = dota.request_player_stats(steam_id)
                profile_stats: Iterable = dota.wait_msg(job, timeout=10)
            except Exception:
                LOG.exception()
                raise
            else:
                # check if result exists
                if profile_stats:
                    LOG.info("Putting profile card in queue")
                    # Put result with identificator to Queue
                    self.q.put(("profile_stats", profile_stats))
                else:
                    LOG.exception()
                    raise BotError("Could not find profile: {}".format(steam_id))

        @dota.on("get_profile_general")
        def handle_get_profile_general(steam_id: int) -> Tuple:
            """
            !!!DEPRECATED!!!
            Fires after api calls `worker.get_profile_general()`

            Puts result to the queue as a Tuple.
            raises BotError if couldn't get profile.
            """
            LOG.info("Caught a get_profile_general event")
            try:
                # Profile stats for heroes
                job = dota.request_profile(steam_id)
                profile_general: Iterable = dota.wait_msg(job, timeout=10)
            except Exception:
                LOG.exception()
                raise
            else:
                # check if result exists
                if profile_general:
                    LOG.info("Putting profile card in queue")
                    # Put result with identificator to Queue
                    self.q.put(("profile_general", profile_general))
                else:
                    LOG.warning("Could not find profile: {}".format(steam_id))

    def prompt_login(self):
        """
        Logins to steam
        """
        self.steam.cli_login(self.username, self.password)

    def handle_task(self, task) -> Dict:
        """
        Basically converts task :class: Tuple to :class: Dict
        """
        item = task[1]
        result: Dict = proto_to_dict(item)
        self.q.task_done()
        LOG.info("Task is done: '{}'".format(task[0]))
        return result

    def get_result_from_queue(self, event) -> Dict:
        """
        !!!DEPRECATED!!!
        Get result from queue by event name
        :return: converted Proto to dict
        :rtype: Dict
        """
        task = self.q.get()
        LOG.info("New task {}".format(task[0]))
        if task[0] == event:  # filtering for desired event
            LOG.info("Working on {}".format(event))
            result = self.handle_task(task)
            return result

    def close(self):
        """
        Closes bot
        """
        if self.steam.logged_on:
            self.logged_on_once = False
            LOG.info("Logout")
            self.steam.logout()
        if self.steam.connected:
            self.steam.disconnect()

    def get_tournament_matches(self, league_id: int) -> Dict:
        """
        !!!DEPRECATED!!!
        Gets league matches.

        :param league_id: int
        :return: matches
        :rtype: Dict
        """
        # timeout variable can be omitted
        timeout = time.time() + 60 * 5  # [seconds]

        # Emiting event
        self.dota.emit("get_tournament_matches", league_id)
        while True:
            if time.time() > timeout:
                raise BotError(
                    "Timeout. Could not wait for results from Dota for tournament matches"
                )
            matches = self.get_result_from_queue("tournament_matches")
            return matches

    def get_detailed_match(self, match_id: int) -> Dict:
        """
        !!!DEPRECATED!!!
        Gets detailed match stats.

        :param match_id: int
        :return: detailed match
        :rtype: Dict
        """
        # timeout variable can be omitted
        timeout = time.time() + 60 * 5  # [seconds]
        # Emiting event
        self.dota.emit("get_detailed_match", match_id)
        while True:
            if time.time() > timeout:
                raise BotError(
                    "Timeout. Could not wait for results from Dota for detailed match"
                )
            match = self.get_result_from_queue("detailed_match")
            return match

    def get_profile_card(self, steam_id: int) -> Dict:
        """
        !!!DEPRECATED!!!
        Find profile card by steam id. Mainly for medal check.

        :param steam_id: int
        :return: profile card
        :rtype: Dict
        """
        # timeout variable can be omitted
        timeout = time.time() + 60 * 5  # [seconds]
        self.dota.emit("get_profile_card", steam_id)
        while True:
            if time.time() > timeout:
                raise BotError(
                    "Timeout. Could not wait for results from Dota for profile card"
                )
            profile_card = self.get_result_from_queue("profile_card")
            return profile_card

    def get_profile_stats(self, steam_id: int) -> Dict:
        """
        !!!DEPRECATED!!!
        Find profile card by steam id. Mainly for in game stats (lasthits, rampages).

        :param steam_id: int
        :return: profile card
        :rtype: Dict
        """
        # timeout variable can be omitted
        timeout = time.time() + 60 * 5  # [seconds]
        self.dota.emit("get_profile_stats", steam_id)
        while True:
            if time.time() > timeout:
                raise BotError(
                    "Timeout. Could not wait for results from Dota for profile stats"
                )
            profile_stats = self.get_result_from_queue("profile_stats")
            return profile_stats

    def get_profile_general(self, steam_id: int) -> Dict:
        """
        !!!DEPRECATED!!!
        Find general profile info by steam id. Mainly for best heroes info.

        :param steam_id: int
        :return: general profile
        :rtype: Dict
        """
        # timeout variable can be omitted
        timeout = time.time() + 60 * 5  # [seconds]
        self.dota.emit("get_profile_general", steam_id)
        while True:
            if time.time() > timeout:
                raise BotError(
                    "Timeout. Could not wait for results from Dota for profile general"
                )
            profile_general = self.get_result_from_queue("profile_general")
            return profile_general
