python -m venv env

source env\Scripts\activate

pip install sqlalchemy

pip freeze > requirements.txt
