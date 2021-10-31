"""
This module contains flask app and its routes.
"""

from dacite import from_dict
from flask import Flask, jsonify, make_response, Blueprint
from typing import Iterable
from steam.utils.proto import proto_to_dict
from steam.steamid import SteamID

from . import steam_bot
from .types import Tournament

import logging
from rich.logging import RichHandler

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

LOG = logging.getLogger(__name__)

bp = Blueprint("app", __name__)
worker = steam_bot


@bp.route("/", methods=["GET"])
def say_hello():
    if worker.username:
        return make_response(jsonify({"Hello": worker.username}), 200)
    else:
        return make_response(
            jsonify({"Error": "Could not get Bot username. Check if it is online"}), 500
        )


@bp.route("/tournaments/<int:league_id>/matches", methods=["GET"])
def tournament_matches(league_id: int):
    """
    Gets 25 last Series from tournament.

    :param league_id: int
    :return: all Series of the tournament
    :rtype: json
    """
    try:
        LOG.info(
            "Recieved tournament_matches request for {} tournament".format(league_id)
        )
        job = worker.dota.request_matches(
            league_id=league_id, matches_requested=25
        )  # 25 is max
        tournament_matches: Iterable = proto_to_dict(
            worker.dota.wait_msg(job, timeout=10)
        )
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        if tournament_matches:
            LOG.info("Found tournament matches. Responding")
            return make_response(jsonify(tournament_matches), 200)
        else:
            LOG.warning("Couldn't find tournament matches")
            return make_response(jsonify({"Error": tournament_matches}, 404))

@bp.route("/matches/<int:match_id>", methods=["GET"])
def get_match(match_id: int):
    """
    Get minimal info for match.

    :param match_id: int
    :return: all data for the public match
    :rtype: json
    """
    try:
        LOG.info(
            "Recieved get_match request for {}".format(match_id)
        )
        job = worker.dota.request_matches_minimal([match_id])
        matches: Iterable = proto_to_dict(
            worker.dota.wait_msg(job, timeout=10)
        )
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        if matches:
            LOG.info("Found match. Responding")
            return make_response(jsonify(matches["matches"][0]), 200)
        else:
            LOG.warning("Couldn't find match")
            return make_response(jsonify({"Error": match_id}, 404))


@bp.route("/tournaments/<int:league_id>/matches/<int:start_time>", methods=["GET"])
def find_match_stats(league_id: int, start_time: int):
    """
    Finds stats for league match.

    :param start_time: int
    :param league_id: int
    :return: stats for the game
    :rtype: json
    """
    try:
        LOG.info(
            "Recieved match by starttime request for tournament {}".format(league_id)
        )
        # Try to find match in Dota with our worker
        job = worker.dota.request_matches(
            league_id=league_id, matches_requested=25
        )  # 25 is max
        tournament_matches: Iterable = proto_to_dict(
            worker.dota.wait_msg(job, timeout=10)
        )
        t = from_dict(data_class=Tournament, data=tournament_matches)
        # Find the desired match by start_time
        LOG.info(
            "Looking for match started {} in tournament_matches {}".format(
                start_time, league_id
            )
        )
        match = t.get_match(start_time)
        match_id = match["match_id"]
        # Find detailed match info by match id
        job2 = worker.dota.request_match_details(match_id)
        detailed_match: Iterable = proto_to_dict(worker.dota.wait_msg(job2, timeout=10))
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        if detailed_match:
            LOG.info("Found tournament match. Responding")
            return make_response(jsonify(detailed_match), 200)
        else:
            LOG.warning("Couldn't find match by starttime")
            return make_response(jsonify({"Error": detailed_match}, 404))


@bp.route("/profiles/<int:steam64_id>/stats", methods=["GET"])
def find_profile_stas(steam64_id):
    """
    Finds stats for profile.
    player_stats

    :param steam64_id: int
    :return: profile stats
    :rtype: json
    """
    try:
        # Try to fetch profile in Dota with our worker
        LOG.info("Recieved stats request for {} profile".format(steam64_id))
        steam32_id = SteamID(steam64_id).as_32
        job = worker.dota.request_player_stats(steam32_id)
        profile_stats: Iterable = proto_to_dict(worker.dota.wait_msg(job, timeout=10))
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        if profile_stats:
            LOG.info("Found profile stats. Responding")
            return make_response(jsonify(profile_stats), 200)
        else:
            LOG.warning("Couldn't find profile stats")
            return make_response(jsonify({"Error": profile_stats}, 404))

@bp.route("/profiles/<int:steam64_id>/recent_matches", methods=["GET"])
def find_profile_info(steam64_id):
    """
    Finds stats for profile.
    player_stats

    :param steam64_id: int
    :return: profile stats
    :rtype: json
    """
    try:
        # Try to fetch profile in Dota with our worker
        LOG.info("Recieved info request for {} profile".format(steam64_id))
        steam32_id = SteamID(steam64_id).as_32
        job = worker.dota.request_profile(steam32_id)
        profile: Iterable = proto_to_dict(worker.dota.wait_msg(job, timeout=10))
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        if profile:
            LOG.info("Found profile stats. Responding")
            return make_response(jsonify(profile["recent_matches"]), 200)
        else:
            LOG.warning("Couldn't find profile stats")
            return make_response(jsonify({"Error": steam64_id}, 404))


@bp.route("/profiles/<int:steam32_id>/successful_heroes", methods=["GET"])
def find_profile_successful_heroes(steam32_id):
    """
    Successful heroes.

    :param steam32_id: int
    :return: top 3 successful heroes
    :rtype: json
    """
    try:
        LOG.info("Recieved successful heroes request for {} profile".format(steam32_id))
        # Try to fetch profile in Dota with our worker
        job = worker.dota.request_profile(steam32_id)
        profile_general: Iterable = proto_to_dict(worker.dota.wait_msg(job, timeout=10))
        """
        Response contains a lot of things.
        Reference: https://github.com/ValvePython/dota2/blob/98763e7b748a588462387469db65ea1a3e19a3af/protobufs/dota_gcmessages_client.proto#L2519-L2539
        For some reason profile_general — object not a dict. Thus, needs to be handled manually.
        As we need for now only heroes, returning heroes.
        """
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        if profile_general and "successful_heroes" in profile_general:
            LOG.info("Found profile successful_heroes. Responding")
            return make_response(jsonify(profile_general["successful_heroes"]), 200)
        elif profile_general and "featured_heroes" in profile_general:
            LOG.info("Found profile featured_heroes. Responding")
            return make_response(jsonify(profile_general["featured_heroes"]), 200)
        else:
            LOG.warning(
                "Couldn't find profile neither successful heroes nor featured heroes"
            )
            return make_response(jsonify([]), 404)


@bp.route("/profiles/<int:steam64_id>/card", methods=["GET"])
def find_profile_card(steam64_id):
    """
    Profile card.

    :param steam64_id: int
    :return: profile card
    :rtype: json
    """
    try:
        LOG.info("Recieved card request for {} profile".format(steam64_id))
        # Try to fetch profile in Dota with our worker
        steam32_id = SteamID(steam64_id).as_32
        job = worker.dota.request_profile_card(steam32_id)
        profile_card: Iterable = proto_to_dict(worker.dota.wait_msg(job, timeout=10))
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        if profile_card:
            LOG.info("Found profile card. Responding")
            return make_response(jsonify(profile_card), 200)
        else:
            LOG.warning("Couldn't find profile card")
            return make_response(jsonify({"Error": profile_card}, 404))


def create_app():
    app = Flask("api")
    app.register_blueprint(bp)
    return app
