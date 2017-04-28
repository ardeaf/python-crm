import os
import peewee
import pytest
from crm.crmmain import Person
from datetime import date

db_path = os.path.join(os.path.expanduser("~"), "crm.db")
db = peewee.SqliteDatabase(db_path)


@pytest.fixture()
def sample_person():
    last_name = "Lothbrok"
    first_name = "Ardeaf"
    cell_phone = "1234567890"
    dob = date(1995, 10, 1)
    current_address = "700 Google Dr. #21B, San Mateo, CA, 98102"
    mailing_address = "P.O. Box 3, San Mateo, CA, 98102"

    return Person(LastName=last_name,
                  FirstName=first_name,
                  CellPhone=cell_phone,
                  Birthdate=dob,
                  AddressCurrent=current_address,
                  AddressMailing=mailing_address)


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

# def test_add_person_saves_one_person():
