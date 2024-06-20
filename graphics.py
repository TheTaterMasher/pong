from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width=800, height=600, close_func=None):
        self.__root = Tk()
        self.__root.title("Pong")
        self.__root.protocol("WM_DELETE_WINDOW", close_func)
        self.canvas = Canvas(self.__root, bd=5, bg="black", height=height, relief="flat", width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.active = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

class Circle():
    def __init__(self, x1, y1, x2, y2, canvas, fill_color="white"):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.circle_id = canvas.create_oval(x1, y1, x2, y2, fill=fill_color)
    
    def update_pos(self, x_speed, y_speed, fill_color="white"):
        self.canvas.delete(self.circle_id)
        self.x1 += x_speed
        self.y1 += y_speed
        self.x2 += x_speed
        self.y2 += y_speed
        self.circle_id = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=fill_color)

class Rect():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, canvas, fill_color="white"):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.rect_id = canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=fill_color)
    
    def update_pos(self, y_speed, fill_color="white"):
        self.canvas.delete(self.circle_id)
        self.y1 += y_speed
        self.y2 += y_speed
        self.y3 += y_speed
        self.y4 += y_speed
        self.rect_id = self.canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4, fill=fill_color)
