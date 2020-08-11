from gevent.pywsgi import WSGIServer

from . import test_league_id, test_steam32_id, test_start_time

import pytest


def test_send_index(server):
    resp = server.get("/")
    resp_json = resp.json

    assert resp.status_int == 200
    assert resp.content_type == "application/json"
    assert isinstance(resp_json, dict)
    assert "Hello" in resp_json


def test_tournament_matches(server):
    # TODO: Create response types for checking
    # WIP not working yet
    resp = server.get("/tournaments/{}/matches".format(test_league_id))
    resp_json = resp.json

    assert resp.status_int == 200
    assert resp.content_type == "application/json"
    assert isinstance(resp_json, dict)
    assert "results_remaining" in resp_json
