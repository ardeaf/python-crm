import os
import peewee
from peewee import ForeignKeyField
import pytest
from crm.crmmain import Person
from datetime import date

db_path = os.path.join(os.path.expanduser("~"), "test_crm.db")
db = peewee.SqliteDatabase(db_path)

@pytest.fixture()
def sample_person():
    return Person(LastName="Lothbrok",
                  FirstName="Ardeaf",
                  CellPhone="1234567890",
                  Email="ardeaf@lothbrok.com",
                  Birthdate=date(1995, 10, 1),
                  AddressCurrent="700 Google Dr. #21B, San Mateo, CA, 98102",
                  AddressMailing="P.O. Box 3, San Mateo, CA, 98102")

"""@pytest.fixture()
def sample_dependent():
    return Dependent(LastName="Lothbrok",
                     FirstName="Bjorn",
                     Birthdate=date(2005, 6, 1),
                     Parent=ForeignKeyField(Person, related_name='Dependents'))"""

def test_query_matches_saved_person(sample_person):
    db.connect()
    db.create_table(Person, True)
    sample_person.save()

    try:
        assert sample_person == Person.get(Person.LastName == sample_person.LastName)
    except (Person.DoesNotExist, AssertionError) as e:
        raise e
    finally:
        # clean up db
        sample_person.delete_instance()
        db.close()

#def test_dependent_parent_equals_person():

