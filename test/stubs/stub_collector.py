from typing import List, Dict, Any, Optional

from contract import ItchCollector


class StubCollector(ItchCollector):
    def __init__(self, results: Optional[List[Dict[str, Any]]] = None):
        if results is None:
            self.results = []
        else:
            self.results = results

    def get(self) -> List[Dict[str, Any]]:
        return self.results
