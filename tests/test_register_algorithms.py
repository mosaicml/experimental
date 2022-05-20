from composer.trainer import TrainerHparams

import experimental


def test_register_algorithms():
    algo_names = experimental.algorithms.register_all_algorithms()

    for algo in algo_names:
        assert algo in TrainerHparams.hparams_registry["algorithms"]
