from crm.crmmain import Person, Dependent, Application, Preapproval, Job, Asset, Rental
from tests.fixtures import sample_person, db, sample_preapproval, sample_application, sample_dependent, sample_job, sample_asset, sample_rental

def test_query_matches_saved_person(sample_person, db):
    db.create_table(Person, True)
    sample_person.save()
    assert sample_person.first_name == Person.get(Person.last_name == sample_person.last_name).first_name


def test_dependent_parent_equals_person_from_query(sample_dependent, sample_person, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Dependent, True)
    sample_dependent.save()

    assert sample_dependent.parent == Person.get(Person.id == 1)  # id is 1 since we added only 1 person


def test_create_application_by_querying_name(sample_person, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Application, True)
    sample_application.save()

    assert sample_application == Person.get(Person.id == 1).applications.get()


def test_create_preapproval_by_querying_name(sample_person, sample_preapproval, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Preapproval, True)
    sample_preapproval.person = Person.get(Person.first_name == sample_person.first_name,
                                           Person.last_name == sample_person.last_name)
    sample_preapproval.save()

    assert sample_preapproval == Person.get(Person.id == 1).preapprovals.get()


def test_job_creation_by_querying_name(sample_person, sample_job, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Application, True)
    sample_application.save()

    db.create_table(Job, True)
    sample_job.person = Person.get(Person.first_name == sample_person.first_name,
                                   Person.last_name == sample_person.last_name)
    sample_job.save()

    assert sample_job == Person.get(Person.id == 1).jobs.get()


def test_asset_creation_by_querying_name(sample_person, sample_application, sample_asset, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Application, True)
    sample_application.save()

    db.create_table(Asset, True)
    sample_asset.person = Person.get(Person.first_name == sample_person.first_name,
                                     Person.last_name == sample_person.last_name)
    sample_asset.save()

    assert sample_asset == Person.get(Person.id == 1).assets.get()

def test_rental_creation_by_querying_name(sample_person, sample_application, sample_rental, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Application, True)
    sample_application.save()

    db.create_table(Rental, True)
    sample_rental.person = Person.get(Person.first_name == sample_person.first_name,
                                      Person.last_name == sample_person.last_name)
    sample_rental.save()

    assert sample_rental == Person.get(Person.id == 1).rentals.get()

def test_referral_creation_by_querying_name(sample_person, sample_application, sample_rental, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Referrals, True)
    sample_referral.person = Person.get(Person.first_name == sample_person.first_name,
                                        Person.last_name == sample_person.last_name)
    sample_referral.save()

    assert sample_referral == Person.get(Person.id == 1).referrals.get()


