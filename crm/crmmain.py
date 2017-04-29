from peewee import Model, CharField, DateField, BooleanField, IntegerField, SqliteDatabase
import os

if __name__ == "__main__":
    db_name = "crm.db"
else:
    db_name = "test_crm.db"

db_path = os.path.join(os.path.expanduser("~"), db_name)
db = SqliteDatabase(db_path)

class Person(Model):
    LastName = CharField()
    FirstName = CharField()
    CellPhone = CharField()
    Email = CharField()
    Birthdate = DateField()
    AddressCurrent = CharField()
    AddressMailing = CharField()

    class Meta:
        database = db

