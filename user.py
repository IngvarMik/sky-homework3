class User: # класс user
    
    def __init__(self, first_name,last_name,year): # имя ,фамилия,возраст
        self.first_name=first_name
        self.last_name=last_name
        self.year = year
        

    def sayName(self): # метод - скажи имя
        print("меня зовут " , self.first_name)

    def saySurname(self): # метод скажи фамидию
        print("моя фамилия  "  , self.last_name)

    def sayFamily(self): # метод скажи имя фамилию
        print ("мои имя и фамилия " , self.first_name ,self.last_name)

    def sayYear(self): # метод скажи возраст года
        print("мне многа лет - вот скока :", self.year)
        
    


