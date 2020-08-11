import pytest

from webtest import TestApp
from app.api import app


@pytest.yield_fixture(name="server")
def client_fixture():
    """ Client fixture """
    _server = TestApp(app)
    yield _server
