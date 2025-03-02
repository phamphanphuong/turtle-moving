from PIL import Image

class ColorDetector:
    def __init__(self, image_path):
        """Khởi tạo với đường dẫn ảnh."""
        self.image = Image.open(image_path).convert("RGB")
        self.width, self.height = self.image.size

    def get_color_at(self, x, y):
        """Lấy màu tại vị trí (x, y) dựa trên hệ tọa độ của Turtle."""
        adjusted_x = int(x + self.width / 2)
        adjusted_y = int(self.height / 2 - y)
        return self.image.getpixel((adjusted_x, adjusted_y))

    def will_move_to_color(self, x, y, speed, angle):
        """Lấy màu tại điểm mà vật sẽ di chuyển đến."""
        import math
        next_x = x + speed * math.cos(math.radians(angle))
        next_y = y + speed * math.sin(math.radians(angle))
        return self.get_color_at(next_x, next_y)
