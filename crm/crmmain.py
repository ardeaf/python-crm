from peewee import Model, CharField, DateField, BooleanField, IntegerField, SqliteDatabase, ForeignKeyField
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


"""class Application(BaseModel)
app date
loan purpose
loan type
credit score
fthb
preapproval date
preapproval rate
condo preapprovals = {mf: purch price, ... }
sfr preapproval = {ins 150: x, ins 250: x}
lock date
lock expiration
close date
close purchase price
close loan amount
close property address
close maintenance fee
close insurance
close other monthly fees
close rate"""