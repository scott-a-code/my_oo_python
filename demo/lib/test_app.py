import pytest
import requests
from unittest import mock

from .api import fetch_houses
from .house import House
from .app import CLI

class TestAPICase():
    def test_fetch_houses(self, house_test_list):
        mock_response = mock.Mock()
        mock_response.json.return_value = house_test_list

        mock_requests_get = mock.Mock(return_value=mock_response)

        requests.get = mock_requests_get
        fetch_houses()
        mock_requests_get.assert_called_with('https://anapioficeandfire.com/api/houses')


class TestCLICase():
    @pytest.mark.parametrize('input, expected', [("1", True), ("0", False), ("4", False), ("3", True)])
    def test_valid_input(self, input, expected, monkeypatch):
        monkeypatch.setattr(House, "all", [{}, {}, {}])
        assert CLI.valid_input(input) == expected

    def test_goodbye(self, capsys):
        CLI.goodbye()
        out, err = capsys.readouterr()
        assert "May the North be with you" in out

    def test_show_house(self, capsys, house_test_data):
        self._original_find_by_input = House.find_by_input
        mock_find_by_input = mock.Mock(return_value=House(house_test_data))
        House.find_by_input = mock_find_by_input

        CLI().show_house()
        House.find_by_input = self._original_find_by_input

        mock_find_by_input.assert_called()
        out, err = capsys.readouterr()
        assert house_test_data['name'] in out