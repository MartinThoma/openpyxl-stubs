upload:
	make clean
	python setup.py sdist bdist_wheel && twine upload dist/*

clean:
	rm -rf build dist *.egg-info
