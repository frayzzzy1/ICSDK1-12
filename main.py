""" головний модуль додатку
виводить розрахункову таблицю, зберігає результати в файл
показує на екрані первинні дані
"""

from os import system
from process_data import create_zajavka_list
from data_service import show_dovidnuk, show_pokazn, get_dovidnuk, get_pokazn

MAIN_MENU = \
"""
~~~~~~~~~~~~ ОБРОБКА ЗАЯВОК НА УСТАТКУВАННЯ ~~~~~~~~~~~
1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід списка товарів
0 - завершення роботи
---------------------------
"""

STOP_MESSAGE = 'Для продовження натисніть <Enter>'

TITLE = "ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ"
HEADER = \
"""
=============================================================================================================================================
  Назва магазина | Квартал | Товарообіг плановий |Товарообіг плановий| Відсотки виконання | Продуктивність планова | Продуктивність фактична |
=============================================================================================================================================
"""

FOOTER =  \
"""
====================================================================================================  
"""

def show_table_on_screen(zajavka_list):
    """вивід таблиці заявок на екран
    Args:
        zajavka_list ([type]): список заявок
    """
    print(f"\n{TITLE:^86}")
    print(HEADER)
    
    for zajavka in zajavka_list:
        print(f"{zajavka['Name_store']:20}",                         \
              f"{zajavka['Quarter']:20}",                            \
              f"{zajavka['Commodity_circulation_planned']:^10}",     \
              f"{zajavka['Commodity_circulation_actual']:>10}"       \
              f"{zajavka['Percentage_of_performance']:>10.2f}",      \
              f"{zajavka['Productivity_planned']:>10.2f} 
              f"{zajavka['Productivity_actual']:>10}",            
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
                str(zajavka['Name_store']) + ';' +    \
                str(zajavka['Quarter']) + ';' +    \
                str(zajavka['Commodity_circulation_planned']) + ';' +    \
                str(zajavka['Commodity_circulation_actual']) + ';' +       \
                str(zajavka['Percentage_of_performance']) + ';' +    \
                str(zajavka['Productivity_planned']) + '\n'
                str(zajavka['Productivity_actual']) + '\n'
                
    
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
        pokazn = get_pokazn()
        show_pokazn(pokazn)
        input(STOP_MESSAGE)

   elif command_number == '4':
        dovidnuk = get_dovidnuk()
        show_dovidnuk(dovidnuk)
        input(STOP_MESSAGE)  