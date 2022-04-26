from typing import Optional

from composer import Algorithm, Event, State
from composer.loggers import Logger


class ExampleAlgorithm(Algorithm):
    """ Example algorithm. The docstrings are important to include
    as we auto-read them to generate configuration files.

    Args:
      alpha (float): alpha factor

    """

    def __init__(self, alpha: float = 0.1) -> None:
        super().__init__()
        self.alpha = alpha

    def match(self, event: Event, state: State) -> bool:
        return True

    def apply(self, event: Event, state: State, logger: Logger) -> Optional[int]:
        pass
