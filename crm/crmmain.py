from peewee import Model, CharField, DateField, BooleanField, IntegerField, SqliteDatabase
import os


db_path = os.path.join(os.path.expanduser("~"), "crm.db")
db = SqliteDatabase(db_path)


class Person(Model):
    LastName = CharField()
    FirstName = CharField()
    CellPhone = CharField()
    Birthdate = DateField()
    AddressCurrent = CharField()
    AddressMailing = CharField()

    class Meta:
        database = db
