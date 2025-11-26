PYTHON=python

setup:
	$(PYTHON) -m venv venv

install:
	venv\Scripts\activate && pip install -r requirements.txt

summary:
	venv\Scripts\activate && $(PYTHON) src/utils/build_summary.py

run:
	venv\Scripts\activate && $(PYTHON) src/run.py "Analyze ROAS drop"

test:
	venv\Scripts\activate && pytest tests
