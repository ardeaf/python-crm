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
    database.drop_tables([Person, Dependent, Application, Preapproval], True)


@pytest.fixture(scope='module')
def sample_person():
    return Person(LastName="Lothbrok",
                  FirstName="Ardeaf",
                  CellPhone="1234567890",
                  Email="ardeaf@lothbrok.com",
                  Birthdate=date(1995, 10, 1),
                  AddressCurrent="700 Google Dr. #21B, San Mateo, CA, 98102",
                  AddressMailing="P.O. Box 3, San Mateo, CA, 98102")


@pytest.fixture(scope='module')
def sample_dependent():
    return Dependent(LastName="Lothbrok",
                     FirstName="Bjorn",
                     Birthdate=date(2005, 6, 1),
                     Parent=1)


@pytest.fixture(scope='module')
def sample_application():
    return Application(Applicant=1,
                       Date=date(2005, 1, 1),
                       LoanPurpose="Purchase",
                       LoanType="Conventional",
                       CreditScore="750",
                       Income=5500,
                       Assets=150000,
                       FTHB=True,
                       Locked=True,
                       LockDate=date(2005, 1, 1),
                       LockRate=4.250,
                       LockExpiration=date(2005, 2, 16),
                       Closed=True,
                       CloseDate=date(2005, 2, 16),
                       PurchasePrice=800000,
                       LoanAmount=600000,
                       PropertyAddress="800 Microsoft Rd. Suite 500, San Lorenzo, CA, 99122",
                       MaintenanceFee=452,
                       Insurance=140,
                       OtherFees=250)


@pytest.fixture(scope='module')
def sample_preapproval():
    return Preapproval(Person=1,                    #This is not an accurate preapproval at all.
                       MaintenanceFee=600,
                       Insurance=40,
                       Taxes=100,
                       Date=date(2005, 1, 1),
                       Rate=4.500,
                       PurchasePrice=400000,
                       LoanAmount=300000,
                       CreditScore=650,
                       Income=5500,
                       ClosingCosts=5000,
                       CashToClose=120000,
                       Reserves=30000,
                       DTI=45)