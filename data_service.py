""" модуль для доступу до вхідних даних та перегляду даних
"""


def get_clients():
    """отримує данні по клієнтам
    Returns:
        clients_list : список клієнтів
    """

    from_file = [
        "1;Універсам №1",
        "6;Галактон",                   
        "7;Поляниця",
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
        "1;1;43102.6;44568.1;209;189",
        "1;6;11707.2;10922.8;45;40",
        "1;7;5498.0;5650.9;20.18;",
        "2;1;52684.5;51825.4;200;190",
        "2;6;15905.3;16000.2;46;45",
        "2;7;6895.0;7000.4;25;23",
        "3;1;68453.4;68400.3;198;195",
        "3;6;14236.6;14000.7;45;43",
        "3;7;7245.2;7300.1;43;43",
        "4;1;7529.9;7524.0;22;21",
        "4;61566.0;1540.1;5;5",
        "4;7;797.0;803.0;3;3",
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





  

