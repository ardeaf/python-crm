from peewee import Model, CharField, DateField, BooleanField, IntegerField, SqliteDatabase, ForeignKeyField, \
    DecimalField, TextField
import os


class BaseModel(Model):
    class Meta:
        db_name = "test_crm.db"

        db_path = os.path.join(os.path.expanduser("~"), db_name)
        db = SqliteDatabase(db_path)

        database = db


class Person(BaseModel):
    last_name = CharField()
    first_name = CharField()
    cellphone = CharField()
    email = CharField()
    birthdate = DateField()
    address_current = CharField()
    address_mailing = CharField()
    is_realtor = BooleanField()


class Dependent(BaseModel):
    parent = ForeignKeyField(Person, related_name='dependents')
    first_name = CharField()
    last_name = CharField()
    birthdate = DateField()


class Application(BaseModel):
    person = ForeignKeyField(Person, related_name='applications')
    date = DateField()
    loan_purpose = CharField()
    loan_type = CharField()
    credit_score = CharField()
    fthb = BooleanField()
    locked = BooleanField
    lock_date = DateField()
    lock_rate = DecimalField()
    lock_expiration = DateField()
    closed = BooleanField()
    close_date = DateField()
    purchase_price = IntegerField()
    loan_amount = IntegerField()
    property_address = CharField()
    maintenance_fee = IntegerField()
    insurance = IntegerField()
    other_fees = IntegerField()


class Preapproval(BaseModel):
    person = ForeignKeyField(Person, related_name="preapprovals")
    maintenance_fee = IntegerField()
    insurance = IntegerField()
    taxes = IntegerField()
    date = DateField()
    rate = DecimalField()
    purchase_price = IntegerField()
    loan_amount = IntegerField()
    credit_score = IntegerField()
    income = IntegerField()
    closing_costs = IntegerField()
    cash_to_close = IntegerField()
    reserves = IntegerField()
    dti = DecimalField()


class Job(BaseModel):
    person = ForeignKeyField(Person, related_name="jobs")
    application = ForeignKeyField(Application, related_name="application_jobs")
    employer = CharField()
    position = CharField()
    monthly_income = IntegerField()


class Asset(BaseModel):
    person = ForeignKeyField(Person, related_name="assets")
    application = ForeignKeyField(Application, related_name="application_assets")
    source = CharField()
    liquid = BooleanField()
    amount = IntegerField()


class Rental(BaseModel):
    person = ForeignKeyField(Person, related_name="rentals")
    application = ForeignKeyField(Application, related_name="application_rentals")
    address = CharField()
    monthly_revenue = IntegerField()
    monthly_expenses = IntegerField()
    pitia = IntegerField()


class Referral(BaseModel):
    referrer = ForeignKeyField(Person, related_name="referrals")
    referral = ForeignKeyField(Person, related_name="referrer")


class Communication(BaseModel):
    person = ForeignKeyField(Person, related_name="communications")
    date = DateField()
    note = TextField()
