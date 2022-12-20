import pytest
from server import create_app
from flask import url_for

@pytest.fixture
def app():
    app = create_app()
    # print('\ntest start ...')
    yield app
    # print("\ntest end")


@pytest.fixture
def runner():
    return 'running'

def test_runner(runner):
    assert runner=='running'

def test_ping(client):
    res = client.get(url_for('app2.ping'))
    assert res.json == {'ping': 'pong'}

def test_index(client):
    res = client.get('/')
    assert res


def test_api(client):
    res = client.get(url_for('app2.api'))
    print('45678')
    assert res
    



