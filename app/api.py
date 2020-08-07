"""
This module contains flask app and its routes.
"""

from getpass import getpass
from dacite import from_dict
from flask import Flask, request, abort, jsonify
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
    return jsonify({"Hello": worker.username})


@app.route("/tournament/matches", methods=["GET"])
def tournament_matches():
    """
    Gets 25 last Series from tournament.

    :param league_id: int
    :return: all Series of the tournament 
    :rtype: json
    TODO: Resolve how to get all Series.
    """
    body: Dict = request.json
    league_id: int = body["league_id"]

    try:
        matches = worker.get_tournament_matches(league_id)
    except Exception as e:
        jsonify({"Error": str(e)})
    else:
        return jsonify(matches)


@app.route("/matches", methods=["POST"])
def find_match_stats():
    """
    Finds stats for league match.
    
    :param start_time: int
    :param league_id: int
    :return: stats for the game 
    :rtype: json
    """
    # Get data from body
    body: Dict = request.json
    start_time: int = body["start_time"]
    league_id: int = body["league_id"]

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
        return jsonify({"Error": str(e)})
    else:
        return jsonify(detailed_match)
