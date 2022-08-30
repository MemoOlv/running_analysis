all: check coverage tests

module = running_analysis

define checkDirectories
	mkdir --parents $(@D)
endef

data/processed/half_marathon_ensenada.csv: setup
	$(checkDirectories)
	python src/half_marathon_ensenada_dataframe.py "data/gpx/medio_maraton_ensenada.gpx" "data/processed/half_maraton_ensenada.csv"

.PHONY: \
	check \
	clean \
	coverage \
	format \
	mutants \
	setup \
	tests

check: 
	black --check --line-length 100 src
	black --check --line-length 100 tests
	black --check --line-length 100 ${module}
	flake8 --max-line-length 100 src
	flake8 --max-line-length 100 tests
	flake8 --max-line-length 100 ${module}
	mypy src
	mypy tests
	mypy ${module}

clean: 
	rm --force --recursive .*_cache
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force coverage.xml

coverage: setup
	pytest --cov=${module} --cov-report=term-missing --verbose

format:
	black --line-length 100 src
	black --line-length 100 tests
	black --line-length 100 ${module}

mutants: setup tests
	mutmut run --paths-to-mutate src
	mutmut run --paths-to-mutate ${module}

setup: clean
	pip install --editable .

tests: setup
	pytest --verbose