from user import User 
"""импорт класса user"""

my_user = User # новый юзер переменная
my_user =User ("Рекорд" , "Надоев",1200, ) # новый юзер
my_user.sayName() # вызов метода - спросил имя
my_user.saySurname() # вызов метода - спросил фамилию
my_user.sayFamily() # спросил имя и ыамилию
my_user.sayYear() # сколько лет 

newUser = User ("Alex" , "Kvakin" ,1300  ) # новый юзер
newUser.sayName() # спросил имя
newUser.saySurname() # спросил фамилию
newUser.sayFamily() # имя фамилия -- метод
newUser.sayYear() # возраст
