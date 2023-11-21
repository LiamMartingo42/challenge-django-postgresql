ifeq ($(OS),WINDOWS_NT)


build:
	pip install -r requirements.txt

run:
	python src/manage.py runserver

tests:

compose:
	docker compose -d up

else

build:
	sudo apt install python3
	pip3 install -r requirements.txt

run:
	python3 src/manage.py runserver

manage:
	python3 src/manage.py $(c)

tests:

compose:
	docker compose up


endif
