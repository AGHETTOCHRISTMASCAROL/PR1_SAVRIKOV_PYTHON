import re
import datetime

class ExceptionIncorrectDate(Exception):
    pass
class ExceptionIncorrectFormat(Exception):
    pass

def addition_script():
    now :datetime = datetime.datetime.now()
    
    print('Система:\tФамилия Имя Отчество год_рождения — Вводи так:')
    
    while True:
        try:
            with open('Users.txt', 'a') as file:
                user_cortege :str = input()
                correct_user_cortege :str = ''
                format_check :re = re.match('\s*[А-Я][а-я]+\s+[А-Я][а-я]+\s+[А-Я][а-я]+\s+\d\d\d\d\s*', user_cortege) # Cын Илона Маска, X AE A—12, не пройдет(
        
                if format_check:
                    for index, user_attribute in enumerate(user_cortege.split(), start=1): # Cобираем кортеж в корректном формате, без лишних пробелов
                        if index == 4:
                            if int(user_attribute) > now.year: # Исключаем не родившихся людей
                                raise ExceptionIncorrectDate()
                        correct_user_cortege += user_attribute + ' '
        
                    file.write(correct_user_cortege.rstrip() + '\n')
                    print('Система:\tДанные добавлены, добавляйте новые:')
                else:
                    raise ExceptionIncorrectFormat()
        
        except KeyboardInterrupt:
            print("Система:\tВы нажали ctrl + c, и вышли в меню")
            break
    
        except ExceptionIncorrectFormat:
            print("Система:\tДанные введены некорректно, попробуйте снова: ")
    
        except ExceptionIncorrectDate:
            print(f'Система:\tЧеловек {user_attribute} года рождения еще не родился, попробуйте снова:')

def viewing_script():
    try:
        with open('Users.txt', 'r') as file:
            print(f'{"Фамилия":<20}{"Имя":<20}{"Отчество":<20}{"Год рождения"}\n\n'.upper())
            while True:
                user_cortege :str = file.readline()
                
                if not user_cortege:
                    break

                for index, user_attribute in enumerate(user_cortege.split(), start=1):
                    if index == 4:
                        print(user_attribute, end='\n\n\n')
                    else:
                        print(f'{user_attribute:<20}', end='')

    except FileNotFoundError:
        print('Система:\tФайл не найден')

try:
    while True:
        choice_menu :str = input('\n1. Добавить данные в файл \n2. Прочитать данные из файла\n\n')

        if choice_menu == '1':
            addition_script()

        elif choice_menu == '2':
            viewing_script()

        else:
            continue
except KeyboardInterrupt:
    print('Система:\tВы вышли из программы')