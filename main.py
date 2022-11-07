from login import *

passw = enterbox("Enter your password for Database", "Password")

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password=passw,
        database="Basket",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")

    try:
        choice = 0
        while choice != "Відміна":
            choice = buttonbox("Привіт, щоб почати покупки необхідно авторизуватись", "Authorizationr", ["Авторизація", "Відміна"])
            if choice == "Авторизація":
                if loginIn(connection) == "Yes":
                    while choice != "Відміна":
                        choice = buttonbox("Подальші дії", "Social network", ["Додати користувача", "Видалити користувача",
                                                                   "Редагування інфо користувача", "Пошук користувача",
                                                                   "Інфо користувача", "Переглянути друзів користувача",
                                                                   "Перегляд усіх публікацій користувача", "Відміна"])
                        if choice == "Додати користувача":
                            pass
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
