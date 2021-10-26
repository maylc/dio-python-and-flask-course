from models import People


def insert_person():
    person = People(name='John', age=30)
    person.save()
    print(person)


def list_people():
    people = People.query.all()
    for i in people:
        print('{} - Age: {}'.format(i.name, i.age))


def search_person():
    person = People.query.filter_by(name='John').first()
    print(person)


def update_person():
    person = People.query.filter_by(name='John').first()
    person.age = 32
    person.save()


def delete_person():
    person = People.query.filter_by(name='John').first()
    person.delete()


if __name__ == '__main__':
    # insert_person()
    # update_person()
    # delete_person()
    list_people()
