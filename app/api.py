from getpass import getpass
from flask import Flask, request, abort, jsonify

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
    """
    return
