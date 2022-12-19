import pytest
from app.server import create_app
from flask import url_for

@pytest.fixture
def app():
    app = create_app()
    print('\ntest start ...')
    yield app
    print("\ntest end")

def test_index(client):
    res = client.get('/')
    assert res


def test_api(client):
    res = client.get(url_for('app2.api'))
    print('45678')
    assert res



