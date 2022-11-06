PYTHON=3.8
BASENAME=$(shell basename $(CURDIR))
CONDA_CH=conda-forge defaults

env:
	conda create -n $(BASENAME)  python=$(PYTHON)

setup:
	pip install -r requirements.txt 

run-server:
	python main.py
