from crm.models import Person
from tests.fixtures import sample_person_one, sample_preapproval, sample_application, sample_dependent, sample_job, \
    sample_asset, sample_rental, sample_person_two, sample_referral, sample_communication, db_fixture


def test_query_matches_saved_person(sample_person_one):
    sample_person_one.save()
    assert sample_person_one.first_name == Person.get(Person.last_name == sample_person_one.last_name).first_name


def test_dependent_parent_equals_person_from_query(sample_dependent, sample_person_one):
    sample_person_one.save()
    sample_dependent.save()
    assert sample_dependent.parent == Person.get(Person.last_name == sample_person_one.last_name)


def test_create_application_by_querying_name(sample_person_one, sample_application):
    sample_person_one.save()
    sample_application.save()

    assert sample_application == Person.get(Person.last_name == sample_person_one.last_name).applications.get()


def test_create_preapproval_by_querying_name(sample_person_one, sample_preapproval):
    sample_person_one.save()
    sample_preapproval.person = Person.get(Person.first_name == sample_person_one.first_name,
                                           Person.last_name == sample_person_one.last_name)
    sample_preapproval.save()

    assert sample_preapproval == Person.get(Person.last_name == sample_person_one.last_name).preapprovals.get()


def test_job_creation_by_querying_name(sample_person_one, sample_job, sample_application):
    sample_person_one.save()
    sample_application.save()
    sample_job.person = Person.get(Person.first_name == sample_person_one.first_name,
                                   Person.last_name == sample_person_one.last_name)
    sample_job.save()

    assert sample_job == Person.get(Person.last_name == sample_person_one.last_name).jobs.get()


def test_asset_creation_by_querying_name(sample_person_one, sample_application, sample_asset):
    sample_person_one.save()
    sample_application.save()
    sample_asset.person = Person.get(Person.first_name == sample_person_one.first_name,
                                     Person.last_name == sample_person_one.last_name)
    sample_asset.save()

    assert sample_asset == Person.get(Person.last_name == sample_person_one.last_name).assets.get()


def test_rental_creation_by_querying_name(sample_person_one, sample_application, sample_rental):
    sample_person_one.save()
    sample_application.save()
    sample_rental.person = Person.get(Person.first_name == sample_person_one.first_name,
                                      Person.last_name == sample_person_one.last_name)
    sample_rental.save()

    assert sample_rental == Person.get(Person.last_name == sample_person_one.last_name).rentals.get()


def test_referral_creation_by_querying_referrer(sample_person_one, sample_person_two, sample_referral):
    sample_person_one.save()
    sample_person_two.save()
    sample_referral.referrer = Person.get(Person.first_name == sample_person_one.first_name,
                                          Person.last_name == sample_person_one.last_name)
    sample_referral.referral = Person.get(Person.first_name == sample_person_two.first_name,
                                          Person.last_name == sample_person_two.last_name)

    sample_referral.save()

    assert sample_referral == Person.get(Person.last_name == sample_person_one.last_name).referrals.get()


def test_communication_by_querying_person(sample_person_one, sample_communication):
    sample_person_one.save()
    sample_communication.Person = Person.get(Person.first_name == sample_person_one.first_name,
                                             Person.last_name == sample_person_one.last_name)

    sample_communication.save()

    assert sample_communication == Person.get(Person.last_name == sample_person_one.last_name).communications.get()
