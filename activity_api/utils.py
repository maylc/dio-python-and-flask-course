from models import People, Users


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


def insert_user(login, password):
    user = Users(login=login, password=password)
    user.save()


def list_users():
    users = Users.query.all()
    print(users)


if __name__ == '__main__':
    # insert_user("may", "1234")
    # insert_user("felix", "5678")
    # insert_person()
    # update_person()
    # delete_person()
    list_users()
    list_people()
