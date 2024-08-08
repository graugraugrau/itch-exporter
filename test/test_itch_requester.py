import unittest
import requests_mock

from itch_requester import ItchRequester, API_URL


class TestItchRequester(unittest.TestCase):
    def test_get_with_no_api_key(self):
        # Arrange
        requester = ItchRequester('')

        # Act
        with self.assertLogs(level='INFO') as cm:
            games = requester.get()

            # Assert
            self.assertEqual(len(games), 0)
            self.assertTrue(any('WARNING' in log for log in cm.output))

    def test_get_request_failed(self):
        # Arrange
        api_key = 'test'
        requester = ItchRequester(api_key)

        with requests_mock.Mocker() as m, self.assertLogs(level='INFO') as cm:
            m.get(API_URL.format(api_key), status_code=500)

            # Act
            games = requester.get()

            # Assert
            self.assertEqual(len(games), 0)
            self.assertTrue(any('ERROR' in log for log in cm.output))
