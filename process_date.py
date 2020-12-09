""" формування заявок на устаткування по магазину
"""

from data_service import get_clients, get_orders


# структура рядка таблиці заявок на устаткування
zajavka = {

    'Name_store'                       : '',     # Назва магазина 
    'Quarter'                          : '',     # Квартал
    'Commodity_circulation_planned'    : 0.0,    # Товарообіг плановий
    'Commodity_circulation_actual'     : 0.0,    # Товарообіг фактичний
    'Percentage_of_performance'        : 0.0,    # Відсотки виконання
    'Productivity_planned'             : 0.0     # Продуктивність планова
    'Productivity_actual'              : 0.0     # Продуктивність фактична
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
