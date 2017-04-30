import os
from peewee import SqliteDatabase
import pytest
from crm.crmmain import Person, Dependent, Application, Preapproval
from datetime import date


@pytest.fixture(scope='session')
def db():
    database_path = os.path.join(os.path.expanduser("~"), "test_crm.db")
    database = SqliteDatabase(database_path)
    yield database
    database.drop_tables([Person, Dependent, Application], True)


@pytest.fixture()
def sample_person():
    return Person(LastName="Lothbrok",
                  FirstName="Ardeaf",
                  CellPhone="1234567890",
                  Email="ardeaf@lothbrok.com",
                  Birthdate=date(1995, 10, 1),
                  AddressCurrent="700 Google Dr. #21B, San Mateo, CA, 98102",
                  AddressMailing="P.O. Box 3, San Mateo, CA, 98102")


@pytest.fixture()
def sample_dependent():
    return Dependent(LastName="Lothbrok",
                     FirstName="Bjorn",
                     Birthdate=date(2005, 6, 1),
                     Parent=1)


@pytest.fixture()
def sample_application():
    return Application(Applicant=1,
                       Date=date(2005, 1, 1),
                       LoanPurpose="Purchase",
                       LoanType="Conventional",
                       CreditScore="750",
                       FTHB=True,
                       LockDate=date(2005, 1, 1),
                       LockRate=4.250,
                       LockExpiration=date(2005, 2, 16),
                       CloseDate=date(2005, 2, 16),
                       ClosePurchasePrice=800000,
                       CloseLoanAmount=600000,
                       ClosePropertyAddress="800 Microsoft Rd. Suite 500, San Lorenzo, CA, 99122",
                       CloseMaintenanceFee=452,
                       CloseInsurance=140,
                       CloseOtherFees=250,
                       CloseRate=4.250)


@pytest.fixture()
def sample_preapproval():
    return Preapproval(Person=1,                    #This is not an accurate preapproval at all.
                       MaintenanceFee=600,
                       Insurance=40,
                       Taxes=100,
                       Date=date(2005, 1, 1),
                       Rate=4.500,
                       PurchasePrice=400000,
                       LoanAmount=300000,
                       IncomeUsed=5500,
                       AssetsUsed=120000,
                       Reserves=30000,
                       DTI=45)

def test_query_matches_saved_person(sample_person, db):
    db.create_table(Person, True)
    sample_person.save()
    assert sample_person.FirstName == Person.get(Person.LastName == sample_person.LastName).FirstName


def test_dependent_parent_equals_person_from_query(sample_dependent, sample_person, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Dependent, True)
    sample_dependent.save()

    assert sample_dependent.Parent == Person.get(Person.id == 1)  # id is 1 since we added only 1 person


def test_application_applicant_equals_person_from_query(sample_person, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Application, True)
    sample_application.save()

    assert sample_application.Applicant == Person.get(Person.id == 1)  # id is 1 since we added only 1 person


def test_create_application_by_querying_name(sample_person, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    first_name = Person.get(Person.FirstName == sample_person.FirstName).FirstName
    last_name = Person.get(Person.LastName == sample_person.LastName).LastName

    db.create_table(Application, True)
    sample_application.Applicant == Person.get(Person.FirstName == first_name, Person.LastName == last_name)
    sample_application.save()

    assert sample_application.Applicant == Person.get(Person.id == 1)


def test_create_preapproval_by_querying_name(sample_person, sample_preapproval, db):
    db.create_table(Person, True)
    sample_person.save()

    first_name = Person.get(Person.FirstName == sample_person.FirstName).FirstName
    last_name = Person.get(Person.LastName == sample_person.LastName).LastName

    db.create_table(Preapproval, True)
    sample_preapproval.Person == Person.get(Person.FirstName == first_name, Person.LastName == last_name)
    sample_preapproval.save()

    assert sample_preapproval.Person == Person.get(Person.id == 1)














