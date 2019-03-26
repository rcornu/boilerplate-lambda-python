all: test

package:
	pip3 install -r requirements.txt -t .

test: flake unittest clean

flake:
	flake8 .

unittest:
	python3 tests/*.py

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
