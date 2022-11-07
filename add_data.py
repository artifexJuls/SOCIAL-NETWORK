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
    with connection.cursor() as cursor:
        add_post = f"insert into `posts` (postName, Login) values ('{postName}', '{Login}')"
        cursor.execute(add_post)
        connection.commit()


def editInfoFromUser(connection):
    with connection.cursor() as cursor:
        edit_user = f"update `users` set surname = '{surname}'"
        cursor.execute(edit_user)
        connection.commit()

def findUser(connction):
    find_user = f"select surname from `users` where surname = '{surname}'"
    cursor.execute(find_user)
    connction.commit()

def selectAllFromUser(connection):
    select_all_from_user = f"select * from `users` where name = '{name}'"
    cursor.execute(select_all_from_user)
    connection.commit()


def delUser(connection):
    with connection.cursor() as cursor:
        del_user = f"delete from '{table}' where "
        cursor.execute(del_user)
        connection.commit()