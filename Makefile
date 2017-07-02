init:
	pip install -r requirements.txt

test:
	python -m unittest discover ./tests

docs:
	cd docs
	make html
	cd ..

.PHONY: init test docs
