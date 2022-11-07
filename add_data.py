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
        nameFriend = multenterbox("Вкажіть контакти друга для додавання та свій логін авторизіції:",'friend',['Name','Surname', 'Login'])
        add_friend = f"insert into `friends` (name, surname, login) values ('{nameFriend[0]}', '{nameFriend[1]}', '{nameFriend[2]}')"
        cursor.execute(add_friend)
        connection.commit()

    return msgbox(f'Друг {nameFriend[1]} доданий')


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
        find_user = f"select * from `users` where surname = '{find}'"
        cursor.execute(find_user)
        result = cursor.fetchall()
        for var in result:
            if find == var['Surname']:
                var = f"{result[0]['Name']} {result[0]['Surname']}, Login: {result[0]['Login']}"
            else:
                var = "No"
    return msgbox(var)

def selectAllFromUser(connection):
    with connection.cursor() as cursor:
        name = enterbox('Вкажіть Login користувача для пошуку:')
        select_all_from_user = f"select * from `users` where Login = '{name}'"
        cursor.execute(select_all_from_user)
        result = cursor.fetchall()
        var = msgbox(f"{result[0]['Name']} {result[0]['Surname']}, Login: {result[0]['Login']}, Password: {result[0]['Parol']}")
    return msgbox(var)

def delUser(connection):
    with connection.cursor() as cursor:
        friendName = multenterbox('Вкажіть name друга,якого ви хочете видалити та свій логін авторизації:', 'Add', ['Name', 'Login'])
        del_user = f"delete from friends where name = '{friendName[0]}' and login = '{friendName[1]}'"
        cursor.execute(del_user)
        connection.commit()

    return msgbox('Користувач видалений')

def allFriend(connection):
    with connection.cursor() as cursor:
        choice_pass = enterbox("Введіть логін авторизації")
        select_all_friend_user = f"select * from `friends` where login = '{choice_pass}'"
        cursor.execute(select_all_friend_user)
        friend = "Friend Wazan:\n"
        result = cursor.fetchall()
        for var in result:
            friend = friend + f"{var['Name']} {var['Surname']}\n"
    return msgbox(friend)

def allPosts(connection):
    with connection.cursor() as cursor:
        var = enterbox("Введіть свій логін:")
        select_all_post = f"select postName from `posts` where login = '{var}'"
        cursor.execute(select_all_post)
        result = cursor.fetchall()
        txt1 = f"Публікації {var}:\n\n"
        for i in result:
            txt1 = txt1 + f"{i['postName']} \n\n"
    return msgbox(txt1)