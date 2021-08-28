.DEFAULT_GOAL := default

.PHONY: default
default: black isort flake8

.PHONY: requirements
req: _requirements.txt.pyc _requirements-test.txt.pyc

_requirements.txt.pyc: requirements.txt
	#pip install -r --upgrade requirements.txt
	pip install -r requirements.txt
	echo > _requirements.txt.pyc

_requirements-test.txt.pyc: requirements-test.txt
	pip install -r requirements-test.txt
	echo > _requirements-test.txt.pyc

.PHONY: black
black:
	black dot2

.PHONY: isort
isort:
	isort dot2

.PHONY: flake8
flake8:
	flake8 dot2

#.\venv\Scripts\activate.bat
