import pymysql
from easygui import *
from login import *




def addUser(connection):
    with connection.cursor() as cursor:
        addname = multenterbox('Додайте юзера:','Table',['name','surname','login','parol'])
        add_user = f"INSERT INTO socialnetwork.users (Name,Surname,Login,Parol) VALUES ('{addname[0]}', '{addname[1]}','{addname[2]}','{addname[3]}')"
        cursor.execute(add_user)
        connection.commit()

    return msgbox(f"{addname[0]} доданий")


def addFriend(connection):
    with connection.cursor() as cursor:
        nameFriend = multenterbox("Вкажіть контакти друга для додавання:",'friend',['Name','Surname'])
        add_friend = f"insert into `friends` (name, surname, login) values ('{nameFriend[0]}', '{nameFriend[1]}', '{table[0]}')"
        cursor.execute(add_friend)
        connection.commit()

    return msgbox('Друг доданий')


def addPost(connection):
    with connection.cursor() as cursor:
        namePost = multenterbox("Вкажіть назву поста та ваш логін", "Post", ["name Post", "login"])
        add_post = f"insert into `posts` (postName, Login) values ('{namePost[0]}', '{namePost[1]}')"
        cursor.execute(add_post)
        connection.commit()

    return msgbox('Пост додано')


def editInfoFromUser(connection):
    with connection.cursor() as cursor:
        choice = buttonbox('Оберіть, що хочете оновити:', 'NewInfo', ['Name','Surname','login','Parol'])
        newInfo = multenterbox(f"Впишіть нові дані для {choice} та логін свого облікового запису", 'Table', [choice, "Login"])
        edit_user = f"update `users` set {choice} = '{newInfo[0]}' where login ='{newInfo[1]}'"
        cursor.execute(edit_user)
        connection.commit()

    return msgbox('Зміни прийняті')


def findUser(connection):
    with connection.cursor() as cursor:
        find = enterbox("Вкажіть прізвище юзера для пошуку:")
        find_user = f"select surname from `users` where surname = '{find}'"
        cursor.execute(find_user)
        result = cursor.fetchall()
    return msgbox(result)


def selectAllFromUser(connection):
    with connection.cursor() as cursor:
        name = enterbox('Вкажіть Login користувача для пошуку:')
        select_all_from_user = f"select * from `users` where Login = '{name}'"
        cursor.execute(select_all_from_user)
        result = cursor.fetchall()
    return msgbox(result)

def delUser(connection):
    with connection.cursor() as cursor:
        friendName = enterbox('Вкажіть name друга,якого ви хочете видалити:')
        del_user = f"delete from friends where name = '{friendName}' and login = (SELECT Login FROM users)"
        cursor.execute(del_user)
        connection.commit()

    return msgbox('Користувач видалений')

def allFriend(connection):
    with connection.cursor() as cursor:
        select_all_friend_user = f"select * from `friends` where login = '{table[0]}'"
        cursor.execute(select_all_friend_user)
        connection.commit()
    return msgbox(select_all_friend_user)

def allPosts(connection):
    with connection.cursor() as cursor:
        select_all_post = f"select * from `posts` where login = '{table[0]}'"
        cursor.execute(select_all_post)
        connection.commit()
    return msgbox(select_all_post)