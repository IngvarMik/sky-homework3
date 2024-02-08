import turtle

pen = turtle.Turtle()


def ring(col, rad): # функция для рисунка динамики - цвет и радиус - форма
    pen.fillcolor(col) # выбрать цвет
    pen.begin_fill()# начать - begin
    pen.circle(rad) # окружность радиус
    pen.end_fill() # закончить рисунок окружности 
""" левое ухо"""
pen.up() # карандаш подняли
pen.setpos(-35, 95) # перенесли по координатам -setpos
pen.down # каарндаш опустить
ring('black', 15) # нарисовать круг - цвет черный .радиус
"""правое ухо"""
pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)
"""голова """
pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 45)
"""рисунок левого глаза"""
pen.up()
pen.setpos(-20, 75)
pen.down
ring('black', 8)
"""рисунок правого глаза"""
pen.up()
pen.setpos(20, 75)
pen.down()
ring('black', 8)
"""прорисовка левого зрачка"""
pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)
"""прорисовка правого зрачка""" 
pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)
"""нос рисуем""" 
pen.up()
pen.setpos(0, 55)
pen.down
ring('black', 10)
""" усы пол носом """
pen.up()
pen.setpos(0, 55)
pen.down()
pen.right(90)
pen.circle(5, 200) # дуга радиусом 5 и длиной 200 пикселей
pen.up() # поднять карандаш
pen.setpos(0, 55) # переместить на позицию
pen.down() # опустить 
pen.left(360)# ход налево карандашом
pen.circle(5, -200)# дуга рисуется радиус 5 , на 200 пикселей влево
pen.hideturtle()
