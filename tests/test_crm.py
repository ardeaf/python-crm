from crm.crmmain import Person, Dependent, Application, Preapproval, Job
from tests.fixtures import sample_person, db, sample_preapproval, sample_application, sample_dependent, sample_job

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


def test_application_applicant_equals_person_from_query(sample_person, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Application, True)
    sample_application.save()

    assert sample_application.person == Person.get(Person.id == 1)  # id is 1 since we added only 1 person


def test_create_application_by_querying_name(sample_person, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    first_name = Person.get(Person.first_name == sample_person.first_name).first_name
    last_name = Person.get(Person.last_name == sample_person.last_name).last_name

    db.create_table(Application, True)
    sample_application.person == Person.get(Person.first_name == first_name, Person.last_name == last_name)
    sample_application.save()

    assert sample_application.person == Person.get(Person.id == 1)


def test_create_preapproval_by_querying_name(sample_person, sample_preapproval, db):
    db.create_table(Person, True)
    sample_person.save()

    first_name = Person.get(Person.first_name == sample_person.first_name).first_name
    last_name = Person.get(Person.last_name == sample_person.last_name).last_name

    db.create_table(Preapproval, True)
    sample_preapproval.person == Person.get(Person.first_name == first_name, Person.last_name == last_name)
    sample_preapproval.save()

    assert sample_preapproval.person == Person.get(Person.id == 1)


def test_job_creation_by_querying_name(sample_person, sample_application, sample_job, db):
    db.create_table(Person, True)
    sample_person.save()

    first_name = Person.get(Person.first_name == sample_person.first_name).first_name
    last_name = Person.get(Person.last_name == sample_person.last_name).last_name

    db.create_table(Application, True)
    sample_application.save()

    db.create_table(Job, True)
    sample_job.Application = Person.get((Person.first_name == sample_person.first_name) &
                                        (Person.last_name == sample_person.last_name)).applications
    sample_job.save()

    assert sample_job.person == Person.get(Person.id == 1)
