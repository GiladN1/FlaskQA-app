import pytest


@pytest.fixture
def url():
    return "http://qa-webapp:5000/health"
