"""
This module contains flask app and its routes.
"""

from getpass import getpass
from dacite import from_dict
from flask import Flask, request, abort, jsonify, make_response
from typing import Dict

from bot import MatchStatsBot
from helpers import Tournament

import logging
from rich.logging import RichHandler

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

LOG = logging.getLogger(__name__)

app = Flask("api")
worker = MatchStatsBot()


@app.route("/", methods=["GET"])
def say_hello():
    return make_response(jsonify({"Hello": worker.username}, 200))


@app.route("/tournaments/<int:league_id>/matches", methods=["GET"])
def tournament_matches(league_id: int):
    """
    Gets 25 last Series from tournament.

    :param league_id: int
    :return: all Series of the tournament 
    :rtype: json
    TODO: Resolve how to get all Series.
    """
    try:
        matches = worker.get_tournament_matches(league_id)
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        return make_response(jsonify(matches), 200)


@app.route("/tournaments/<int:league_id>/matches/<int:start_time>", methods=["GET"])
def find_match_stats(league_id: int, start_time: int):
    """
    Finds stats for league match.
    
    :param start_time: int
    :param league_id: int
    :return: stats for the game 
    :rtype: json
    """
    try:
        # Try to find match in Dota with our worker
        tournament_matches = worker.get_tournament_matches(league_id)
        t = from_dict(data_class=Tournament, data=tournament_matches)
        # Find the desired match by start_time
        match = t.get_match(start_time)
        match_id = match["match_id"]
        # Find detailed match info by match id
        detailed_match = worker.get_detailed_match(match_id)
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        return make_response(jsonify(detailed_match), 200)


@app.route("/profiles/<int:steam32_id>/stats", methods=["GET"])
def find_profile_stas(steam32_id):
    """
    Finds stats for profile.
    player_stats
    
    :param steam32_id: int
    :return: profile stats
    :rtype: json
    """
    try:
        # Try to fetch profile in Dota with our worker
        profile_stats = worker.get_profile_stats(steam32_id)
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        return make_response(jsonify(profile_stats), 200)


@app.route("/profiles/<int:steam32_id>/successful_heroes", methods=["GET"])
def find_profile_successful_heroes(steam32_id):
    """
    Successful heroes.
    
    :param steam32_id: int
    :return: top 3 successful heroes
    :rtype: json
    """
    try:
        # Try to fetch profile in Dota with our worker
        profile_general = worker.get_profile_general(steam32_id)
        """ 
        Response contains a lot of things. 
        Reference: https://github.com/ValvePython/dota2/blob/98763e7b748a588462387469db65ea1a3e19a3af/protobufs/dota_gcmessages_client.proto#L2519-L2539 
        For some reason profile_general — object not a dict. Thus, needs to be handled manually.
        As we need for now only heroes, returning heroes.
        """
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        return make_response(jsonify(profile_general["successful_heroes"]), 200)


@app.route("/profiles/<int:steam32_id>/card", methods=["GET"])
def find_profile_card(steam32_id):
    """
    Profile card.
    
    :param steam32_id: int
    :return: profile card
    :rtype: json
    """
    try:
        # Try to fetch profile in Dota with our worker
        profile_card = worker.get_profile_card(steam32_id)
    except Exception as e:
        return make_response(jsonify({"Error": str(e)}), 500)
    else:
        return make_response(jsonify(profile_card), 200)
