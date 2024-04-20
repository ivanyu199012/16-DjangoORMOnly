# Django specific settings
import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

from db.models import Person

def main():
  print("Project started!!")
  person = Person()
  person.name = 'John Doe'
  person.age = 30
  person.birth_date = datetime.datetime(1963, 2, 5)
  person.save()
  print("Saved!!")

if __name__ == '__main__':
  main()