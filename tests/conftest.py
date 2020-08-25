import pytest

from app.api import create_app
import flask


@pytest.fixture
def app():
    flask_app = create_app()
    return flask_app


@pytest.fixture
def client(app):
    app.config["TESTING"] = True
    app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = False
    app.debug = True

    return app.test_client()
