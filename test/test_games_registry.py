import unittest

from test.stubs.common import create_game
from test.stubs.stub_collector import StubCollector
from test.stubs.stub_registry import StubRegistry
from games_registry import GameRegistry


class TestGameRegistry(unittest.TestCase):
    def test_update_new(self):
        # Arrange
        collector_stub = StubCollector([create_game(1)])
        register_stub = StubRegistry()
        game_registry = GameRegistry(collector_stub, register_stub)

        # Act
        game_registry.update()

        # Assert
        self.assertEqual(len(register_stub.register_collectors), 1)
        metric = list(register_stub.register_collectors[0].collect())
        self.assertEqual(metric[0].name, 'itch_views_count')
        self.assertEqual(metric[1].name, 'itch_downloads_count')
        self.assertEqual(metric[2].name, 'itch_purchases_count')

    def test_update_existing(self):
        # Arrange
        collector_stub = StubCollector([create_game(1)])
        register_stub = StubRegistry()
        game_registry = GameRegistry(collector_stub, register_stub)

        # Act
        game_registry.update()
        collector_stub.results = [create_game(1, views=10, downloads=5)]
        game_registry.update()

        # Assert
        self.assertEqual(len(register_stub.register_collectors), 1)
        metric = list(register_stub.register_collectors[0].collect())
        self.assertEqual(metric[0].name, 'itch_views_count')
        self.assertEqual(metric[0].samples[0].value, 10)
        self.assertEqual(metric[1].name, 'itch_downloads_count')
        self.assertEqual(metric[1].samples[0].value, 5)
        self.assertEqual(metric[2].name, 'itch_purchases_count')

    def test_update_remove(self):
        collector_stub = StubCollector([create_game(1)])
        register_stub = StubRegistry()
        game_registry = GameRegistry(collector_stub, register_stub)

        # Act
        game_registry.update()
        collector_stub.results = []
        game_registry.update()

        # Assert
        self.assertEqual(len(register_stub.register_collectors), 1)
        metric = list(register_stub.register_collectors[0].collect())
        self.assertEqual(metric[0].name, 'itch_views_count')
        self.assertEqual(len(metric[0].samples), 0)
