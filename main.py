import pymysql
from easygui import *
from login import *
from add_data import *
from filestart import *

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

    try:
        choice = 0
        while choice != "Вихід":
            choice = buttonbox("SocialNetwork", "Authorizationr", ["Авторизація", "Вихід"], 'j.gif')
            if choice == "Авторизація":
                if loginIn(connection) == "Yes":
                    while choice != "Відміна":
                        choice = buttonbox("Подальші дії", "Social network",
                                           ["Settings", "Search", "Friends",
                                            "Posts", "User info",
                                            "Відміна"], '1.gif')
                        if choice == "User info":
                            selectAllFromUser(connection)
                        if choice == "Search":
                            findUser(connection)
                        if choice == "Posts":
                            while choice != "Повернутись":
                                choice = buttonbox("Подальші дії", "Social network",
                                                   ["Додати пост", "Перегляд усіх публікацій", "Видалити пост",
                                                    "Повернутись"], 'post.gif')
                                if choice == "Додати пост":
                                    addPost(connection)
                                if choice == "Перегляд усіх публікацій":
                                    allPosts(connection)
                                if choice == "Видалити пост":
                                    delPost(connection)
                        if choice == "Friends":
                            while choice != "Повернутись":
                                choice = buttonbox("Подальші дії", "Social network",
                                                   ["Додати друга", "Переглянути друзів", "Видалити друга", "Повернутись"],
                                                   'fr.gif')
                                if choice == "Додати друга":
                                    addFriend(connection)
                                if choice == "Переглянути друзів":
                                    allFriend(connection)
                                if choice == "Видалити друга":
                                    delFriend(connection)
                        if choice == "Settings":
                            while choice != "Повернутись":
                                choice = buttonbox("Подальші дії", "Social network",
                                                   ["Реєстрація нового юзера", "Видалити акаунт",
                                                    "Редагувати інформацію", "Повернутись"], 'set.gif')
                                if choice == "Реєстрація нового юзера":
                                    addUser(connection)
                                if choice == "Видалити акаунт":
                                    delUser(connection)
                                if choice == "Редагувати інформацію":
                                    editInfoFromUser(connection)
                else:
                    break
    finally:
        connection.close()

except:
    print("Error")
