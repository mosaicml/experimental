# experimental

`experimental` is a repository of algorithms that are either third-party contributions, or not sufficiently mature to contribute into `Composer`.

## Adding algorithms

To add an algorithm to `experimental`, create a folder `experimental/algorithms/your_algo_name`, with the following files:
* `__init__.py` that imports your algorithm class
* `metadata.json` with some metadata for your algorithm.
* `*.py` with your code!

The `metadata.json` should have the following fields:

```
{
    "name": "My Example Algorithm",
    "class_name": "ExampleAlgorithm",
    "tldr": "Just an Example",
    "attribution": "(Example et al, 2022)",
    "link": ""
}
```

Where the `"class_name"` field should be importable from `your_algo_name` folder. The other fields are optional.

For an example, see [ExampleAlgorithm](https://github.com/mosaicml/experimental/tree/main/experimental/algorithms/example_algorithm).

## Using experimental

To use experimental in your code, simply import the library and use with your trainer:

```python
from experimental.algorithms import ExampleAlgorithm
from composer import Trainer

trainer = Trainer(
    algorithms=[ExampleAlgorithm()],
    ...,
)
```

To use experimental with YAHP and our YAML config files, in your entrypoint code, call `register_all_algorithms()`, after which the algorithms will be accessible through YAHP, our
config management library.

```python
import experimental
from composer.trainer import TrainerHparams

experimental.algorithms.register_all_algorithms()
trainer = TrainerHparams.create(f="my_yaml_file.yaml")
trainer.fit()
```

The key in your YAML file is the folder name of the algorithm:
```
algorithms:
  - example_algorithm:
    alpha: 0.1
```
