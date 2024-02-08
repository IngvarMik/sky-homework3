from smartfone import Smartfone # обьявление класса смартфон

"""каталог смартфон"""
catalog = [
    Smartfone("fhilips" , "fizz" , " +7976464466") , 
    Smartfone ("samsung" , " galaxy" , " +7976464643"),
    Smartfone("poco" , "lann" , " +7976464664"),
    Smartfone("huawei" , " nova" ," +798764642"),
    Smartfone( "honor" , "iceland" , " +7964646464")
]

"""цикл  - весь каталог печать """
for phone in catalog:
    print(f"{phone.brand} > {phone.model} >{phone.phone_number}") # функция f
