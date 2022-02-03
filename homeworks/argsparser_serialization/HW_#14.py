import json
import argparse


def create_file():
    file = open("users.json", 'w')
    file.write(json.dumps([]))
    file.close()
    return open("users.json", 'r')


def create_user(users):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="username")
    parser.add_argument("-e", "--email", help="email")
    parser.add_argument("-s", "--status", help="status")
    args = parser.parse_args()

    try:
        users['username'] = args.username
        users['email'] = args.email
        users['status'] = args.status
    except IndexError:
        raise Exception('error')


def check_user_exists(users_data, user):
    for users in users_data:
        if user["username"] == users["username"] or user["email"] == users["email"]:
            return True
    return False


def add_user(user):
    try:
        file = open('users.json', 'r')
    except FileNotFoundError:
        file = create_file()

    try:
        users_data = json.loads(file.read())
    except ValueError:
        with open('users.json', "w") as file:
            file.write(json.dumps([]))
        users_data = []

    file.close()

    if not check_user_exists(users_data, user):
        users_data.append(user)
        with open('users.json', 'w') as file:
            file.write(json.dumps(users_data, indent=4, sort_keys=True))
    else:
        raise 'A user with this name or email is present'


if __name__ == "__main__":
    user = {}
    create_user(user)
    add_user(user)
