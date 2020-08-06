import gevent.monkey

gevent.monkey.patch_all()

from gevent.pywsgi import WSGIServer
import gevent

from api import app
from bot import MatchStatsBot

worker = MatchStatsBot()

http_server = WSGIServer(("0.0.0.0", 8080), app)

server = gevent.spawn(http_server.serve_forever)
bot = gevent.spawn(worker.prompt_login)

try:
    gevent.joinall([server, bot])
except KeyboardInterrupt:
    worker.close()
