from filestart import *


def addUser(connection):
    with connection.cursor() as cursor:
        add_user = f"insert into `users` (name, surname, login, parol) values ('{name}', '{surname}', '{login}','{parol}')"
        cursor.execute(add_user)
        connection.commit()


def addFriend(connection):
    with connection.cursor() as cursor:
        add_friend = f"insert into `friends` (name, surname, login) values ('{name}', '{surname}', '{login}')"
        cursor.execute(add_friend)
        connection.commit()


def addPost(connection):
    with connection.cursor as cursor:
        add_post = f"insert into `posts` (postName, Login) values ('{postName}', '{Login}')"
        cursor.execute(add_post)
        connection.commit()


def delUser(connection):
    with connection.cursor() as cursor:
        del_user = f"delete from '{table}' where "