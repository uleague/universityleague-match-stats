"""
This module contains flask app and its routes.
"""

from getpass import getpass
from flask import Flask, request, abort, jsonify
from typing import Dict

from bot import MatchStatsBot

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

    # Try to find match in Dota with our worker
    try:
        worker.get_tournament_matches()
    except Exception:
        raise
    return
