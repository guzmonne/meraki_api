init:
	pip install -r requirements.txt

test:
	python -m unittest discover ./tests

html:
	cd docs && make html && cd ..

build:
	rm -rf build dist
	python setup.py sdist
	python setup.py bdist_wheel

deploy:
	twine upload dist/*
	make docs

docs:
	make html
	git add --all
	git commit -m "updated docs"
	git branch -D gh-pages
	git checkout -b gh-pages
	mkdir ../tmp_branch
	mkdir ../deleteme
	mv ./docs/_build/html/* ../tmp_branch
	mv * ../deleteme
	rm -rf ../deleteme
	mv ../tmp_branch/* .
	rm -rf ../tmp_branch
	touch .nojekyll
	git add --all
	git commit -m "updated docs"
	git push origin gh-pages --force
	git checkout master

.PHONY: init test docs html build deploy
