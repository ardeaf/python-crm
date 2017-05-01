from crm.crmmain import Person, Dependent, Application, Preapproval
from tests.fixtures import sample_person, db, sample_preapproval, sample_application, sample_dependent

def test_query_matches_saved_person(sample_person, db):
    db.create_table(Person, True)
    sample_person.save()
    assert sample_person.FirstName == Person.get(Person.LastName == sample_person.LastName).FirstName


def test_dependent_parent_equals_person_from_query(sample_dependent, sample_person, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Dependent, True)
    sample_dependent.save()

    assert sample_dependent.Parent == Person.get(Person.id == 1)  # id is 1 since we added only 1 person


def test_application_applicant_equals_person_from_query(sample_person, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    db.create_table(Application, True)
    sample_application.save()

    assert sample_application.Applicant == Person.get(Person.id == 1)  # id is 1 since we added only 1 person


def test_create_application_by_querying_name(sample_person, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    first_name = Person.get(Person.FirstName == sample_person.FirstName).FirstName
    last_name = Person.get(Person.LastName == sample_person.LastName).LastName

    db.create_table(Application, True)
    sample_application.Applicant == Person.get(Person.FirstName == first_name, Person.LastName == last_name)
    sample_application.save()

    assert sample_application.Applicant == Person.get(Person.id == 1)


def test_create_preapproval_by_querying_name(sample_person, sample_preapproval, db):
    db.create_table(Person, True)
    sample_person.save()

    first_name = Person.get(Person.FirstName == sample_person.FirstName).FirstName
    last_name = Person.get(Person.LastName == sample_person.LastName).LastName

    db.create_table(Preapproval, True)
    sample_preapproval.Person == Person.get(Person.FirstName == first_name, Person.LastName == last_name)
    sample_preapproval.save()

    assert sample_preapproval.Person == Person.get(Person.id == 1)


def test_employer_creation_by_querying_name(sample_person, sample_application, db):
    db.create_table(Person, True)
    sample_person.save()

    first_name = Person.get(Person.FirstName == sample_person.FirstName).FirstName
    last_name = Person.get(Person.LastName == sample_person.LastName).LastName

    db.create_table(Employer, True)
    sample_employer.Person == Person.get(Person.FirstName == first_name, Person.LastName == last_name)
    sample_employer.save()

    assert sample_employer.Person == Person.get(Person.id == 1)
