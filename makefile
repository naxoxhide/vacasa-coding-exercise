VENV_NAME=venv_vacasa

ifeq ($(OS),Windows_NT)
	ACTIVATE=$(VENV_NAME)\Scripts\activate
else
	ACTIVATE=source $(VENV_NAME)/bin/activate
endif

venv:
	python -m venv $(VENV_NAME)
	@echo "Virtual environment created."

install: venv
	$(ACTIVATE) && pip install -r requirements.txt
	@echo "Installed dependencies."

run:
	$(ACTIVATE) && flask run --host=0.0.0.0 --port=3000

test:
	$(ACTIVATE) && pytest test_app.py

clean:
	rm -rf __pycache__ *.pyc $(VENV_NAME)
	@echo "Clean project."
