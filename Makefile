
init:
	apt-get install python-gobject
	apt-get install libnotify-bin
	apt-get install libnotify-dev
	pip install -r requirements.txt

test:
	nosetests

run:
	python2 tl_en/tl_en.py

clean:
	find . -name "*.pyc" -exec rm -rf {} \;


.PHONY: init test clean
