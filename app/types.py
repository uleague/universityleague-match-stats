"""
This module is mainly for dataclasses.
"""

from dataclasses import dataclass
from typing import List, Sequence, TypedDict, Dict, Union

from .exceptions import TournamentError


@dataclass
class MatchPlayer(TypedDict):
    account_id: int
    active_plus_subscription: bool
    hero_id: int
    leaver_status: int
    mmr_type: int
    player_name: str
    player_slot: int


@dataclass
class Match(TypedDict):
    dire_team_complete: int
    dire_team_id: int
    dire_team_logo: int
    dire_team_logo_url: str
    dire_team_name: str
    dire_team_tag: str
    game_mode: int
    leagueid: int
    lobby_type: int
    match_flags: int
    match_id: int
    match_outcome: int
    negative_votes: int
    players: List[Dict["str", Union[MatchPlayer, str, int, List]]]
    positive_votes: int
    radiant_team_complete: int
    radiant_team_id: int
    radiant_team_logo: int
    radiant_team_logo_url: str
    radiant_team_name: str
    radiant_team_tag: str
    series_id: int
    series_type: int
    startTime: int


@dataclass
class Series(TypedDict):
    series_id: int
    matches: List[Dict["str", Union[Match, int, List]]]
    series_type: int


@dataclass
class Tournament:
    request_id: int
    results_remaining: int
    series: List[Dict["str", Union[Series, int, List]]]
    total_results: int

    def get_match(self, start_time: int) -> Match:
        """
        Gets match by start time.

        :param startTime: int
        :return :class: Match
        """
        for serie in self.series:
            for match in serie["matches"]:
                if match["startTime"] == start_time:
                    return match
        return None
