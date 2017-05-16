import os

from tests.fixtures import db_fixture, sample_application
from crm.models import Person, Dependent, Application, Preapproval, Job, Asset, Rental, Referral, Communication
from crm import main
from peewee import fn, CharField, DateField, BooleanField, IntegerField, DecimalField, TextField, ForeignKeyField
from playhouse.shortcuts import model_to_dict
from hypothesis import given, settings, event, assume, note
from hypothesis.strategies import text, booleans, integers, builds, decimals, none
from hypothesis.extra.datetime import dates


# Helper functions.

# Returns dict of field names and the corresponding field type, given an object.
def fields_to_dict(obj):
    diction =  {field_name: hypothesis_strategy(field) for field_name, field in zip(obj._meta.sorted_field_names, obj._meta.sorted_fields)
            if field_name != 'id'}

    return diction


# Reads the given field type and returns the associated hypothesis strategy we are going to use.
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
        return integers(min_value=-(2 ** 63 - 1), max_value=2 ** 63 - 1)
    if isinstance(field_type, DecimalField):
        return decimals(min_value=-(2 ** 63 - 1), max_value=2 ** 63 - 1)


@given(builds(Person, **fields_to_dict(Person)),
       builds(Dependent, **fields_to_dict(Dependent)),
       builds(Application, **fields_to_dict(Application)),
       builds(Preapproval, **fields_to_dict(Preapproval)),
       builds(Job, **fields_to_dict(Job)),
       builds(Asset, **fields_to_dict(Asset)),
       builds(Rental, **fields_to_dict(Rental)),
       builds(Referral, **fields_to_dict(Referral)),
       builds(Communication, **fields_to_dict(Communication)))
def test_insert_and_remove(db_fixture, person, dependent, application, preapproval, job, asset, rental, referral, communication):
    with db_fixture.atomic() as txn:
        objects = [person, dependent, application, preapproval, job, asset, rental, referral, communication]
        before_count = list()

        for object in objects:
            object.create_table(True)
            note("Initial {} = {}".format(object.__class__.__name__, model_to_dict(object)))
            before_count.append(object.select().count())

        for object in objects:
            if isinstance(object, Person):
                main.insert(db_fixture, object)

            random_person = Person.select().order_by(fn.Random()).limit(1).get()

            for key, value in model_to_dict(object).items():
                if key in ['person', 'parent', 'referrer', 'referral']:
                    object.key = random_person
                    setattr(object, "{}_id".format(key), random_person.id)

            try:  # Need to do this try in case the application table is empty.
                random_application = Application.select().order_by(fn.Random()).limit(1).get()
                for key, value in model_to_dict(object).items():
                    if key in ['application']:
                        object.key = random_application
                        setattr(object, "{}_id".format(key), random_application.id)
            except Application.DoesNotExist:
                pass

            if not isinstance(object, Person):
                main.insert(db_fixture, object)

        after_count = [object.select().count() for object in objects]

        for counts in zip(before_count, after_count):
            assert counts[0] == counts[1] - 1

        # Done inserting, now test removing.
        before_remove_count = list()
        for object in objects:
            before_remove_count.append(object.select().count())
            main.remove(db_fixture, object)

        after_remove_count = [object.select().count() for object in objects]

        for counts in zip(before_remove_count, after_remove_count):
            assert counts[0] - 1 == counts[1]
