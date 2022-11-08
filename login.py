import pymysql
from easygui import *


def loginIn(connection):
    while True:
        table = multpasswordbox("Зайдіть у свій акаунт", "Table", ["Логін", "Пароль"])
        with connection.cursor() as cursor:
            login = f"select * FROM `users` where login = '{table[0]}' and parol = '{table[1]}'"
            cursor.execute(login)
            connection.commit()
            result = cursor.fetchall()
            print(login)
            for i in result:
                if table[0] == i["Login"] and table[1] == i["Parol"]:
                    var = "Yes"
                    msgbox('Ви успішно зайшли у свій акаунт', 'Welcome', 'ОК', 'good.gif')
                    break
                else:
                    msgbox("Невірний пороль або логін")
            var = 'Yes'
            break
    return var
