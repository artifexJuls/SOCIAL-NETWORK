import pymysql
from easygui import *
from login import  *
from add_data import  *

# userInter = enterbox("Enter your name for Database", "Password")
# passw = enterbox("Enter your password for Database", "Password")

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user='root',
        password='12921292a',
        database="socialnetwork",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:
        choice = 0
        while choice != "Відміна":
            choice = buttonbox("Зайдіть у свій акаунт", "Authorizationr", ["Авторизація", "Відміна"])
            if choice == "Авторизація":
                if loginIn(connection) == "Yes":
                    while choice != "Відміна":
                        choice = buttonbox("Подальші дії", "Social network", ["Додати користувача", "Видалити користувача",
                                                                   "Редагування інфо користувача", "Пошук користувача",
                                                                   "Інфо користувача", "Переглянути друзів користувача",
                                                                   "Перегляд усіх публікацій користувача",'Додати друга',"Додати пост", "Відміна"])
                        if choice == "Додати користувача":
                            addUser(connection)
                        if choice == "Видалити користувача":
                            delUser(connection)
                        if choice == "Редагування інфо користувача":
                            editInfoFromUser(connection)
                        if choice == "Пошук користувача":
                            findUser(connection)
                        if choice == "Інфо користувача":
                            selectAllFromUser(connection)
                        if choice == "Переглянути друзів користувача":
                            allFriend(connection)
                        if choice == "Перегляд усіх публікацій користувача":
                            allPosts(connection)
                        if choice == 'Додати друга':
                            addFriend(connection)
                        if choice == "Додати пост":
                            addPost(connection)


    finally:
        connection.close()

except:
    print("Error")
