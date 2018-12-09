run:
	venv/bin/python compartir/manage.py runserver

install:
	virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt

freeze:
	venv/bin/pip freeze

mm:
	venv/bin/python compartir/manage.py makemigrations

m:
	venv/bin/python compartir/manage.py migrate

clean:
	rm -R venv
