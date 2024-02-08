from address import Address # обьявление класса mailing

class Mailing:
    def __init__(self, to_address, from_address, cost, track): # адре куда,адрес откуда,стоимость,трек номер
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track