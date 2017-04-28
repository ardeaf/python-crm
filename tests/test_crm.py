import os
import peewee
from datetime import date

db_path = os.path.join(os.path.expanduser("~"), "crm.db")
db = peewee.SqliteDatabase(db_path)


def test_add_person():
    last_name = "Lothbrok"
    first_name = "Ardeaf"
    cell_phone = "1234567890"
    dob = date(1995, 10, 1)
    current_address = "700 Google Dr. #21B, San Mateo, CA, 98102"
    mailing_address = "P.O. Box 3, San Mateo, CA, 98102"

    test_entry = Person(LastName=last_name,
                        FirstName=first_name,
                        CellPhone=cell_phone,
                        Birthdate=dob,
                        AddressCurrent=current_address,
                        AddressMailing=mailing_address)

    