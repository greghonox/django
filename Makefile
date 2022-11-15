clean_pycache:
	find . -type d -name __pycache__ -exec rm -r {} \+

run:
	venv/bin/uvicorn --host 127.0.0.1 --port 8000 --reload --log-level debug --app-dir src main:app

create-venv:
	python3 -m venv venv

install-requirements:
	venv/bin/python3 -m pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
