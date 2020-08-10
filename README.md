# Match stats bot

Match stats bot is a Steam bot for fetching Dota 2 data.

## Description
 *Consists of*:
    - Flask Web Server (api.py)
    - Dota Worker (bot.py)

## Installation

1) Clone repository
2) Create .env file
3) Consult for secrets
    - Steam Secrets
    - Backend Secrets
4) Run docker-compose

```bash
docker-compose up --build
```

## Usage

```bash
GET /tournaments/<int:league_id>/matches
```
Returns last 25 matches for the tournament.

<details>
<summary>Example Response</summary>

```json
{
    "request_id": 0,
    "results_remaining": 25,
    "series": [
        {
            "matches": [
                {
                    "dire_team_complete": 0,
                    "dire_team_id": 7912704,
                    "dire_team_logo": 1000305831702422575,
                    "dire_team_logo_url": "https://steamusercontent-a.akamaihd.net/ugc/1000305831702422575/B279DCF20A9DEAA49C1D5C1B358C971508DB2729/",
                    "dire_team_name": "Ранхигс Москва",
                    "dire_team_tag": "RANHMSK",
                    "game_mode": 2,
                    "leagueid": 11776,
                    "lobby_type": 1,
                    "match_flags": 0,
                    "match_id": 5396792947,
                    "match_outcome": 3,
                    "negative_votes": 0,
                    "players": [
                        {
                            "account_id": 143817835,
                            "active_plus_subscription": true,
                            "hero_id": 64,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "4to takoe dobrot",
                            "player_slot": 0
                        },
                        {
                            "account_id": 334728173,
                            "active_plus_subscription": false,
                            "hero_id": 46,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "kapsnik",
                            "player_slot": 1
                        },
                        {
                            "account_id": 90891743,
                            "active_plus_subscription": false,
                            "hero_id": 1,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Mu[RR]ZiK",
                            "player_slot": 2
                        },
                        {
                            "account_id": 912054671,
                            "active_plus_subscription": false,
                            "hero_id": 79,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Sherli",
                            "player_slot": 3
                        },
                        {
                            "account_id": 400009989,
                            "active_plus_subscription": true,
                            "hero_id": 129,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "!КОТИК В АКВАЛАНГЕ!",
                            "player_slot": 4
                        },
                        {
                            "account_id": 241483346,
                            "active_plus_subscription": false,
                            "hero_id": 93,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Juseark",
                            "player_slot": 128
                        },
                        {
                            "account_id": 123086641,
                            "active_plus_subscription": true,
                            "hero_id": 37,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "TEMPEST DOUBLE",
                            "player_slot": 129
                        },
                        {
                            "account_id": 48650948,
                            "active_plus_subscription": false,
                            "hero_id": 2,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Jugger",
                            "player_slot": 130
                        },
                        {
                            "account_id": 449071511,
                            "active_plus_subscription": false,
                            "hero_id": 101,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "jaguarflow_",
                            "player_slot": 131
                        },
                        {
                            "account_id": 301736317,
                            "active_plus_subscription": true,
                            "hero_id": 74,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Hamjak",
                            "player_slot": 132
                        }
                    ],
                    "positive_votes": 0,
                    "radiant_team_complete": 0,
                    "radiant_team_id": 7894396,
                    "radiant_team_logo": 1019446044006726350,
                    "radiant_team_logo_url": "https://steamusercontent-a.akamaihd.net/ugc/1019446044006726350/FE75930DF3CB44309C7A398DAF33F4DE2B85DE6B/",
                    "radiant_team_name": "opyat' na pari",
                    "radiant_team_tag": "ONP",
                    "series_id": 438628,
                    "series_type": 1,
                    "startTime": 1588612054
                },
                {
                    "dire_team_complete": 0,
                    "dire_team_id": 7894396,
                    "dire_team_logo": 1019446044006726350,
                    "dire_team_logo_url": "https://steamusercontent-a.akamaihd.net/ugc/1019446044006726350/FE75930DF3CB44309C7A398DAF33F4DE2B85DE6B/",
                    "dire_team_name": "opyat' na pari",
                    "dire_team_tag": "ONP",
                    "game_mode": 2,
                    "leagueid": 11776,
                    "lobby_type": 1,
                    "match_flags": 0,
                    "match_id": 5396960579,
                    "match_outcome": 2,
                    "negative_votes": 0,
                    "players": [
                        {
                            "account_id": 241483346,
                            "active_plus_subscription": false,
                            "hero_id": 42,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Juseark",
                            "player_slot": 0
                        },
                        {
                            "account_id": 123086641,
                            "active_plus_subscription": true,
                            "hero_id": 64,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "TEMPEST DOUBLE",
                            "player_slot": 1
                        },
                        {
                            "account_id": 48650948,
                            "active_plus_subscription": false,
                            "hero_id": 51,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Jugger",
                            "player_slot": 2
                        },
                        {
                            "account_id": 301736317,
                            "active_plus_subscription": true,
                            "hero_id": 36,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Hamjak",
                            "player_slot": 3
                        },
                        {
                            "account_id": 449071511,
                            "active_plus_subscription": false,
                            "hero_id": 126,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "jaguarflow_",
                            "player_slot": 4
                        },
                        {
                            "account_id": 143817835,
                            "active_plus_subscription": true,
                            "hero_id": 37,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "4to takoe dobrot",
                            "player_slot": 128
                        },
                        {
                            "account_id": 90891743,
                            "active_plus_subscription": false,
                            "hero_id": 4,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Mu[RR]ZiK",
                            "player_slot": 129
                        },
                        {
                            "account_id": 400009989,
                            "active_plus_subscription": true,
                            "hero_id": 96,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "!КОТИК В АКВАЛАНГЕ!",
                            "player_slot": 130
                        },
                        {
                            "account_id": 334728173,
                            "active_plus_subscription": false,
                            "hero_id": 52,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "kapsnik",
                            "player_slot": 131
                        },
                        {
                            "account_id": 912054671,
                            "active_plus_subscription": false,
                            "hero_id": 121,
                            "leaver_status": 0,
                            "mmr_type": 1,
                            "player_name": "Sherli",
                            "player_slot": 132
                        }
                    ],
                    "positive_votes": 0,
                    "series_id": 438628,
                    "series_type": 1,
                    "startTime": 1588618115
                }
            ],
            "series_id": 438628,
            "series_type": 1
        },
	...
	...
	...   
    ],
    "total_results": 50
}
```
</details>


-------------------

```bash
GET /tournaments/<int:league_id>/matches/<int:start_time>
```
Returns json with detailed stats of the match.

<details>
<summary>Example Response</summary>

```json
{
    "match": {
        "barracks_status": [
            60,
            60
        ],
        "broadcaster_channels": [
            {
                "broadcaster_infos": [
                    {
                        "account_id": 110797951,
                        "name": "Dandelion"
                    },
                    {
                        "account_id": 302693725,
                        "name": "Loba"
                    },
                    {
                        "account_id": 1022099190,
                        "name": "Not toxic; TryHard & All Muted"
                    }
                ],
                "country_code": "ru",
                "description": "Eee",
                "language_code": "russian"
            }
        ],
        "cluster": 134,
        "dire_team_complete": 0,
        "dire_team_id": 7912704,
        "dire_team_logo": 1000305831702422575,
        "dire_team_logo_url": "https://steamusercontent-a.akamaihd.net/ugc/1000305831702422575/B279DCF20A9DEAA49C1D5C1B358C971508DB2729/",
        "dire_team_name": "Ранхигс Москва",
        "dire_team_score": 49,
        "duration": 2851,
        "engine": 1,
        "first_blood_time": 170,
        "game_mode": 2,
        "human_players": 10,
        "leagueid": 11776,
        "lobby_type": 1,
        "match_flags": 0,
        "match_id": 5396792947,
        "match_outcome": 3,
        "negative_votes": 0,
        "picks_bans": [
            {
                "hero_id": 102,
                "is_pick": false,
                "team": 0
            },
            {
                "hero_id": 39,
                "is_pick": false,
                "team": 1
            },
            {
                "hero_id": 17,
                "is_pick": false,
                "team": 0
            },
            {
                "hero_id": 110,
                "is_pick": false,
                "team": 1
            },
            {
                "hero_id": 98,
                "is_pick": false,
                "team": 0
            },
            {
                "hero_id": 59,
                "is_pick": false,
                "team": 1
            },
            {
                "hero_id": 91,
                "is_pick": false,
                "team": 0
            },
            {
                "hero_id": 111,
                "is_pick": false,
                "team": 1
            },
            {
                "hero_id": 64,
                "is_pick": true,
                "team": 0
            },
            {
                "hero_id": 2,
                "is_pick": true,
                "team": 1
            },
            {
                "hero_id": 101,
                "is_pick": true,
                "team": 1
            },
            {
                "hero_id": 129,
                "is_pick": true,
                "team": 0
            },
            {
                "hero_id": 128,
                "is_pick": false,
                "team": 0
            },
            {
                "hero_id": 106,
                "is_pick": false,
                "team": 1
            },
            {
                "hero_id": 37,
                "is_pick": true,
                "team": 1
            },
            {
                "hero_id": 79,
                "is_pick": true,
                "team": 0
            },
            {
                "hero_id": 93,
                "is_pick": true,
                "team": 1
            },
            {
                "hero_id": 1,
                "is_pick": true,
                "team": 0
            },
            {
                "hero_id": 43,
                "is_pick": false,
                "team": 1
            },
            {
                "hero_id": 36,
                "is_pick": false,
                "team": 0
            },
            {
                "hero_id": 46,
                "is_pick": true,
                "team": 0
            },
            {
                "hero_id": 74,
                "is_pick": true,
                "team": 1
            }
        ],
        "players": [
            {
                "XP_per_min": 286,
                "account_id": 143817835,
                "active_plus_subscription": true,
                "assists": 14,
                "deaths": 14,
                "denies": 1,
                "gold_per_min": 214,
                "hero_id": 64,
                "item_0": 36,
                "item_1": 79,
                "item_2": 214,
                "item_3": 40,
                "item_4": 218,
                "item_5": 31,
                "item_6": 0,
                "item_7": 0,
                "item_8": 0,
                "kills": 1,
                "lane_selection_flags": 0,
                "last_hits": 66,
                "leaver_status": 0,
                "level": 16,
                "mmr_type": 1,
                "net_worth": 4808,
                "party_id": 0,
                "permanent_buffs": [
                    {
                        "permanent_buff": 6,
                        "stack_count": 1
                    }
                ],
                "player_name": "4to takoe dobrot",
                "player_slot": 0
            },
            {
                "XP_per_min": 827,
                "account_id": 334728173,
                "active_plus_subscription": false,
                "assists": 4,
                "deaths": 7,
                "denies": 20,
                "gold_per_min": 639,
                "hero_id": 46,
                "item_0": 63,
                "item_1": 1,
                "item_2": 116,
                "item_3": 139,
                "item_4": 141,
                "item_5": 168,
                "item_6": 38,
                "item_7": 0,
                "item_8": 0,
                "kills": 16,
                "lane_selection_flags": 0,
                "last_hits": 454,
                "leaver_status": 0,
                "level": 28,
                "mmr_type": 1,
                "net_worth": 23865,
                "party_id": 0,
                "player_name": "kapsnik",
                "player_slot": 1
            },
            {
                "XP_per_min": 699,
                "account_id": 90891743,
                "active_plus_subscription": false,
                "assists": 7,
                "deaths": 11,
                "denies": 5,
                "gold_per_min": 561,
                "hero_id": 1,
                "item_0": 208,
                "item_1": 147,
                "item_2": 145,
                "item_3": 36,
                "item_4": 75,
                "item_5": 63,
                "item_6": 0,
                "item_7": 0,
                "item_8": 0,
                "kills": 9,
                "lane_selection_flags": 0,
                "last_hits": 380,
                "leaver_status": 0,
                "level": 26,
                "mmr_type": 1,
                "net_worth": 19031,
                "party_id": 0,
                "player_name": "Mu[RR]ZiK",
                "player_slot": 2
            },
            {
                "XP_per_min": 337,
                "account_id": 912054671,
                "active_plus_subscription": false,
                "assists": 11,
                "deaths": 10,
                "denies": 3,
                "gold_per_min": 238,
                "hero_id": 79,
                "item_0": 254,
                "item_1": 102,
                "item_2": 180,
                "item_3": 0,
                "item_4": 57,
                "item_5": 0,
                "item_6": 290,
                "item_7": 0,
                "item_8": 0,
                "kills": 1,
                "lane_selection_flags": 0,
                "last_hits": 54,
                "leaver_status": 0,
                "level": 18,
                "mmr_type": 1,
                "net_worth": 8527,
                "party_id": 0,
                "permanent_buffs": [
                    {
                        "permanent_buff": 6,
                        "stack_count": 3
                    }
                ],
                "player_name": "Sherli",
                "player_slot": 3
            },
            {
                "XP_per_min": 492,
                "account_id": 400009989,
                "active_plus_subscription": true,
                "assists": 14,
                "deaths": 7,
                "denies": 20,
                "gold_per_min": 357,
                "hero_id": 129,
                "item_0": 36,
                "item_1": 116,
                "item_2": 90,
                "item_3": 1,
                "item_4": 63,
                "item_5": 178,
                "item_6": 0,
                "item_7": 0,
                "item_8": 0,
                "kills": 1,
                "lane_selection_flags": 0,
                "last_hits": 253,
                "leaver_status": 0,
                "level": 22,
                "mmr_type": 1,
                "net_worth": 12705,
                "party_id": 0,
                "player_name": "!КОТИК В АКВАЛАНГЕ!",
                "player_slot": 4
            },
            {
                "XP_per_min": 824,
                "account_id": 241483346,
                "active_plus_subscription": false,
                "assists": 15,
                "deaths": 3,
                "denies": 9,
                "gold_per_min": 591,
                "hero_id": 93,
                "item_0": 108,
                "item_1": 174,
                "item_2": 63,
                "item_3": 208,
                "item_4": 116,
                "item_5": 117,
                "item_6": 0,
                "item_7": 75,
                "item_8": 0,
                "kills": 13,
                "lane_selection_flags": 0,
                "last_hits": 350,
                "leaver_status": 0,
                "level": 29,
                "mmr_type": 1,
                "net_worth": 26490,
                "party_id": 0,
                "permanent_buffs": [
                    {
                        "permanent_buff": 6,
                        "stack_count": 1
                    },
                    {
                        "permanent_buff": 8,
                        "stack_count": 25
                    }
                ],
                "player_name": "Juseark",
                "player_slot": 128
            },
            {
                "XP_per_min": 496,
                "account_id": 123086641,
                "active_plus_subscription": true,
                "assists": 22,
                "deaths": 8,
                "denies": 6,
                "gold_per_min": 352,
                "hero_id": 37,
                "item_0": 108,
                "item_1": 36,
                "item_2": 254,
                "item_3": 40,
                "item_4": 244,
                "item_5": 29,
                "item_6": 0,
                "item_7": 0,
                "item_8": 0,
                "kills": 5,
                "lane_selection_flags": 0,
                "last_hits": 69,
                "leaver_status": 0,
                "level": 23,
                "mmr_type": 1,
                "net_worth": 12473,
                "party_id": 0,
                "permanent_buffs": [
                    {
                        "permanent_buff": 6,
                        "stack_count": 3
                    }
                ],
                "player_name": "TEMPEST DOUBLE",
                "player_slot": 129
            },
            {
                "XP_per_min": 632,
                "account_id": 48650948,
                "active_plus_subscription": false,
                "assists": 22,
                "deaths": 5,
                "denies": 34,
                "gold_per_min": 490,
                "hero_id": 2,
                "item_0": 112,
                "item_1": 90,
                "item_2": 162,
                "item_3": 50,
                "item_4": 1,
                "item_5": 127,
                "item_6": 0,
                "item_7": 0,
                "item_8": 0,
                "kills": 4,
                "lane_selection_flags": 0,
                "last_hits": 304,
                "leaver_status": 0,
                "level": 26,
                "mmr_type": 1,
                "net_worth": 20790,
                "party_id": 0,
                "player_name": "Jugger",
                "player_slot": 130
            },
            {
                "XP_per_min": 508,
                "account_id": 449071511,
                "active_plus_subscription": false,
                "assists": 24,
                "deaths": 9,
                "denies": 4,
                "gold_per_min": 288,
                "hero_id": 101,
                "item_0": 102,
                "item_1": 77,
                "item_2": 77,
                "item_3": 77,
                "item_4": 37,
                "item_5": 206,
                "item_6": 0,
                "item_7": 38,
                "item_8": 0,
                "kills": 8,
                "lane_selection_flags": 0,
                "last_hits": 46,
                "leaver_status": 0,
                "level": 23,
                "mmr_type": 1,
                "net_worth": 10169,
                "party_id": 0,
                "player_name": "jaguarflow_",
                "player_slot": 131
            },
            {
                "XP_per_min": 660,
                "account_id": 301736317,
                "active_plus_subscription": true,
                "assists": 20,
                "deaths": 3,
                "denies": 12,
                "gold_per_min": 577,
                "hero_id": 74,
                "item_0": 50,
                "item_1": 267,
                "item_2": 1,
                "item_3": 119,
                "item_4": 116,
                "item_5": 256,
                "item_6": 0,
                "item_7": 0,
                "item_8": 0,
                "kills": 18,
                "lane_selection_flags": 0,
                "last_hits": 344,
                "leaver_status": 0,
                "level": 27,
                "mmr_type": 1,
                "net_worth": 25600,
                "party_id": 0,
                "permanent_buffs": [
                    {
                        "permanent_buff": 2,
                        "stack_count": 0
                    }
                ],
                "player_name": "Hamjak",
                "player_slot": 132
            }
        ],
        "positive_votes": 0,
        "pre_game_duration": 90,
        "radiant_team_complete": 0,
        "radiant_team_id": 7894396,
        "radiant_team_logo": 1019446044006726350,
        "radiant_team_logo_url": "https://steamusercontent-a.akamaihd.net/ugc/1019446044006726350/FE75930DF3CB44309C7A398DAF33F4DE2B85DE6B/",
        "radiant_team_name": "opyat' na pari",
        "radiant_team_score": 28,
        "replay_salt": 2004736356,
        "replay_state": 0,
        "series_id": 438628,
        "series_type": 1,
        "startTime": 1588612054,
        "tower_status": [
            1824,
            1590
        ]
    },
    "result": 1,
    "vote": 0
}
```
</details>

-------------------

```bash
GET /profiles/<int:steam32_id>/stats
```

<details>
<summary>Example Response</summary>

```json
{
    "account_id": 71935067,
    "aegises_snatched": 1,
    "cheeses_eaten": 16,
    "couriers_killed": 58,
    "creeps_stacked": 2395,
    "farm_score": 0.23394371569156647,
    "fight_score": 0.3918910026550293,
    "first_blood_claimed": 42,
    "first_blood_given": 81,
    "match_count": 20,
    "mean_damage": 8424.650390625,
    "mean_gpm": 312.3500061035156,
    "mean_heals": 1188.25,
    "mean_lasthits": 102.0,
    "mean_networth": 9651.9501953125,
    "mean_xppm": 456.6499938964844,
    "push_score": 0.4136309325695038,
    "rampages": 2,
    "rapiers_purchased": 6,
    "support_score": 0.6341832280158997,
    "triple_kills": 78,
    "versatility_score": 0.8591762185096741
}
```
</details>

-------------------

```bash
GET /profiles/<int:steam32_id>/successful_heroes
```

<details>
<summary>Example Response</summary>

```json
[
    {
        "hero_id": 41,
        "longest_streak": 4,
        "win_percent": 0.7333333492279053
    },
    {
        "hero_id": 85,
        "longest_streak": 6,
        "win_percent": 0.7241379022598267
    },
    {
        "hero_id": 48,
        "longest_streak": 1,
        "win_percent": 0.7037037014961243
    }
]
```
</details>

-------------------

```bash
GET /profiles/<int:steam32_id>/card
```

<details>
<summary>Example Response</summary>

```json
{
    "account_id": 71935067,
    "background_def_index": 0,
    "badge_points": 6970,
    "is_plus_subscriber": false,
    "plus_original_start_date": 0,
    "previous_rank_tier": 0,
    "rank_tier": 63
}
```
</details>

!!! IMPORTANT TO SEND STEAM32_ID !!!
-----------
Also important to note that Response contains field rank_tier_mmr_type which should
be converted to "medal". Please consider converting by following logic.

```javascript
const RANK_TO_MEDAL = {
  80: 'Immortal',
  70: 'Divine',
  60: 'Ancient',
  50: 'Legend',
  40: 'Archon',
  30: 'Crusader',
  20: 'Guardian',
  10: 'Herald',
  0: 'Uncalibrated',
};
/**
 * @memberof module:rankTier
 */
const rankTierToMedalName = (_rankTier) => {
  const rankTier = _rankTier || 0;
  const rank = Math.floor(rankTier / 10) * 10;
  const tier = rankTier % 10;
  let medal = 'Unknown';
  if (rank >= 0 && rank < 90) {
    medal = `${RANK_TO_MEDAL[rank]}`;
    if (rank !== 80 && rank > 0 && tier > 0) {
      medal += ` ${tier}`;
    }
  }
  return medal;
};
```

-------------------

## API reference
<https://www.notion.so/Match-stats-bot-305a3750d69f4c1d9a5f9ab67a60e963>
