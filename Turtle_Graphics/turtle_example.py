# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "yellow")
# timmy.forward(100)
# timmy.begin_fill()
# timmy.circle(-200)
# timmy.end_fill()
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
#
# my_screen.exitonclick()
#

# from turtle import *
# from turtle import Screen
#
# my_screen = Screen()
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(185)
#     if abs(pos()) < 1:
#         break
# end_fill()
#
# done()
#
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)
