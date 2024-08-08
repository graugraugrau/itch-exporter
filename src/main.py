import os
import time

from prometheus_client import (
    start_http_server,
    disable_created_metrics,
    REGISTRY,
    GC_COLLECTOR,
    PLATFORM_COLLECTOR,
    PROCESS_COLLECTOR
)

from games_registry import GameRegistry
from itch_requester import ItchRequester

INTERVAL = int(os.environ.get('REQUEST_INTERVAL', 3600))
API_KEY = os.environ.get('API_KEY', '')
ITCH_REQUESTER = ItchRequester(API_KEY)
GAMES_REGISTRY = GameRegistry(ITCH_REQUESTER, REGISTRY)


if __name__ == '__main__':
    REGISTRY.unregister(PROCESS_COLLECTOR)
    REGISTRY.unregister(PLATFORM_COLLECTOR)
    REGISTRY.unregister(GC_COLLECTOR)
    disable_created_metrics()
    start_http_server(8000)

    while True:
        GAMES_REGISTRY.update()
        time.sleep(INTERVAL)
