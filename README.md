# SOCIAL NETWORK
****
>homework
****
Даний проєкт є міні-відворенням базових функцій в соц.мережах.\
Створений разом з `WaRaN1` і `maximbabaiev`
>:eyes: усі файли мають бути в одній папці для коректної роботи коду

:books: Потрібно встановити: 

| Бібліотеки у коді| Версія | Команди|
|----------------|:---------:|----------------:|
| pymysql| 1.0.1 | import pymysql|
| Easygui | 0.98.3 | from easygui import * |

# Логіка коду :large_blue_diamond:
****
У проєкті є 4 файли. ___FileStart,Login,AddData___ i ___Main___.

>`Main` - це основний файл, який треба запускати самим першим і єдиним, маючи відкриті на фоні нище перераховані.

>`FileStart` - це файл в якому прописаний код створення датабази.
>При його запуску - вас запитають ваш логін(root) і пароль до SQL. Потім вам створиться database, заповниться таблицями і додасться вам дефолтний акаунт в таблицю users.

>У дефолтного юзера: `login` буде - Wazan,а пароль - `1234`

>`Login` - це файл, який буде викликатись наступним. Він перевіряє чи є ви у таблиці users, чи ви ввели правильний логін/пароль - чи маєте акаунт у базі. 

>`AddData` - це файл в якому записані усі функції, імпортувавши його у файл `main` - ми зберегли більше місця і чистоту другого.

# Можливості програми
****
Після того, як ви зайшли у свій акаунт - вам відкривається меню Easygui з десятком варіантів роботи в SQL.

Декілька з доступних функцій:\

+ Ви можете керувати постами через функціонал `Post`\
Вам висвітлиться віконце `buttonbox` де ви зможете вибрати наступні дії:
- `Додати пост`
    - :heavy_check_mark: Дати ім'я публікації, прив'язати її до свого логіна, написати саму публікацію.
- `Перегляд усіх публікацій`
    - :heavy_check_mark: Побачити усі публікаї свої, або іншої людини, логін, якої ви знаєте і є у database.
- `Видалити пост`
    - :heavy_check_mark: Видаляти пости.
    - :heavy_check_mark: Усі дії проводяться через таблицю `Post`
****
+ Ви можете керувати друзями.\
Усі дії проводяться через таблицю `Post`
-Вам висвітлиться віконце `buttonbox` де ви зможете вибрати наступні дії:
  - `Додати друга`
  - `Переглянути друзів`
  - `Видалити друга`
****
+ `Search`\
  -Пошук користувачів по логіну, вертає усю інформацію про них.
****
+ `Settings`
  - :heavy_check_mark: Реєстрація нового юзера
  - :heavy_check_mark: Видаляння акаунта
  - :heavy_check_mark: Редагування інформації
