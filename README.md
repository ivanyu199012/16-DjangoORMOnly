# Using Django ORM only without web server

## Detail Guide
[Using Django ORM only without web server]()

## Requirements
- Python 3.10.11
- Django 4.0.4

## Setup
```cmd
git clone https://github.com/ivanyu199012/16-DjangoORMOnly.git
cd 16-DjangoORMOnly

python -m venv ormOnlyEnv
ormOnlyEnv\Scripts\activate

pip install -r requirements.txt
```

## Create sqlite database
```cmd
python manage.py migrate
```

## Run
```cmd
python saveSingleRecord.py
python saveMultipleRecords.py
```

## Output
```cmd
Project started!!
Saved!!

Time cost for no transaction = 2.268s
Time cost for transaction atomic = 0.238s
```

