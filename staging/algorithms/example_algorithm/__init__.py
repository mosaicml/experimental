import composer
from composer.trainer import TrainerHparams
from example_algorithm import ExampleAlgorithmHparams
"""
The module should register the class with TrainerHparams
so that it is available via YAHP.
"""
TrainerHparams.register_class(
    field="algorithms",
    register_class=ExampleAlgorithmHparams,
    class_key="example_algorithm",
)
