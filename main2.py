import math
import turtle
from PIL import Image
# import numpy as np



# Load ảnh
image = Image.open("map.png").convert("RGB")
width, height = image.size

# Khởi tạo Turtle
screen = turtle.Screen()
screen.setup(width, height)
screen.bgpic("map.png")  # Hiển thị ảnh làm nền

screen.tracer(0)
screen.title("Game")


player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.penup()
player.speed(0)
player.goto(-360, 70)

playerSpeed = 0.01

enemy = turtle.Turtle()
enemy.shape("turtle")
enemy.color("blue")
enemy.penup()
enemy.speed(0)
enemy.goto(360, -70)

from color_detector import ColorDetector

# Khởi tạo ColorDetector
color_detector = ColorDetector("map.png")

def clickChuoi(x, y):
    print(x, y)

    # Lấy màu tại điểm click
    color = color_detector.get_color_at(x, y)
    print("color =", color)

    # Lấy màu tại vị trí của người chơi
    player_color = color_detector.get_color_at(player.xcor(), player.ycor())
    print("playerColor =", player_color)

    enemy.goto(x, y)

screen.onclick(clickChuoi)

while True:
    player.setheading(player.towards(enemy))

    # Tính toán vị trí tiếp theo
    next_color = color_detector.will_move_to_color(player.xcor(), player.ycor(), playerSpeed, player.heading())

    # Di chuyển nếu màu là màu đường đi
    if next_color == (255, 201, 14):
        player.forward(playerSpeed)


    screen.update()

