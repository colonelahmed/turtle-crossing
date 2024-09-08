from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Cars:

    def __init__(self):
        self.cars = []
        self.car_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car =Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(280, random_y)
            car.setheading(180)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += 10




        # for position in POSITIONS:
        #     car = Turtle("square")
        #     car.color("black")
        #     car.penup()
        #     car.goto(position)
        #     car.setheading(180)
        #     self.tb.append(car)

    # def move(self):
    #     for seg_num in range(len(self.tb)-1, 0, -1):
    #         new_x = self.tb[seg_num - 1].xcor()
    #         new_y = self.tb[seg_num - 1].ycor()
    #         self.tb[seg_num].goto(new_x, new_y)
    #     self.tb[0].forward(20)
    #


