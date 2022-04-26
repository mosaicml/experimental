# staging

`staging` is a repository of algorithms that not quite ready for merging into Composer, either they are working implementions of algorithms we'd like to share with the community, or not quite proven yet in our experiments.

## Adding algorithms

To add an algorithm to `staging`, see the `example_algorithm` folder. Importantly, provide a `metadata.json`. The `hparams` key in the `metadata` will be used by YAPH to register the hparams object with the YAHP configuration manager.

## Using staging

To use staging in your code, simply import the library and use with your trainer:

```python
from staging.algorithms import ExampleAlgorithm
from composer import Trainer

trainer = Trainer(
    algorithms=[ExampleAlgorithm()],
    ...,
)
```

To use staging with YAPH and our YAML config files, in your entrypoint code, call `register_all_algorithms()`, after which the algorithms will be accessible through our config file system:

```python
import staging
from composer.trainer import TrainerHparams

staging.algorithms.register_all_algorithms()
trainer = TrainerHparams.create(f="my_yaml_file.yaml")
trainer.fit()
```


