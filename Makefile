ifeq ($(OS),WINDOWS_NT)

migrate:
	python src/manage.py makemigrations 
	python src/manage.py migrate 

build:
	pip install -r requirements.txt

run:
	python src/manage.py runserver

tests:

compose:
	docker compose -d up

else

migrate:
	python3 src/manage.py makemigrations 
	python3 src/manage.py migrate 
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
