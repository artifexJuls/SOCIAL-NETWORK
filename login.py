import pymysql
from easygui import *

userInter = enterbox("Enter your password for Database", "Password")
passw = enterbox("Enter your password for Database", "Password")

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user=userInter,
        password=passw,
        database="socialnetwork",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Ok")
    start_meny = buttonbox('Що бажаєте робити?', 'FILES', ['Вхід', 'Реєстрація'])
    if start_meny == 'Вхід':
        table = multpasswordbox("Зайдіть в свій акаунт", "Table", ["Логін", "Пароль"])
    try:
        with connection.cursor() as cursor:
            login = f"select * FROM `users` where login = '{table[0]}' and parol = '{table[1]}'"
            if cursor.execute(login):
                cursor.execute(login)
                connection.commit()
                msgbox('Ви успішно зайшли у свій акаунт', 'Welcome', 'Перейти до кошика')
    finally:
        connection.close()

except:
    msgbox('Користувач з таким іменем і паролем вже зареєстровані, виберіть інше')
