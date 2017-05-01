import os
from peewee import SqliteDatabase
import pytest
from crm.crmmain import Person, Dependent, Application, Preapproval, Job
from datetime import date

@pytest.fixture(scope='session')
def db():
    database_path = os.path.join(os.path.expanduser("~"), "test_crm.db")
    database = SqliteDatabase(database_path)
    yield database
    database.drop_tables([Person, Dependent, Application, Preapproval, Job], True)


@pytest.fixture(scope='module')
def sample_person():
    return Person(last_name="Lothbrok",
                  first_name="Ardeaf",
                  cellphone="1234567890",
                  email="ardeaf@lothbrok.com",
                  birthdate=date(1995, 10, 1),
                  address_current="700 Google Dr. #21B, San Mateo, CA, 98102",
                  address_mailing="P.O. Box 3, San Mateo, CA, 98102")


@pytest.fixture(scope='module')
def sample_dependent():
    return Dependent(last_name="Lothbrok",
                     first_name="Bjorn",
                     birthdate=date(2005, 6, 1),
                     parent=1)


@pytest.fixture(scope='module')
def sample_application():
    return Application(person=1,
                       date=date(2005, 1, 1),
                       loan_purpose="Purchase",
                       loan_type="Conventional",
                       credit_score="750",
                       income=5500,
                       assets=150000,
                       fthb=True,
                       locked=True,
                       lock_date=date(2005, 1, 1),
                       lock_rate=4.250,
                       lock_expiration=date(2005, 2, 16),
                       closed=True,
                       close_date=date(2005, 2, 16),
                       purchase_price=800000,
                       loan_amount=600000,
                       property_address="800 Microsoft Rd. Suite 500, San Lorenzo, CA, 99122",
                       maintenance_fee=452,
                       insurance=140,
                       other_fees=250)


@pytest.fixture(scope='module')
def sample_preapproval():
    return Preapproval(person=1,                    #This is not an accurate preapproval at all.
                       maintenance_fee=600,
                       insurance=40,
                       taxes=100,
                       date=date(2005, 1, 1),
                       rate=4.500,
                       purchase_price=400000,
                       loan_amount=300000,
                       credit_score=650,
                       income=5500,
                       closing_costs=5000,
                       cash_to_close=120000,
                       reserves=30000,
                       dti=45)

@pytest.fixture(scope='module')
def sample_job():
    return Job(person=1,
               application=1,
               employer="Riot Games",
               position="Developer",
               monthly_income=5500)