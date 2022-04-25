import staging
import pytest
from composer.trainer import TrainerHparams
from composer.models import ResNetCIFARHparams
from composer.datasets import CIFAR10DatasetHparams, DataLoaderHparams


def test_register_algorithms():
    algo_names = staging.algorithms.register_all_algorithms()

    for algo in algo_names:
        assert algo in TrainerHparams.hparams_registry["algorithms"]
