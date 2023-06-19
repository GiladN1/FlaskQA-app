import requests


def test_url(url):
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == "server is up"