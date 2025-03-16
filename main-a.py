import math
import turtle
from PIL import Image
import heapq  # Dùng cho thuật toán A*

# Load ảnh
image = Image.open("map.png").convert("RGB")
width, height = image.size
pixels = image.load()

# Khởi tạo Turtle
screen = turtle.Screen()
screen.setup(width, height)
screen.bgpic("map.png")  # Hiển thị ảnh làm nền
screen.tracer(0)
screen.title("Game")

# Khởi tạo Player
player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.penup()
player.speed(1)
player.goto(-360, 70)

# Khởi tạo Enemy
enemy = turtle.Turtle()
enemy.shape("turtle")
enemy.color("blue")
enemy.penup()
enemy.speed(5)
enemy.goto(360, -70)

# Màu có thể đi được
MOVEABLE_COLOR = (255, 201, 14)

# Tạo ma trận bản đồ
def is_walkable(x, y):
    """ Kiểm tra xem pixel tại (x, y) có thể đi được không """
    if 0 <= x < width and 0 <= y < height:
        return pixels[x, height - y] == MOVEABLE_COLOR
    return False

# Chuyển đổi tọa độ màn hình sang tọa độ ma trận
def screen_to_grid(x, y):
    return int(x + width // 2), int(y + height // 2)

def grid_to_screen(x, y):
    return x - width // 2, y - height // 2

# Thuật toán A* tìm đường đi
def heuristic(a, b):
    """ Hàm ước lượng khoảng cách từ điểm a đến b """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal):
    """ Tìm đường từ start đến goal bằng A* """
    open_set = []
    heapq.heappush(open_set, (0, start))  # (giá trị f, điểm)
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        for neighbor in neighbors:
            if not is_walkable(*neighbor):
                continue
            
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Không tìm được đường

# Di chuyển đến mục tiêu
def move_player_along_path(path):
    for grid_x, grid_y in path:
        screen_x, screen_y = grid_to_screen(grid_x, grid_y)
        player.setheading(player.towards(screen_x, screen_y))
        player.goto(screen_x, screen_y)
        screen.update()

# Sự kiện click chuột để đặt enemy
def click_handler(x, y):
    enemy.goto(x, y)
    start = screen_to_grid(player.xcor(), player.ycor())
    goal = screen_to_grid(x, y)
    
    path = a_star(start, goal)
    
    if path:
        move_player_along_path(path)
    else:
        print("Không tìm được đường đi!")

screen.onclick(click_handler)

screen.mainloop()
