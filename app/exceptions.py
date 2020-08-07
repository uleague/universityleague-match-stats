"""
This module contains custom exceptions.
"""


class BotError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "Bot caught an error --> {}".format(self.message)


class TournamentError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "Tournament caught an error --> {}".format(self.message)
