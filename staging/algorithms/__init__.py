import importlib
import json
from composer.trainer import TrainerHparams
import logging
import os


def register_all_algorithms():
    """
    Registers every algorithm in the folder with the
    trainer hparams using the associated metadata. Assumes that:
    - ``metadata.json`` has the ``hparams`` and ``hparams_key`` keys.
    - the hparams object is importable. e.g.
      from staging.algorithms.example_algorithm import ExampleAlgorithmHparams
    """

    root_folder = os.path.split(__file__)[0]
    subfolders = [f.path for f in os.scandir(root_folder) if f.is_dir()]

    logging.debug(f"Found {len(subfolders)} algorithm folders.")

    for folder in subfolders:
        metadata_path = os.path.join(folder, 'metadata.json')
        algorithm_name = os.path.split(folder)[-1]

        if not os.path.isfile(metadata_path):
            raise FileNotFoundError(f"{metadata_path} does not exist")

        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
            hparams_class = metadata[algorithm_name]['hparams']

        cls = getattr(importlib.import_module(name=f"staging.algorithms.{algorithm_name}"), hparams_class)
        TrainerHparams.register_class(
            field="algorithms",
            register_class=cls,
            class_key=algorithm_name,
        )


register_all_algorithms()