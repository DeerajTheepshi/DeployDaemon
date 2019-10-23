virtualenv:
	( \
	virtualenv ./; \
	)

install:
	( \
	source bin/activate; \
	pip -V; \
    pip install -r requirements.txt; \
	python setup.py; \
    )
