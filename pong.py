from graphics import Window, Rect, Circle
from time import sleep
class Pong():
    def __init__(self, width=800, height=600):
        self.win = Window(width, height, self.stop, self.check_valid_imput)
        self.width = width
        self.height = height
        self.ball_size = 40
        self.ball = Circle(width//2, height//2, width//2 + self.ball_size, height//2 + self.ball_size, self.win.canvas)
        self.left_rect = Rect(20, 20, 40, 20, 40, 160, 20, 160, self.win.canvas)
        self.right_rect = Rect(width-30, 20, width-10, 20, width-10, 160, width-30, 160, self.win.canvas)
        self.left_rect_speed = 5
        self.right_rect_speed = -5
        self.circle_x_speed = -3
        self.circle_y_speed = -1
        self.game_active = False
    
    def start(self):
        self.game_active = True
        self.win.active = True
        self.update()

    # main game loop
    def update(self):
        while self.game_active:
            # check if the ball hits and edge
            if self.ball.x2 > self.width:
                self.circle_x_speed = 0
                self.circle_y_speed = 0
            elif self.ball.x1 < 8:
                self.circle_x_speed = 0
                self.circle_y_speed = 0
            if self.ball.y2 > self.height:
                self.circle_y_speed = -self.circle_y_speed
            elif self.ball.y1 < 8:
                self.circle_y_speed = -self.circle_y_speed
            self.ball.update_pos(self.circle_x_speed, self.circle_y_speed)
            
            # check if the ball intersects left rect
            if self.left_rect.x1 < self.ball.x1 < self.left_rect.x2 and self.ball.y2 > self.left_rect.y1 and self.ball.y1 < self.left_rect.y4:
                self.circle_x_speed = -self.circle_x_speed
            
            # check if the ball intersects right rect
            if self.right_rect.x1 < self.ball.x2 < self.right_rect.x2 and self.ball.y2 > self.right_rect.y1 and self.ball.y1 < self.right_rect.y4:
                self.circle_x_speed = -self.circle_x_speed
            
            # redraw and sleep to get 60fps
            self.win.redraw()
            sleep(1/60)
                

    def stop(self):
        self.game_active = False
        self.win.active = False
    
    def check_valid_imput(self, event):
        match event.char:
            case "w":
                self.left_rect_speed = -5
                if not self.left_rect.y1 < 5:
                    self.left_rect.update_pos(self.left_rect_speed)
            case "s":
                self.left_rect_speed = 5
                if not self.left_rect.y4 > self.height-5:
                    self.left_rect.update_pos(self.left_rect_speed)
            case "i":
                self.right_rect_speed = -5
                if not self.right_rect.y1 < 5:
                    self.right_rect.update_pos(self.right_rect_speed)
            case "k":
                self.right_rect_speed = 5
                if not self.right_rect.y4 > self.height-5:
                    self.right_rect.update_pos(self.right_rect_speed)