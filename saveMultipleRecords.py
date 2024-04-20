import datetime
from timeit import default_timer as timer
from faker import Faker

##############################
# Django specific settings (Please this BEFORE import model class)
##############################
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
##############################

# Import your models for use in your script
from django.db import transaction
from db.models import Person

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
  print(f"Time cost for no transaction = {round(timer() - start, 3)}s")

  # chunk the list to be sublist and each contains 10 elements
  chunks = [person_list_2[x:x + 10] for x in range(0, len(person_list_2), 10)]
  start = timer()
  for chunk in chunks:
    with transaction.atomic():
      for person in chunk:
        person.save()
  print(f"Time cost for transaction atomic = {round(timer() - start, 3)}s")


if __name__ == '__main__':
  main()
