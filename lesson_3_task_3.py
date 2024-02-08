from address import Address # импорт адресс
from mailing import Mailing # импорт майлинг 

# Создаем экземпляр класса Mailing
to_address = Address("123456", "City A", "Street A", "1", "101") # адрес куда
from_address = Address("654321", "City B", "Street B", "2", "202") # адрес откуда
mailing_in = Mailing(to_address, from_address, 10.50, "ABC") # как новый юзер - ввод данных адреса, стоимость и трек номер

"""печать по заданию через f  строка """
print(f"Отправление {mailing_in.track} из индекс {mailing_in.to_address.index}, город {mailing_in.to_address.city} на улицу {mailing_in.to_address.street},  дом {mailing_in.to_address.house}, квартира {mailing_in.to_address.apartment}, стоимость {mailing_in.cost} ")