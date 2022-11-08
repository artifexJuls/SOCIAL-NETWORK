import pymysql
from easygui import *
from login import *


def alllogin(connection):
    with connection.cursor() as cursor:
        sel = "select Login from socialnetwork.users"
        cursor.execute(sel)
        result = cursor.fetchall()
        allLog = []
        for i in result:
            allLog.append(i['Login'])
    return allLog

def addUser(connection):
    with connection.cursor() as cursor:
        addname = multenterbox('Реєстрація нового юзера:', 'Table', ['Name', 'Surname', 'Login', 'Parol'])
        user_data = f"select login from `users`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        for el in result:
            if addname[2] != el['login']:
                add_user = f"INSERT INTO socialnetwork.users (Name,Surname,Login,Parol) VALUES ('{addname[0]}', '{addname[1]}','{addname[2]}','{addname[3]}')"
                cursor.execute(add_user)
                connection.commit()
                msgbox(f"{addname[0]} зареєстрований", image='good.gif')
            else:
                msgbox(f"Краш програми логін: {addname[2]} вже зареестрований", image='giphy.gif')
    return "done"


def addFriend(connection):
    with connection.cursor() as cursor:
        nameFriend = multenterbox("Вкажіть контакти друга для додавання та свій логін авторизації:", 'friend',
                                  ['Name', 'Surname','Login'])
        user_data = f"select login from `friends`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if nameFriend[2] in loginList:
            add_friend = f"insert into `friends` (name, surname, login) values ('{nameFriend[0]}', '{nameFriend[1]}', '{nameFriend[2]}')"
            cursor.execute(add_friend)
            connection.commit()
            msgbox(f'Друг {nameFriend[1]} доданий', image='good.gif')
        else:
            msgbox(f"Краш програми логін: {nameFriend[2]} нема у базі", image='giphy.gif')
    return 'done'


def addPost(connection):
    with connection.cursor() as cursor:
        namePost = multenterbox("Вкажіть назву поста та ваш логін", "Post", ["name Post", "login"])
        user_data = f"select login from `posts`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if namePost[1] in loginList:
            post = enterbox("Напишіть свій пост:", image='helper.gif')
            add_post = f"insert into `posts` (postName,post, Login) values ('{namePost[0]}','{post}', '{namePost[1]}')"
            cursor.execute(add_post)
            connection.commit()
            msgbox('Пост додано', image='good.gif')
        else:
            msgbox(f"Краш програми логін: {namePost[1]} нема у базі", image='giphy.gif')
    return 'done'


def editInfoFromUser(connection):
    with connection.cursor() as cursor:
        choice = buttonbox('Оберіть, що хочете оновити:', 'NewInfo', ['Name', 'Surname', 'login', 'Parol'], 'set.gif')
        newInfo = multenterbox(f"Впишіть нові дані для {choice} та логін свого облікового запису", 'Table',
                               [choice, "Login"])
        user_data = f"select login from `users`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if newInfo[1] in loginList:
            edit_user = f"update `users` set {choice} = '{newInfo[0]}' where login ='{newInfo[1]}'"
            cursor.execute(edit_user)
            connection.commit()
            msgbox('Зміни прийняті', image='good.gif')
        else:
            msgbox(f"Краш програми логін: {newInfo[1]} нема у базі", image='giphy.gif')
    return 'done'


def findUser(connection):
    with connection.cursor() as cursor:
        find = enterbox("Вкажіть прізвище юзера для пошуку:", image='1.gif')
        user_data = f"select surname from `users`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        SurnList = []
        for el in result:
            SurnList.append(el['surname'])
        if find in SurnList:
            find_user = f"select * from `users` where surname = '{find}'"
            cursor.execute(find_user)
            result = cursor.fetchall()
            for var in result:
                if find == var['Surname']:
                    var = f"{result[0]['Name']} {result[0]['Surname']}, Login: {result[0]['Login']}"
                else:
                    var = "No"
            msgbox(var, image='programer.gif')
        else:
            msgbox(f"Краш програми користувача з таким прізвишем нема у базі", image='giphy.gif')
    return 'done'


def selectAllFromUser(connection):
    with connection.cursor() as cursor:
        name = enterbox('Вкажіть свій Login :', image='helper.gif')
        user_data = f"select login from `users`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if name in loginList:
            select_all_from_user = f"select * from `users` where Login = '{name}'"
            cursor.execute(select_all_from_user)
            result = cursor.fetchall()
            msgbox(
                f"{result[0]['Name']} {result[0]['Surname']}, Login: {result[0]['Login']}, Password: {result[0]['Parol']}",
                image='programer.gif')
        else:
            msgbox(f"Краш програми логін: {name} нема у базі", image='giphy.gif')
    return 'done'


def delFriend(connection):
    with connection.cursor() as cursor:
        friendName = multenterbox('Вкажіть name друга,якого ви хочете видалити та свій логін авторизації:', 'Add',
                                  ['Name','Surname', 'Login'])
        user_data = f"select login from `friends`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if friendName[0] and friendName[1] and friendName[2] in loginList:
            del_user = f"delete from `friends` where name = '{friendName[0]}' and surname = '{friendName[1]}' and login = '{friendName[2]}'"
            cursor.execute(del_user)
            connection.commit()
            msgbox('Користувач видалений', image='good.gif')
        else:
            msgbox(f"Краш програми логін: {friendName[2]} нема у базі", image='giphy.gif')
    return 'done'


def delUser(connection):
    with connection.cursor() as cursor:
        delName = enterbox('Вкажіть свій логін для видалення:', 'DELETE', )
        user_data = f"select login from `users`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if delName in loginList:
            del_user = f"delete from `users` where login = '{delName}'"
            cursor.execute(del_user)
            connection.commit()
            msgbox('Користувач видалений', image='good.gif')
        else:
            msgbox(f"Краш програми логін: {delName} нема у базі", image='giphy.gif')
    return 'done'


def allFriend(connection):
    with connection.cursor() as cursor:
        choice_pass = enterbox("Введіть логін авторизації", image='1.gif')
        user_data = f"select login from `friends`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if choice_pass in loginList:
            select_all_friend_user = f"select * from `friends` where login = '{choice_pass}'"
            cursor.execute(select_all_friend_user)
            friend = f"Друзі користувача {choice_pass}:\n"
            result = cursor.fetchall()
            for var in result:
                friend = friend + f"{var['Name']} {var['Surname']}\n"
                msgbox(friend, image='programer.gif')
        else:
            msgbox(f"Краш програми логін: {choice_pass} нема у базі", image='giphy.gif')
    return 'done'


def allPosts(connection):
    with connection.cursor() as cursor:
        var = enterbox("Введіть свій логін:", image='wifi.gif')
        user_data = f"select login from `post`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if var in loginList:
            select_all_post = f"select postName,Post from `posts` where login = '{var}'"
            cursor.execute(select_all_post)
            result = cursor.fetchall()
            txt1 = f"Публікації {var}:\n\n"
            for i in result:
                txt1 = txt1 + f"{i['postName']} \n\n{i['Post']}"
                msgbox(txt1, image='2.gif')
        else:
            msgbox(f"Краш програми логін: {var} нема у базі", image='giphy.gif')
    return 'done'


def delPost(connection):
    with connection.cursor() as cursor:
        delPost = multenterbox('Вкажіть Назву поста,який ви хочете видалити та свій логін авторизації:', 'DELETE',
                               ['Name', 'Login'])
        user_data = f"select login from `posts`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['login'])
        if delPost[1] in loginList:
            del_Post = f"delete from `posts` where login = '{delPost[1]}' and postName = '{delPost[0]}'"
            cursor.execute(del_Post)
            connection.commit()
            msgbox('Пост видалений', image='good.gif')
        else:
            msgbox(f"Краш програми логін: {delPost[1]} нема у базі", image='giphy.gif')
    return 'done'

