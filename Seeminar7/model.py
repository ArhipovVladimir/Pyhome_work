import sqlite3

bd = sqlite3.connect("Data.db")
cursor = bd.cursor() 

def preview_base():
    bd = sqlite3.connect("Data.db")
    cursor = bd.cursor() 
    for i in cursor.execute('SELECT * FROM personal'):
        print (*i)


def add_record():
    bd = sqlite3.connect("Data.db")
    cursor = bd.cursor() 
    new_rec = [input("id"), input('Имя'), input("Фамилия"), input("Должность"), input("Зарплата"), input("Премия")]
    
    try:
        cursor.execute('INSERT INTO personal VALUES(?,?,?,?,?,?)', new_rec)
        bd.commit()
    except:
            print ("Данные есть в базе")

def dell_record(id):
    bd = sqlite3.connect("Data.db")
    cursor = bd.cursor() 
    cursor.execute(f'DELETE FROM personal WHERE id={id};')
    bd.commit()
    for i in cursor.execute('SELECT * FROM personal'):
         print (*i)
    print ("Новая база")

def find_record(column, name):
    bd = sqlite3.connect("Data.db")
    cursor = bd.cursor() 
    cursor.execute(f'SELECT * FROM personal WHERE {column} LIKE {name};')
    one=cursor.fetchmany()
    return one 

def update_base(wenn, new, id):
    bd = sqlite3.connect("Data.db")
    cursor = bd.cursor() 
    cursor.execute(f'UPDATE personaL SET {wenn} = {new} WHERE id = {id};')
    bd.commit()
    for i in cursor.execute('SELECT * FROM personal'):
        print (*i)





