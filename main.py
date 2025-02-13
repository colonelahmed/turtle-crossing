from turtle import Screen
from cars import Cars
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600 ,height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

car_manager = Cars()
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_turtle, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()







screen.exitonclick()