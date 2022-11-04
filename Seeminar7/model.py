import sqlite3
bd = sqlite3.connect("Data.db")
cursor = bd.cursor() 

def preview_base():
    for i in cursor.execute('SELECT * FROM personal'):
        print (*i)


def add_record():
    new_rec = [input("id"), input('Имя'), input("Фамилия"), input("Должность"), input("Зарплата"), input("Премия")]
    
    try:
        cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)', new_rec)
        bd.commit()
    except:
            print ("Данные есть в базе")

def dell_record(id):
    cursor.execute(f'DELETE FROM personal WHERE id={id};')
    bd.commit()
    for i in cursor.execute('SELECT * FROM personal'):
         print (*i)
    print ("Новая база")

def find_record(column, name):
    cursor.execute(f'SELECT * FROM personal WHERE {column} LIKE {name};')
    one=cursor.fetchmany()
    return one 

def update_base(wenn, new, id):
    cursor.execute(f'UPDATE personaL SET {wenn} = {new} WHERE id = {id};')
    bd.commit()
    for i in cursor.execute('SELECT * FROM personal'):
        print (*i)





