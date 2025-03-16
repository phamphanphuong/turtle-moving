import turtle

# Khởi tạo màn hình
screen = turtle.Screen()
height = 800
width = 1920

screen.setup(width, height)
screen.bgpic("map.png")
screen.title("Game")

try:
    screen._root.window_centered = True
    screen._root.eval(f'wm geometry {screen._root} {width}x{height}+{(screen._root.winfo_screenwidth() - width) // 2}+{(screen._root.winfo_screenheight() - height) // 2}')
except AttributeError:
    pass

def onclick(x, y):
    print(x, y)
    
screen.onclick(onclick)

screen.mainloop()
