pkg:
	newversion.py version
	python setup.py sdist bdist_wheel upload 
