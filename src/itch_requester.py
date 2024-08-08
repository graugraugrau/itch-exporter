import logging
from typing import Dict, Any, List
import requests

from contract import ItchCollector

API_URL = 'http://itch.io/api/1/{0}/my-games'


class ItchRequester(ItchCollector):
    def __init__(self, api_key: str):
        self._api_key = api_key

    def get(self) -> List[Dict[str, Any]]:
        if not self._api_key:
            logging.warning('No API key was provided!')
            return []

        url = API_URL.format(self._api_key)
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            logging.error('Request to %s failed. Got response %i', url, response.status_code)
            return []

        json = response.json()
        return json['games']
