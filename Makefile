venv: venv/touchfile

build:
	python3 -m venv venv
	python3 -m pip freeze > requirements.txt

run:
	. venv/bin/activate;
	venv/bin/pip install pygame
	venv/bin/python ./code/main.py

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
	rm requirements.txt
