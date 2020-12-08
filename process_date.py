""" формування заявок на устаткування по магазину
"""

from data_service import get_clients, get_orders


# структура рядка таблиці заявок на устаткування
zajavka = {

 'currency_name'  : '',       # найменування валюти
 'currency_code'  : 0,        # код валюти
 'order_number'   : '',       # 1.10
 'course'         : 0,        # курс на 1.11
 'price'          : 0.0,      #  курс на 1.12
 'total'        : 0.0       # рівень за 3 місяці
}

clients = get_clients()
orders = get_orders() 


def create_zajavka_list():
    """[summary]
    """
   
    def get_clients_name(client_code):
        """повертає назву клієнта по його коду
        Args:
            client_code ([type]): [description]
        Returns:
             [type]: [description]
        """
         for client in clients:
            if client_code  = client[0]:
                return client[1]
        
        return "*** назва не знайдена"

    
    # накопичувач заявок
     zajavka_list = []

     for order in orders:
    
         # створити робочу копію
         zajavka_work = zajavka.copy()
     
         zajavka_work['currency_name']    = order[2]
         zajavka_work['order_numder']    = order[1]
         zajavka_work['course']             = order[3]
         zajavka_work['price']           = order[4]
         zajavka_work['total']           = zajavka_work['course'] * zajavka_work['price']
        zajavka_work['currency_code']      =get_clients_name(order[0])
        
        
         zajavka_list.append(zajavka_work)

    return zajavka_list


z = create_zajavka_list()
for i in z:
print(i)
