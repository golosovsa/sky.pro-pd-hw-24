"""
    pytest config
    flask app fixture
"""

from pytest import fixture
from app import create_app


@fixture(scope="session")
def app():
    flask_app = create_app()
    return flask_app
