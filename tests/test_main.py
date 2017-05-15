import os

from tests.fixtures import db_fixture, sample_application
from crm.models import Person, Dependent, Application, Preapproval, Job, Asset, Rental, Referral, Communication
from crm import main
from peewee import fn, CharField, DateField, BooleanField, IntegerField, DecimalField, TextField, ForeignKeyField
from hypothesis import given, settings, event, assume
from hypothesis.strategies import text, booleans, integers, builds, decimals, none
from hypothesis.extra.datetime import dates


# Helper function. Returns dict of field names and the corresponding field type, given an object.
def fields_to_dict(obj):
    diction =  {field_name: hypothesis_strategy(field) for field_name, field in zip(obj._meta.sorted_field_names, obj._meta.sorted_fields)
            if field_name != 'id'}

    return diction

# Helper function.  Reads the given field type and returns the associated hypothesis strategy we are going to use.
def hypothesis_strategy(field_type):
    if isinstance(field_type, ForeignKeyField):
        return none()
    if isinstance(field_type, CharField) or isinstance(field_type, TextField):
        return text()
    if isinstance(field_type, DateField):
        return dates()
    if isinstance(field_type, BooleanField):
        return booleans()
    if isinstance(field_type, IntegerField):
        return integers()
    if isinstance(field_type, DecimalField):
        return decimals()

@given(builds(Person, **fields_to_dict(Person)),
       builds(Dependent, **fields_to_dict(Dependent)),
       builds(Application, **fields_to_dict(Application)))
def test_insert(db_fixture, person, dependent, application):
    with db_fixture.atomic() as txn:
        person.create_table(True)
        dependent.create_table(True)
        application.create_table(True)

        before_count = (person.select().count(), dependent.select().count(), application.select().count())

        main.insert(db_fixture, person)

        random_person = person.select().order_by(fn.Random()).limit(1).get()
        dependent.parent = random_person
        application.person = random_person

        main.insert(db_fixture, dependent)
        main.insert(db_fixture, application)

        after_count = (person.select().count(), dependent.select().count(), application.select().count())

        for counts in zip(before_count, after_count):
            assert counts[0] == counts[1] - 1
