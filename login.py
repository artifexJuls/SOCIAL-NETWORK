import pymysql
from easygui import *

def loginIn(connection):
    table = multpasswordbox("Зайдіть в свій акаунт", "Table", ["Логін", "Пароль"])
    try:
        with connection.cursor() as cursor:
            login = f"select * FROM `users` where login = '{table[0]}' and parol = '{table[1]}'"
            if cursor.execute(login):
                cursor.execute(login)
                connection.commit()
                msgbox('Ви успішно зайшли у свій акаунт', 'Welcome', 'ОК')
                return 'YES'
            else:
                msgbox('Не вірний пароль, або логін')
    finally:
        connection.close()

    return 'YES'
