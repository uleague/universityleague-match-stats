"""
This module contains Steam bot.
"""

import gevent
from typing import Iterable

from steam.client import SteamClient
from steam.core.msg import MsgProto
from steam.enums.emsg import EMsg
from steam.utils.proto import proto_to_dict

from dota2.client import Dota2Client

from settings import SteamConfig

import logging
from rich.logging import RichHandler

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

LOG = logging.getLogger(__name__)


class MatchStatsBot(object):
    """
    Represents a Bot.

    ...

    Attributes:
    ----------
    username: str
        Steam username
    password: str
        Steam password
    logged_on_once: bool
        From https://github.com/ValvePython/steam/blob/master/recipes/2.SimpleWebAPI/steam_worker.py
    steam: SteamClient
        Steam client from steam lib
    dota: Dota2Client
        Dota client from dota lib
    
    Methods:
    ----------


    """

    def __init__(self):
        self.username = SteamConfig.STEAM_LOGIN
        self.password = SteamConfig.STEAM_PASSWORD

        self.logged_on_once = False

        self.steam = client = SteamClient()
        self.dota = dota = Dota2Client(client)

        client.set_credential_location("./sentry")

        @client.on("error")
        def handle_error(result):
            LOG.info("Logon result: %s", repr(result))

        @client.on("connected")
        def handle_connected():
            LOG.info("Connected to %s", client.current_server_addr)

        @client.on("channel_secured")
        def send_login():
            if self.logged_on_once and self.steam.relogin_available:
                self.steam.relogin()

        @client.on("logged_on")
        def handle_after_logon():
            self.logged_on_once = True

            LOG.info("-" * 30)
            LOG.info("Logged on as: %s", client.user.name)
            LOG.info("Community profile: %s", client.steam_id.community_url)
            LOG.info("Last logon: %s", client.user.last_logon)
            LOG.info("Last logoff: %s", client.user.last_logoff)
            LOG.info("-" * 30)
            # Launch dota when logged in to Steam
            dota.launch()

        @client.on("disconnected")
        def handle_disconnect():
            LOG.info("Disconnected.")

            if self.logged_on_once:
                LOG.info("Reconnecting...")
                client.reconnect(maxdelay=30)

        @client.on("reconnect")
        def handle_reconnect(delay):
            LOG.info("Reconnect in %ds...", delay)

    def prompt_login(self):
        """
        Logins to steam
        """
        self.steam.cli_login(self.username, self.password)

    def close(self):
        """
        Closes bot
        """
        if self.steam.logged_on:
            self.logged_on_once = False
            LOG.info("Logout")
            self.steam.logout()
        if self.steam.connected:
            self.steam.disconnect()

    def get_tournament_matches(self, league_id: int = 12245) -> MsgProto:
        """
        Gets league matches.

        :param league_id: int
        :return: matches 
        :rtype: MsgProto

        TODO: Seems that proto has changed. Investigating...
        https://github.com/SteamDatabase/Protobufs/tree/master/dota2
        """
        job = self.dota.request_matches(league_id=league_id, matches_requested=50)
        tournament_matches: Iterable = self.dota.wait_msg(job, timeout=10)
        LOG.info(tournament_matches)
        return tournament_matches

    def get_match_by_start_time(self, start_time: int) -> MsgProto:
        """
        Find match by start_time in get_tournament_matches

        :param start_time: int
        """
        return
