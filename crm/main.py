import os, cmd
import crm.const as const
from crm.models import Person, Dependent, Application, Preapproval, Job, Asset, Rental, Referral, Communication
from crm.models import db
import peewee
from datetime import date



class CmdShell(cmd.Cmd):
    intro = const.intro
    prompt = const.prompt
    db = db

    def do_print_db_path(self, arg):
        "Prints path to connected database."
        print(db.database)

    def do_exit(self, arg):
        "Exits prompt."
        print(const.outtro)
        return True

# Inserts a object into the db.
def insert(db, object):
    with db.atomic() as txn:
        object.save()


# Removes object from db.
def remove(db, object):
    with db.atomic() as txn:
        return object.delete_instance()


def main():
    # Points to the database our models will be using to instantiate themselves.
    db_name = "crm.db"
    db_path = os.path.join(os.path.expanduser("~"), db_name)
    db.init(db_path)

    CmdShell().cmdloop()


if __name__ == "__main__":
    main()
