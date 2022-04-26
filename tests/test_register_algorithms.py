from composer.trainer import TrainerHparams

import staging


def test_register_algorithms():
    algo_names = staging.algorithms.register_all_algorithms()

    for algo in algo_names:
        assert algo in TrainerHparams.hparams_registry["algorithms"]
