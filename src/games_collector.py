from datetime import datetime
from typing import Dict, Any, List

from prometheus_client.metrics_core import CounterMetricFamily, InfoMetricFamily
from prometheus_client.registry import Collector


class GamesCollector(Collector):
    def __init__(self):
        self._current_game_infos = []

    def collect(self):
        views_metric = CounterMetricFamily(
            'itch_views_count',
            'Views count',
            labels=['game_id'])
        downloads_metric = CounterMetricFamily(
            'itch_downloads_count',
            'Downloads count',
            labels=['game_id'])
        purchases_metric = CounterMetricFamily(
            'itch_purchases_count',
            'Purchases count',
            labels=['game_id'])
        info_metric = InfoMetricFamily(
            'itch_meta',
            'Meta information',
            labels=['game_id'])

        for game_info in self._current_game_infos:
            game_info_id = [str(game_info['id'])]
            views_metric.add_metric(game_info_id, game_info['views_count'])
            downloads_metric.add_metric(game_info_id, game_info['downloads_count'])
            purchases_metric.add_metric(game_info_id, game_info['purchases_count'])
            info_metric.add_metric(game_info_id, value={
                'title': game_info['title'],
                'description': game_info.get('short_text', ''),
                'published': str(GamesCollector.__parse_time(game_info.get('published_at'))),
                'created': str(GamesCollector.__parse_time(game_info.get('created_at')))
            })

        yield views_metric
        yield downloads_metric
        yield purchases_metric
        yield info_metric

    def update(self, game_infos: List[Dict[str, Any]]) -> None:
        self._current_game_infos = game_infos

    @staticmethod
    def __parse_time(date_str: str) -> int:
        if date_str is None:
            return 0

        return int(datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
