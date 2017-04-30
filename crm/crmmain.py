from peewee import Model, CharField, DateField, BooleanField, IntegerField, SqliteDatabase, ForeignKeyField, \
    DecimalField
import os

if __name__ == "__main__":
    db_name = "crm.db"
else:
    db_name = "test_crm.db"

db_path = os.path.join(os.path.expanduser("~"), db_name)
db = SqliteDatabase(db_path)


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    LastName = CharField()
    FirstName = CharField()
    CellPhone = CharField()
    Email = CharField()
    Birthdate = DateField()
    AddressCurrent = CharField()
    AddressMailing = CharField()


class Dependent(BaseModel):
    Parent = ForeignKeyField(Person, related_name='Dependents')
    FirstName = CharField()
    LastName = CharField()
    Birthdate = DateField()


class Application(BaseModel):
    Applicant = ForeignKeyField(Person, related_name='Applications')
    Date = DateField()
    LoanPurpose = CharField()
    LoanType = CharField()
    CreditScore = CharField()
    Income = IntegerField()
    Assets = IntegerField()
    FTHB = BooleanField()
    Locked = BooleanField
    LockDate = DateField()
    LockRate = DecimalField()
    LockExpiration = DateField()
    Closed = BooleanField()
    CloseDate = DateField()
    PurchasePrice = IntegerField()
    LoanAmount = IntegerField()
    PropertyAddress = CharField()
    MaintenanceFee = IntegerField()
    Insurance = IntegerField()
    OtherFees = IntegerField()


class Preapproval(BaseModel):
    Person = ForeignKeyField(Person, related_name="Preapprovals")
    MaintenanceFee = IntegerField()
    Insurance = IntegerField()
    Taxes = IntegerField()
    Date = DateField()
    Rate = DecimalField()
    PurchasePrice = IntegerField()
    LoanAmount = IntegerField()
    CreditScore = IntegerField()
    Income = IntegerField()
    ClosingCosts = IntegerField()
    CashToClose = IntegerField()
    Reserves = IntegerField()
    DTI = DecimalField()
