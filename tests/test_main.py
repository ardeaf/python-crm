import os

from tests.fixtures import db_fixture
from crm.models import Person, Dependent, Application, Preapproval, Job, Asset, Rental, Referral, Communication
from crm import main
from hypothesis import given
import hypothesis.strategies as st

@given(st.builds(Person,
                 last_name=st.text(), first_name=st.text(), cellphone=st.text(), email=st.text(), birthdate=st.text(),
                 address_current=st.text(), address_mailing=st.text(), is_realtor=st.booleans()))
def test_insert(db_fixture, person):
    with db_fixture.atomic() as txn:
        person.create_table(type(person))
        before_count = person.select().count()
        main.insert(person, db_fixture)
        after_count = person.select().count()
        assert before_count == after_count - 1
        txn.rollback()