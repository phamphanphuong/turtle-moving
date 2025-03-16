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


try:
    screen._root.window_centered = True
    screen._root.eval(f'wm geometry {screen._root} {width}x{height}+{(screen._root.winfo_screenwidth() - width) // 2}+{(screen._root.winfo_screenheight() - height) // 2}')
except AttributeError:
    pass

screen.tracer(0)
screen.title("Game")


player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.penup()
player.speed(0)
player.goto(-360, 70)
playerSpeed = 0.03

# Tạo radar
radar = turtle.Turtle()
radar.shape("circle")
radar.color("green")
radar.penup()
radar.speed(0)
radar.shapesize(0.5)  # Giảm kích thước radar để trông nhỏ hơn

# Hàm làm radar nhấp nháy
radar_visible = True
def blink_radar():
    global radar_visible
    if radar_visible:
        radar.hideturtle()
    else:
        radar.showturtle()
    radar_visible = not radar_visible
    screen.ontimer(blink_radar, 500)  # Nhấp nháy mỗi 500ms (0.5 giây)

# Bắt đầu nhấp nháy radar
blink_radar()

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
    # print(x, y)

    # Lấy màu tại điểm click
    # color = color_detector.get_color_at(x, y)
    # print("color =", color)

    # Lấy màu tại vị trí của người chơi
    # player_color = color_detector.get_color_at(player.xcor(), player.ycor())
    # print("playerColor =", player_color)

    enemy.goto(x, y)
    
    goc = player.towards(enemy)
    print("goc = ", goc)
    print("play_to_enemy = ",player.towards(enemy))
    print("player.heading() = ", player.heading())

screen.onclick(clickChuoi)

moveable_color = (255, 201, 14)
TURN = 1
while True:
   
   # Cập nhật vị trí radar (đặt nó phía trước player)
    radar_x = player.xcor() + math.cos(math.radians(player.heading())) * 20
    radar_y = player.ycor() + math.sin(math.radians(player.heading())) * 20
    radar.goto(radar_x, radar_y)
    
    
    
    player.setheading(player.towards(enemy))
    
   

    # Tính toán vị trí tiếp theo
    next_color = color_detector.will_move_to_color(player.xcor(), player.ycor(), playerSpeed, player.heading())

    # Di chuyển nếu màu là màu đường đi
    if next_color == moveable_color:
        player.forward(playerSpeed)
    elif next_color != moveable_color:
        for i in range(360):
            goc = player.towards(enemy)
            if 90 < goc < 270:
                player.left(TURN)
            else:
                player.right(TURN)
            
            next_color = color_detector.will_move_to_color(player.xcor(), player.ycor(), playerSpeed, player.heading())
            if next_color == moveable_color:
                player.forward(playerSpeed)
                break
      
    screen.update()

