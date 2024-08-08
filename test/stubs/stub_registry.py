from prometheus_client.registry import Collector


class StubRegistry:
    def __init__(self):
        self.register_collectors = []

    def register(self, collector: Collector):
        self.register_collectors.append(collector)

    def unregister(self, collector: Collector):
        self.register_collectors.remove(collector)
