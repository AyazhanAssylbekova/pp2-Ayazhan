import psycopg2
# создаем таблицу телефонной книги
config = psycopg2.connect(
    host='localhost',
    port = '2005', 
    database='postgres',
    user='postgres',    
    password='Password2005'
)

current = config.cursor()
sql = '''
        CREATE TABLE phonebook2(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            surename VARCHAR(100),
            number VARCHAR(12)
    );
'''
current.execute(sql)

current.close()
config.commit()
config.close()