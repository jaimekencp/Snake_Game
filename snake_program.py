''' Assignment: Pirate
Created on 12 dec. 2019
@author: Jaime Ken Costa Pereira'''


from ipy_lib import SnakeUserInterface
from classes import Snake
from Coordinate import Coordinate
from classes import CoordinateRow

WIDTH = 20
HEIGHT = 20
SCALE = 1
FP = 24  # frame per second

ui = SnakeUserInterface(WIDTH, HEIGHT, SCALE)


def calculate_new_head(coordinate):
    new_coordinate = Coordinate(coordinate.x, coordinate.y)
    if snake.direction == "r":
        new_coordinate.x += 1

    if snake.direction == "l":
        new_coordinate.x -= 1

    if snake.direction == "u":
        new_coordinate.y -= 1

    if snake.direction == "d":
        new_coordinate.y += 1

    return new_coordinate


def correct_new_head(new_head):
    if new_head.x >= WIDTH and snake.direction == "r":
        new_head.x = 0

    if new_head.x < 0 and snake.direction == "l":
        new_head.x = WIDTH - 1

    if new_head.y < 0 and snake.direction == "u":
        new_head.y = HEIGHT - 1

    if new_head.y >= HEIGHT and snake.direction == "d":
        new_head.y = 0

    return new_head


def directions():
    new_coordinate = calculate_new_head(snake.get_head())
    new_head = correct_new_head(new_coordinate)

    snake.add_body(new_head)
    snake.remove_body(snake.get_tail())


def process_alarm():
    global score
    ui.clear()
    directions()
    for part in snake.snake_body.coordinaterow:
        ui.place(part.x, part.y, ui.SNAKE)
    ui.place(food.x, food.y, ui.FOOD)
    score_display()
    ui.show()


def process_event(event):
    global score
    change_direction(event)
    if event.name == "alarm":
        process_alarm()

    ui.show()


def snake_reaction():
    global score, food
    new_head = calculate_new_head(snake.get_head())
    new_head = correct_new_head(new_head)

    if new_head.is_equal(food):
        snake.snake_grow()
        food = food_coordinate()
        score = int(score) + 1
        score = str(score)

    if snake.hit_something(new_head):
        ui.clear_text()
        ui.print_("game over")
        ui.stay_open()


def change_direction(event):
    if event.name == "arrow":
        if event.data == "r" and snake.direction != "l":
            snake.direction = "r"

        if event.data == "l" and snake.direction != "r":
            snake.direction = "l"

        if event.data == "u" and snake.direction != "d":
            snake.direction = "u"

        if event.data == "d" and snake.direction != "u":
            snake.direction = "d"


def food_coordinate():
    food_x = ui.random(WIDTH)
    food_y = ui.random(HEIGHT)
    food_position = Coordinate(food_x, food_y)
    if not snake.hit_something(food_position):
        return food_position
    else:
        return food_coordinate()


def score_display():
    global score
    ui.clear_text()
    ui.print_(score)


snake = Snake()
snake_coordinate = [[0, 0], [1, 0]]
for coordinate in snake_coordinate:
    snake.add_body(Coordinate(coordinate[0], coordinate[1]))
food = food_coordinate()
score = "0"

ui.set_animation_speed(FP)

while True:  # infinite loop
    event = ui.get_event()
    snake_reaction()
    process_event(event)
    ui.show()
