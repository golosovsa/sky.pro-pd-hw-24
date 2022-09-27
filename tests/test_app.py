import pytest
from flask.testing import FlaskClient


class TestApp:

    def test_api_perform_query(self, client: FlaskClient):
        url = "/perform_query"
        payload = {
            'file_name': 'apache_logs.txt',
            'cmd1': 'regex',
            'value1': 'images/\\w+\\.png',
            'cmd2': 'sort',
            'value2': 'asc'
        }
        response = client.post(url, data=payload)
        assert response.status_code == 200
        for line in response.text.split("\n"):
            assert ".png" in line
