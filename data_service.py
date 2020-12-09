""" модуль для доступу до вхідних даних та перегляду даних
"""


def get_clients():
    """отримує данні по клієнтам
    Returns:
        clients_list : список клієнтів
    """

    from_file = [
        "322;Ціна зарядки", 
        "170;Книга",                   
        "350;Навушники",
        "220;Колонка",
        "180;Коврик до комп'ютерної миші",
        "450;Клавіатура",
        "100;Світодіодна гірлянда",
        "300;Мікрофон",
        "150;Розетка",
        "190;Налог на куплені товари",
    ]

    # накопичувач рядків
    clients_list = []

    for line in from_file:
        line_list = line.split(';')
        clients_list.append(line_list)

    return clients_list


def get_orders():
    """повертає список накладних
    Returns:
        from_file: список накладних
    """

    from_file = [       
        "322;4,0;21,0;18,0;330,0;269,0;",
        "170;7,0;40,0;48,0;104,0;271,0;",
        "350;7,0;10,0;21,0;122,0;51,0;",
        "220;5,0;17,0;40,0;63,0;526,0;",
        "180;396,0;832,0;1818,0;6631,0; 19426,0;",
        "450;2,0;3,0;3,0;3,0;6,0;",
        "100;6,0;58,0;165,0;483,0;850,0;",
        "300;1,0;2,0;12,0;25,0;119,0;",
        "150;2,0;1,0;1,0;0,3;2,0;",
        "190;54,0;3,0;3,0;3,7;2,0;",
    ]

    # розбити строку на реквізити та перетворити формати (при потребі)
    orders_list = []    # список-накопичувач
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        orders_list.append(line_list)

    return orders_list





def show_clients(clients):
    """виводить список клієнтів за заданої умови
    Args:
        clients : сприсок клієнтів
    """

    client_code_from = input("З якого кода клієнта? ")
    client_code_to   = input("По який кода клієнта? ")
    
    for client in clients:
        if  client_code_from  <= client[0] <= client_code_to:
            print( "код: {:4} назва: {:18} адреса: {:20}".format(client[0], client[1], client[2]))


# clients = get_clients()
# show_clients(clients)

orders = get_orders()
for o in  orders:
    print(o)





  

