# Django specific settings
import datetime
from timeit import default_timer as timer
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

from db.models import Person
from django.db import transaction
from faker import Faker

def main():
  fake = Faker()

  person_list_1 = []
  person_list_2 = []

  for _ in range(500):
    person = Person()
    person.name = fake.name()
    person.age = fake.pyint(min_value=10, max_value=100)
    person.birth_date = fake.date()
    person_list_1.append(person)

    person = Person()
    person.name = fake.name()
    person.age = fake.pyint(min_value=10, max_value=100)
    person.birth_date = fake.date()
    person_list_2.append(person)

  start = timer()
  for person in person_list_1:
    person.save()
  print( f"Time cost for no transaction = {timer() - start}s" )

  chunks = [person_list_2[x:x+10] for x in range(0, len(person_list_2), 10)]
  start = timer()
  for chunk in chunks:
    with transaction.atomic():
      for person in chunk:
        person.save()
  print( f"Time cost for transaction atomic = {timer() - start}s" )

if __name__ == '__main__':
  main()