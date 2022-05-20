from dataclasses import dataclass
from typing import Optional

import yahp as hp
from composer import Algorithm, Event, State
from composer.algorithms import AlgorithmHparams
from composer.loggers import Logger


class ExampleAlgorithm(Algorithm):

    def __init__(self, alpha: float = 0.1) -> None:
        super().__init__()
        self.alpha = alpha

    def match(self, event: Event, state: State) -> bool:
        return True

    def apply(self, event: Event, state: State, logger: Logger) -> Optional[int]:
        pass


@dataclass
class ExampleAlgorithmHparams(AlgorithmHparams):

    alpha: float = hp.optional('alpha factor', default=0.1)

    def initialize_object(self) -> ExampleAlgorithm:
        return ExampleAlgorithm(alpha=self.alpha)