import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
car = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.write_scoreboard()

    car.create_car()
    car.move_cars()

    for vehicle in car.all_cars:
        if player.distance(vehicle) < 20:
            score.game_over()
            game_is_on = False

    #Detect player reached the finish line
    if player.ycor() > 280:
        player.reset_position()
        score.update_level()
        car.increase_car_speed()



screen.exitonclick()