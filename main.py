"""головний модуль додатку
виводить розрахункову талицю, зберігає результати в файл
показу на екрані первинні дані
"""

from os import system
from process_data import create_zajavka_list
from data_service import show_orders, show_clients, get_orders, get_clients

MAIN_MENU = \
"""
~~~~~~~~~~~~ ОБРОБКА ЗАЯВОК НА УСТАТКУВАННЯ ~~~~~~~~~~~
1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід курсу валют
0 - завершення роботи
---------------------------
"""

STOP_MESSAGE = 'Для продовження нажмить <Enter>'

TITLE = "ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ"
HEADER = \
"""
=====================================================================================
Найменування валюти|Код валюти | Курс 1.11 | Курс на 1.12 | Ціна| Рівень за 3 місяці      
=====================================================================================  
"""

FOOTER =  \
"""
=====================================================================================  
"""

def show_table_on_screen(zajavka_list):
    """вивід таблиці заявок на екран
    Args:
        zajavka_list ([type]): список заявок
    """
    print(f"\n{TITLE:^86}")
    print(HEADER)
    
    for zajavka in zajavka_list:
        print(f"{zajavka['currency_name']:20}",     \
              f"{zajavka['currency_code']:20}",     \
              f"{zajavka['order_number']:^10}",   \
              f"{zajavka['course']:>10}",            \
              f"{zajavka['price']:>10.2f}",       \
              f"{zajavka['total']:>10.2f}"            
              ) 
    
    print(FOOTER)


def write_zajavka(zajavka_list):
    """записує масив заявок в файл
    Args:
        zajavka_list ([type]): список заявок
    """
    
    with open('./data/zajvaka.txt', "w") as zajavka_file:
        for zajavka in zajavka_list:
            line = \
                zajavka['currency_name'] + ';' +    \
                zajavka['currency_code'] + ';' +    \
                zajavka['order_number'] + ';' +    \
                str(zajavka['course']) + ';' +       \
                str(zajavka['price']) + ';' +    \
                str(zajavka['total']) + '\n'
    
            zajavka_file.write(line)
       
        print("Файл сформовано ...") 
    
while True:
   
   system('clear')
   print(MAIN_MENU) 
   command_number = input("Введіть номер команди: ")
   
   if command_number == '0':
       print('\nПрограмма завершила роботу')
       exit(0)
       
   elif command_number == '1':
       zajavka_list = create_zajavka_list()
       show_table_on_screen(zajavka_list)
       input(STOP_MESSAGE)
       
   elif command_number == '2':
        zajavka_list = create_zajavka_list()
        write_zajavka(zajavka_list)
        input(STOP_MESSAGE)
        
   elif command_number == '3':
       orders = get_orders()
       show_orders(orders)
       input(STOP_MESSAGE)
       
   elif command_number == '4':
       cliens = get_clients()
       show_clients(cliens)
       input(STOP_MESSAGE