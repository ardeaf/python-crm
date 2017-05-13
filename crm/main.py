import os
from crm.models import Person, Dependent, Application, Preapproval, Job, Asset, Rental, Referral, Communication
from crm.models import db
import cmd


def insert(db):
    # Inserts a specified model into the db.
    pass


def remove():
    # Deletes a specified model into the db.
    pass


def main():
    # Points to the database our models will be using to instantiate themselves.
    db_name = "crm.db"
    db_path = os.path.join(os.path.expanduser("~"), db_name)
    db.init(db_path)

if __name__ == "__main__":
    main()
