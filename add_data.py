import pymysql
from easygui import *
from login import *
# from main import *

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
                break
            else:
                msgbox(f"Краш програми логін: {addname[2]} вже зареестрований", image='giphy.gif')
                break
    return "done"


def addFriend(connection, log_now):
    with connection.cursor() as cursor:
        nameFriend = enterbox("Вкажіть login друга для додавання:", 'friend',image='j.gif')
        user_data = f"select login,name,surname from `users` where login = {nameFriend}"
        cursor.execute(user_data)
        result = cursor.fetchall()
        surnList = []
        nameList = []
        loginList = []
        for el in result:
            surnList.append(el['surname'])
            nameList.append(el['name'])
            loginList.append(el['login'])
            add_friend = f"insert into `friends` (name, surname, login,FriendLogin) values ('{nameList}', '{surnList}','{log_now}','{nameFriend}')"
            cursor.execute(add_friend)
            connection.commit()
            msgbox(f'Друг під ніком {nameFriend} - доданий', image='good.gif')
        else:
            msgbox(f"Такого користувача не знайдено", image='giphy.gif')
    return 'done'


def addPost(connection, log_now):
    with connection.cursor() as cursor:
        namePost = multenterbox("Вкажіть назву поста", "Post", ["name Post"])
        post = enterbox("Напишіть свій пост:", image='helper.gif')
        add_post = f"insert into `posts` (postName,post, Login) values ('{namePost[0]}','{post}', '{log_now}')"
        cursor.execute(add_post)
        connection.commit()
        msgbox('Пост додано', image='good.gif')
    return 'done'


def editInfoFromUser(connection, log_now):
    with connection.cursor() as cursor:
        choice = buttonbox('Оберіть, що хочете оновити:', 'NewInfo', ['Name', 'Surname', 'Parol'], 'set.gif')
        newInfo = multenterbox(f"Впишіть нові дані для {choice} свого облікового запису", 'Table',
                               [choice])
        edit_user = f"update `users` set {choice} = '{newInfo[0]}' where login ='{log_now}'"
        cursor.execute(edit_user)
        connection.commit()
        msgbox('Зміни прийняті', image='good.gif')
    return 'done'


def findUser(connection):
    with connection.cursor() as cursor:
        find = enterbox("Вкажіть login юзера для пошуку:", image='about.gif')
        user_data = f"select * from socialnetwork.users"
        cursor.execute(user_data)
        result = cursor.fetchall()
        SurnList = []
        for el in result:
            SurnList.append(el['login'])
        if find in SurnList:
            find_user = f"select * from `users` where login = '{find}'"
            cursor.execute(find_user)
            result = cursor.fetchall()
            for var in result:
                if find == var['login']:
                    var = f"{result[0]['Name']} {result[0]['Surname']}, Login: {result[0]['Login']}"
                else:
                    var = "No"
            msgbox(var, image='programer.gif')
        else:
            msgbox(f"Користувача з таким прізвищем нема у базі", image='giphy.gif')
    return 'done'


def selectAllFromUser(connection, log_now):
    with connection.cursor() as cursor:
        select_all_from_user = f"select * from `users` where Login = '{log_now}'"
        cursor.execute(select_all_from_user)
        result = cursor.fetchall()
        msgbox(
            f"{result[0]['Name']} {result[0]['Surname']}, Login: {result[0]['Login']}, Password: {result[0]['Parol']}",
            image='programer.gif')
    return 'done'


def delFriend(connection, log_now):
    with connection.cursor() as cursor:
        friendName = enterbox('Вкажіть login друга,якого ви хочете видалити:', 'Add',image='77.gif')
        user_data = f"select FriendLogin from `friends` WHERE Login = '{log_now}'"
        cursor.execute(user_data)
        result = cursor.fetchall()
        surnameList = []
        for el in result:
            surnameList.append(el['FriendLogin'])
        if friendName in surnameList:
            del_user = f"delete from `friends` where FriendLogin = '{friendName}' and login = '{log_now}'"
            cursor.execute(del_user)
            connection.commit()
            msgbox('Користувач видалений', image='good.gif')
        else:
            msgbox(f"Такого користувача не знайдено", image='giphy.gif')
    return 'done'


def delUser(connection, log_now):
    choice2 = enterbox("Впишіть логін для видалення юзера:",image='200w.gif')
    with connection.cursor() as cursor:
        del_user = f"delete from `users` where Login = '{choice2}'"
        print('1')
        cursor.execute(del_user)
        print('2')
        connection.commit()
        print('3')
        msgbox('Користувач видалений', image='good.gif')
        choice = "Відміна"
    return "done"


def allFriend(connection, log_now):
    with connection.cursor() as cursor:
        select_all_friend_user = f"select * from `friends` where login = '{log_now}'"
        cursor.execute(select_all_friend_user)
        friend = f"Друзі користувача {log_now}:\n"
        result = cursor.fetchall()
        for var in result:
            friend = friend + f"{var['Name']} {var['Surname']}\n"
        msgbox(friend, image='programer.gif')
    return 'done'


def allPosts(connection, log_now):
    with connection.cursor() as cursor:
        select_all_post = f"select postName,Post from `posts` where login = '{log_now}'"
        cursor.execute(select_all_post)
        result = cursor.fetchall()
        txt1 = f"Публікації {log_now}:\n\n"
        for i in result:
            txt1 = txt1 + f"{i['postName']} \n\n{i['Post']}\n\n"
        msgbox(txt1, image='2.gif')
    return 'done'


def delPost(connection, log_now):
    with connection.cursor() as cursor:
        delPost = multenterbox('Вкажіть Назву поста,який ви хочете видалити:', 'DELETE',
                               ['Name'])
        user_data = f"select postName from `posts`"
        cursor.execute(user_data)
        result = cursor.fetchall()
        loginList = []
        for el in result:
            loginList.append(el['postName'])
        if delPost[0] in loginList:
            del_Post = f"delete from `posts` where login = '{log_now}' and postName = '{delPost[0]}'"
            cursor.execute(del_Post)
            connection.commit()
            msgbox('Пост видалений', image='good.gif')
        else:
            msgbox(f"{delPost[0]} нема у базі", image='giphy.gif')
    return 'done'
