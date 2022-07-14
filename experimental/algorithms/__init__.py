import importlib
import json
import logging
import os
from typing import List

from composer.algorithms.algorithm_hparams_registry import algorithm_registry


def is_algorithm_folder(f: os.DirEntry) -> bool:
    """Exclude directories that start with _ or ."""
    folder_name = os.path.basename(f.path)
    return f.is_dir() and not folder_name.startswith('_') and not folder_name.startswith('.')


def register_all_algorithms() -> List[str]:
    """Registers every algorithm in the folder with the trainer hparams using the associated metadata.

    Assumes that the algorithm has docstrings that can be used to auto-generated an hparams class.

    """

    root_folder = os.path.split(__file__)[0]
    subfolders = [f.path for f in os.scandir(root_folder) if is_algorithm_folder(f)]
    algorithm_names = [os.path.split(f)[-1] for f in subfolders]

    for folder in subfolders:

        # the folder name (e.g. example_algorithm) is the key
        algorithm_name = os.path.split(folder)[-1]

        # retrieve the class name from the metadata.json
        # this should be importable with
        # from experimental.algorithms.{algorithm_name} import {class_name}
        metadata_path = os.path.join(folder, 'metadata.json')
        if not os.path.isfile(metadata_path):
            raise FileNotFoundError(f"{metadata_path} does not exist")

        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
            class_name = metadata['class_name']

        # import the algorithm class and add to the algorithm registry
        cls = getattr(
            importlib.import_module(name=f"experimental.algorithms.{algorithm_name}"),
            class_name,
        )

        if algorithm_name in algorithm_registry:
            raise ValueError(f'Duplicate algorith name {algorithm_name} already exists in registry.')

        algorithm_registry[algorithm_name] = cls

    logging.info(f"Registered {len(subfolders)} algorithms: {algorithm_names}")
    return algorithm_names
