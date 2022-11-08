# SOCIAL NETWORK
****
>homework
****
Даний проєкт є міні-відворенням базових функцій в соц.мережах.\
Створений разом з `WaRaN1` і `maximbabaiev`
>:eyes: усі файли мають бути в одній папці для коректної роботи коду

:books: Потрібно встановити: 

| Бібліотекy| Версія | Команди|
|----------------|:---------:|----------------:|
| pymysql| 1.0.1 | import pymysql|
| Easygui | 0.98.3 | from easygui import * |

# Логіка коду :large_blue_diamond:
****
У проєкті є 4 файли. ___FileStart,Login,AddData___ i ___Main___.

>`Main` - це основний файл, який треба запускати самим першим і єдиним, маючи відкриті на фоні нище перераховані.

>`FileStart` - це файл в якому прописаний код створення датабази.
>При його запуску - вас запитають ваш логін(root) і пароль до SQL. Потім вам створиться database, заповниться таблицями і додасться дефолтний акаунт в таблицю users.

>У дефолтного юзера: `login` буде - Wazan,а пароль - `1234`

>`Login` - це файл, який буде викликатись наступним. Він перевіряє чи є ви у таблиці users, чи ви ввели правильний логін/пароль - чи маєте акаунт у базі. 

>`AddData` - це файл в якому записані усі функції, імпортувавши його у файл `main` - ми зберегли більше місця і чистоту другого.

# Можливості програми :large_blue_diamond:
****
Після того, як ви зайшли у свій акаунт - вам відкривається меню Easygui з десятком варіантів роботи в SQL.

Декілька з доступних функцій:
****
+ `Post` - керування таблицею з постами.
    - Вам висвітлиться віконце `buttonbox` де ви зможете вибрати наступні дії:
        - `Додати пост`
            - Дати ім'я публікації, прив'язати її до свого логіна, написати саму публікацію.  :heavy_check_mark: 
        - `Перегляд усіх публікацій`
            - Побачити усі публікації свої, або іншої людини, логін, якої ви знаєте і вона є у database.  :heavy_check_mark: 
        - `Видалити пост`
            - Видаляти пости.  :heavy_check_mark: 
     - Усі дії проводяться через таблицю `Posts`
****
+ `Friends` - керувати друзями.
- Вам висвітлиться віконце `buttonbox` де ви зможете вибрати наступні дії:
  - `Додати друга`  :heavy_check_mark: 
  - `Переглянути друзів`  :heavy_check_mark: 
  - `Видалити друга`  :heavy_check_mark: 
- Усі дії проводяться через таблицю `Friends`
****
+ `Search`
  - Пошук користувачів по логіну, вертає усю інформацію про них.  :heavy_check_mark: 
 - Ці дії проводяться через таблицю `users`
****
+ `Settings`
  -  Реєстрація нового юзера  :heavy_check_mark: 
  -  Видаляння акаунта  :heavy_check_mark: 
  -  Редагування інформації  :heavy_check_mark: 
- Ці дії проводяться через таблицю `users`
****
>> :heavy_multiplication_x: Баги (фічі) коду :heavy_multiplication_x: \
Користувач по суті являється адміністратором соц.мережі.\
Так, як для запуску деякий унікальних операцій - він має ввести Login, але цей логін може бути любий і ніде не прописано правило, що користувач може вводити тільки той логін під яким зайшов.\
Тож, це як адмін-панель. :necktie:
