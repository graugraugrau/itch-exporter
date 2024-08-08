from prometheus_client import CollectorRegistry

from contract import ItchCollector
from games_collector import GamesCollector


class GameRegistry:
    def __init__(self, collector: ItchCollector, registry: CollectorRegistry):
        self._game_collector = GamesCollector()
        self._registry = registry
        self._itch_collector = collector

        self._registry.register(self._game_collector)

    def update(self) -> None:
        games = self._itch_collector.get()
        self._update_games(games)

    def _update_games(self, games):
        self._game_collector.update(games)
