import sqlite3 as sq

with sq.connect('hw_8.db') as con:
    cursor = con.cursor()

def create_table(table):
    try:
        cursor.execute(table)
    except sq.Error as e:
        print(e)

def insert_into_countries(country):
    sql_insert = 'INSERT INTO countries (title) VALUES(?)'
    try:
        cursor.execute(sql_insert,(country,))
        con.commit()
    except sq.Error as e:
        print(e)

def insert_into_cities(city):
    sql_insert = 'INSERT INTO сities (title,area,country_id) VALUES(?,?,?)'
    try:
        cursor.execute(sql_insert,city)
        con.commit()
    except sq.Error as e:
        print(e)

def insert_employees(employee):
    sql_insert = 'INSERT INTO employees (first_name,last_name,city_id) VALUES(?,?,?)'
    try:
        cursor.execute(sql_insert,employee)
        con.commit()
    except sq.Error as e:
        print(e)

employees_table = 'CREATE TABLE employees (' \
                  'id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
                  'first_name TEXT NOT NULL ,' \
                  'last_name TEXT NOT NULL ,' \
                  'city_id INTEGER, ' \
                  'FOREIGN KEY (city_id) REFERENCES cities(id))'

countries_table = 'CREATE TABLE countries (' \
                  'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                  'title TEXT NOT NULL ' \
                  ')'

cities_table = 'CREATE TABLE cities (' \
                  'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                  'title TEXT NOT NULL ,' \
                  'area FLOAT DEFAULT 0,' \
                  'country_id INTEGER,' \
                  'FOREIGN KEY (country_id) REFERENCES countries(id))'

def get_lists_of_employees():
    while True:
        try:
            print('\nВы можете отобразить список сотрудников '
                  '\nпо выбранному id города из перечня городов ниже,'
                  '\nдля выхода из программы введите 0: ')
            cursor.execute('SELECT id, title '
                           'FROM cities ')
            lists_of_cities = cursor.fetchall()
            for id_city,name_city in lists_of_cities:
                print(f'ID: {id_city}, CITY: {name_city}')
            id = int(input())
            sql = 'SELECT first_name,last_name,countries.title as country,cities.title as city,area ' \
                  'FROM countries ' \
                  'JOIN cities ON countries.id = cities.country_id ' \
                  'JOIN employees ON employees.city_id = cities.id ' \
                  'WHERE cities.id = (?)'
            cursor.execute(sql, (id,))
            lists = cursor.fetchall()
            for first_name, last_name, country, city, area in lists:
                print(f'\nName: {first_name}'
                      f'\nLast_name: {last_name}'
                      f'\nCountry: {country}'
                      f'\nCity: {city}'
                      f'\nArea: {area}')
            if id == 0:
                break
        except ValueError:
            print('В ВВОД ПРИНИМАЮТСЯ ТОЛЬКО ЦИФРЫ! (ID 1-7) ')





# create_table(countries_table)
# create_table(cities_table)
# insert_into_countries('Kyrgyzstan')
# insert_into_countries('Russia')
# insert_into_countries('USA')
# insert_into_cities(('Bishkek',127,1))
# insert_into_cities(('Osh',182,1))
# insert_into_cities(('Naryn',40.51,1))
# insert_into_cities(('Moskva',2511,2))
# insert_into_cities(('St.Petersburg',1439,2))
# insert_into_cities(('New-York',783.8,3))
# insert_into_cities(('Chicago',600,3))
# create_table(employees_table)
# insert_employees(('Анастасия','Куликова',1))
# insert_employees(('Анна','Савельева',2))
# insert_employees(('Даниил','Смирнов',4))
# insert_employees(('София','Соколова',3))
# insert_employees(('Сергей','Куликов',5))
# insert_employees(('Артём','Демин',7))
# insert_employees(('Кристина','Третьякова',6))
# insert_employees(('Каролина','Афанасьева',4))
# insert_employees(('Алина','Воронова',1))
# insert_employees(('Тимофей','Зайцев',5))
# insert_employees(('Егор','Савельев',7))
# insert_employees(('Максим','Власов',3))
# insert_employees(('Николай','Ершов',1))
# insert_employees(('Александр','Попов',5))
# insert_employees(('Таисия','Горохова',3))



get_lists_of_employees()
