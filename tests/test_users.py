from app import app, db
import json
from tests.lib import login, setup


def test_login():

    client = app.test_client()

    token = login(client)

    assert isinstance(token, str)
