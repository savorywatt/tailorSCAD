
clean:
	rm -f .coverage
	find . -name "*.py[co]" -delete
	

test: clean
	nosetests -a '!slow'

coverage: clean
	nosetests --with-coverage --cover-package tailorscad -a '!slow'

integrations: clean
	nosetests --with-coverage --cover-package tailorscad -a slow
