import Task7_1 as f

def input_choice():

    while True:
        user_choice= input ("1-посмотреть базу, 2- добавить запись, 3- удалить запись, 4- найти по ФИО, 5 - изменить данные, q- выход")
        if user_choice == "1":
            f.preview_base()
        elif user_choice == "2":
            f.add_record()
        elif user_choice == "3":
            f.dell_record(input("Какое id удалить? "))
        elif user_choice == "4":
            f.find_record()
        elif user_choice == "5":
            f.update_base(input("Что помееять?"), input("новое значение"))    
        elif user_choice == "q":
            print ('Выход')
            break
        else:
            print ('Не верно введен')

