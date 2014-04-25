
clean:
	rm -f .coverage
	find . -name "*.py[co]" -delete
	find . -name "*.stl" -delete
	

test: clean
	nosetests -a '!slow'

coverage: clean
	nosetests --with-coverage --cover-package tailorscad -a '!slow'

integrations: clean
	nosetests --with-coverage --cover-package tailorscad -a slow
