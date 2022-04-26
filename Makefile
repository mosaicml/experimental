# several pytest settings
PYTHON ?= python  # Python command
PYTEST ?= pytest  # Pytest command
PYRIGHT ?= pyright  # Pyright command. Pyright must be installed seperately -- e.g. `node install -g pyright`
EXTRA_ARGS ?=  # extra arguments for pytest

dirs := staging tests

# run this to autoformat your code
style:
	$(PYTHON) -m isort $(dirs)
	$(PYTHON) -m yapf -rip $(dirs)
	$(PYTHON) -m docformatter -ri --wrap-summaries 120 --wrap-descriptions 120 $(dirs)

# this only checks for style & pyright, makes no code changes
lint:
	$(PYTHON) -m isort -c --diff $(dirs)
	$(PYTHON) -m yapf -dr $(dirs)
	$(PYTHON) -m docformatter -r --wrap-summaries 120 --wrap-descriptions 120 $(dirs)
	$(PYRIGHT) $(dirs)

test:
	$(PYTHON) -m $(PYTEST) $(EXTRA_ARGS)

clean-notebooks:
	$(PYTHON) scripts/clean_notebooks.py -i notebooks/*.ipynb

.PHONY: test lint style clean-notebooks
