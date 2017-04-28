import os
import peewee
from datetime import date


db_path = os.path.join(os.path.expanduser("~"), "crm.db")
db = peewee.SqliteDatabase(db_path)

def test_add_person():
    lastname = "Lothbrok"
    firstname = "Ardeaf"
    cellphone = "123-456-7890"
    dob = date(1995,10,1)
