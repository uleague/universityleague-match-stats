from unittest import mock
from . import TestResponses
from app.api import create_app, worker


def new_loaddata(cls, *args, **kwargs):
    # Your custom testing override
    return 1


class TestRoutes:
    def test_index_success(self, client):
        resp = client.get("/")
        resp_json = resp.get_json()

        assert resp.status_code == 200
        assert resp.content_type == "application/json"
        assert isinstance(resp_json, dict)
        assert {"Hello": "ul_test1"} == resp_json

    def test_tournament_matches_success(self, client):
        with mock.patch.object(
            worker.dota,
            "request_matches",
            return_value=TestResponses.tournament_matches_response,
        ) as m:
            client.get("/tournaments/{}/matches".format(TestResponses.league_id))
            m.assert_called_once_with(
                league_id=TestResponses.league_id, matches_requested=25
            )

    @mock.patch.object(
        worker.dota,
        "request_matches",
        return_value=TestResponses.tournament_matches_response,
    )
    @mock.patch.object(
        worker.dota,
        "request_match_details",
        return_value=TestResponses.detailed_match_response,
    )
    def test_find_match_stats_success(
        self, mock_detailed_match, mock_t_matches, client
    ):
        client.get(
            "/tournaments/{}/matches/{}".format(
                TestResponses.league_id, TestResponses.start_time
            )
        )

        mock_t_matches.assert_called_once_with(
            league_id=TestResponses.league_id, matches_requested=25
        )
        mock_detailed_match.assert_called_once_with(
            TestResponses.detailed_match_response["match"]["match_id"]
        )

    @mock.patch.object(
        worker.dota,
        "request_player_stats",
        return_value=TestResponses.profile_stats_response,
    )
    def test_find_profile_stats_success(self, mock_profile_stats, client):
        client.get("/profiles/{}/stats".format(TestResponses.steam32_id))
        mock_profile_stats.assert_called_once_with(TestResponses.steam32_id)

    @mock.patch.object(
        worker.dota,
        "request_profile",
        return_value=TestResponses.successful_heroes_response,
    )
    def test_find_profile_successful_heroes_success(self, mock_profile_general, client):
        client.get("/profiles/{}/successful_heroes".format(TestResponses.steam32_id))
        mock_profile_general.assert_called_once_with(TestResponses.steam32_id)

    @mock.patch.object(
        worker.dota,
        "request_profile_card",
        return_value=TestResponses.successful_heroes_response,
    )
    def test_find_profile_card_sucess(self, mock_profile_stats, client):
        client.get("/profiles/{}/card".format(TestResponses.steam32_id))
        mock_profile_stats.assert_called_once_with(TestResponses.steam32_id)
