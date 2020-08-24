import json

with open("tests/data/tournament_matches.json", "r") as f:
    test_tournament_matches_response = json.load(f)

with open("tests/data/detailed_match.json", "r") as f:
    test_detailed_match_response = json.load(f)

with open("tests/data/profile_stats.json", "r") as f:
    test_profile_stats_response = json.load(f)

with open("tests/data/successful_heroes.json", "r") as f:
    test_successful_heroes_response = json.load(f)

with open("tests/data/profile_card.json", "r") as f:
    test_profile_card_response = json.load(f)


class TestResponses:
    steam32_id = 71935067
    league_id = 11776
    start_time = 1588612054
    tournament_matches_response = test_tournament_matches_response
    detailed_match_response = test_detailed_match_response
    profile_stats_response = test_profile_stats_response
    successful_heroes_response = test_successful_heroes_response
    profile_card_response = test_profile_card_response
