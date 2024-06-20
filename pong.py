from graphics import Window, Rect, Circle
from time import sleep
class Pong():
    def __init__(self, width=800, height=600):
        self.win = Window(width, height, self.stop)
        self.width = width
        self.height = height
        self.ball_size = width // 20
        self.ball = Ball(width//2, height//2, self.ball_size, self.win.canvas)
        self.left_rect = Rect(20, 20, 40, 20, 40, 160, 20, 160, self.win.canvas)
        self.left_rect = Rect(width-40, 20, width-20, 20, width-20, 160, width-40, 160, self.win.canvas)
        self.game_active = False
    
    def start(self):
        self.game_active = True
        self.win.active = True
        self.update()

    def update(self):
        x_speed = 5
        y_speed = 2
        while self.game_active:
            # check if the ball hits an edge and change the direction its heading
            
            if self.ball.x2 > self.width:
                x_speed = -x_speed
            elif self.ball.x1 < 1:
                x_speed = -x_speed
            if self.ball.y2 > self.height:
                y_speed = -y_speed
            elif self.ball.y1 < 1:
                y_speed = -y_speed
            
            self.ball.update_pos(x_speed, y_speed)
            self.win.redraw()
            sleep(1/60)

    def stop(self):
        self.game_active = False
        self.win.active = False

class Ball():
    def __init__(self, x1, y1, ball_size, canvas):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + ball_size
        self.y2 = y1 + ball_size
        self.circle_obj = Circle(self.x1, self.y1, self.x2, self.y2, self.canvas)