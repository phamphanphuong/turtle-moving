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


def clickChuoi(x, y):
    print(x, y)
    
    # Lấy màu tại điểm click
    # Adjust coordinates to match image's coordinate system
    adjusted_x = int(x + width / 2)
    adjusted_y = int(height / 2 - y)
    color = image.getpixel((adjusted_x, adjusted_y))
    print("color = ", color)
    
    playerColor = image.getpixel((int(player.xcor() + width / 2), int(height / 2 - player.ycor())))
    print("playerColor = ", playerColor[0], playerColor[1], playerColor[2])
    
    enemy.goto(x, y)
    
screen.onclick(clickChuoi)


# (255, 201, 14) là màu của đường đi
# (0, 0, 0) là màu của tường


while True:
    
    
    
    # torwards enemy
    player.setheading(player.towards(enemy))
    
    # Calculate next position
    next_x = player.xcor() + playerSpeed * math.cos(math.radians(player.heading()))
    next_y = player.ycor() + playerSpeed * math.sin(math.radians(player.heading()))
    
    playerCorlor = image.getpixel((int(next_x + width / 2), int(height / 2 - next_y)))
    
    # forward if color is yellow
    if playerCorlor == (255, 201, 14):
        player.forward(playerSpeed)
      
      
    
    # player.setheading(player.towards(enemy))
    screen.update()


