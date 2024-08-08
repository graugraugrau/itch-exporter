import abc
from typing import Dict, Any, List


class ItchCollector(abc.ABC):
    @abc.abstractmethod
    def get(self) -> List[Dict[str, Any]]:
        pass
