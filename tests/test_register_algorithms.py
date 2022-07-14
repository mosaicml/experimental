from composer.trainer.trainer_hparams import TrainerHparams

import experimental


def test_register_algorithms():
    algo_names = experimental.algorithms.register_all_algorithms()

    assert len(algo_names) > 0
    assert TrainerHparams.hparams_registry is not None

    for algo in algo_names:
        assert algo in TrainerHparams.hparams_registry["algorithms"]
