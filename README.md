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
POST /match
```
```bash
Payload {
    "start_time": int,
    "league_id"
}
```
Returns json with stats of the match.


## API reference
<https://www.notion.so/Match-stats-bot-305a3750d69f4c1d9a5f9ab67a60e963>