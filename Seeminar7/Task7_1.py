import Bases_create as b 

def preview_base():
    for i in b.cursor.execute('SELECT * FROM personal'):
        print (*i)


def add_record():
    new_rec = [input("id"), input('Имя'), input("Фамилия"), input("Должность"), input("Зарплата"), input("Премия")]
    
    try:
        b.cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)', new_rec)
        b.bd.commit()
    except:
            print ("Данные есть в базе")

def dell_record(id):
    b.cursor.execute(f'DELETE FROM personal WHERE id={id};')
    b.bd.commit()
    for i in b.cursor.execute('SELECT * FROM personal'):
         print (*i)
    print ("Новая база")

def find_record(column, name):
    b.cursor.execute(f'SELECT * FROM personal WHERE {column} LIKE {name};')
    one=b.cursor.fetchmany()
    return one 

def update_base(wenn, new, id):
    b.cursor.execute(f'UPDATE personaL SET {wenn} = {new} WHERE id = {id};')
    b.bd.commit()
    for i in b.cursor.execute('SELECT * FROM personal'):
        print (*i)





