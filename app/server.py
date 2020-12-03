import gevent.monkey

gevent.monkey.patch_all()

from gevent.pywsgi import WSGIServer
import gevent
import os

from . import steam_bot
from .api import create_app
from .settings import Config

import sentry_sdk

sentry_sdk.init(os.getenv("SENTRY_DSN"), traces_sample_rate=0)

def init():
    app = create_app()
    http_server = WSGIServer(("0.0.0.0", int(Config.PORT)), app)

    server = gevent.spawn(http_server.serve_forever)
    worker = gevent.spawn(steam_bot.prompt_login)

    try:
        gevent.joinall([server, worker])
    except KeyboardInterrupt:
        steam_bot.close()
