import importlib
import json
import logging
import os
from typing import List

from composer.trainer import TrainerHparams


def is_algorithm_folder(f) -> bool:
    """Exclude directories that start with _ or ."""
    folder_name = os.path.basename(f.path)
    return f.is_dir() and not folder_name.startswith('_') and not folder_name.startswith('.')


def register_all_algorithms() -> List[str]:
    """Registers every algorithm in the folder with the trainer hparams using the associated metadata. Assumes that:

    - ``metadata.json`` has the ``hparams`` and ``hparams_key`` keys.
    - the hparams object is importable. e.g.
      from staging.algorithms.example_algorithm import ExampleAlgorithmHparams
    """

    root_folder = os.path.split(__file__)[0]
    subfolders = [f.path for f in os.scandir(root_folder) if is_algorithm_folder(f)]
    algorithm_names = [os.path.split(f)[-1] for f in subfolders]

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

    logging.info(f"Registered {len(subfolders)} algorithms: {algorithm_names}")
    return algorithm_names
