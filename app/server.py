import gevent.monkey

gevent.monkey.patch_all()

from gevent.pywsgi import WSGIServer
import gevent

from . import steam_bot
from .api import create_app
from .settings import Config


def init():
    app = create_app()
    http_server = WSGIServer(("0.0.0.0", int(Config.PORT)), app)

    server = gevent.spawn(http_server.serve_forever)
    worker = gevent.spawn(steam_bot.prompt_login)

    try:
        gevent.joinall([server, worker])
    except KeyboardInterrupt:
        steam_bot.close()
