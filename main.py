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
        user='Julia',
        password='2002dododo',
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
                                                                   "Перегляд усіх публікацій користувача", "Відміна"])
                        if choice == "Додати користувача":
                            addUser(connection)
                        if choice == "Видалити користувача":
                            pass
                        if choice == "Редагування інфо користувача":
                            pass
                        if choice == "Пошук користувача":
                            pass
                        if choice == "Інфо користувача":
                            pass
                        if choice == "Переглянути друзів користувача":
                            pass
                        if choice == "Перегляд усіх публікацій користувача":
                            pass


    finally:
        connection.close()

except:
    print("Error")
