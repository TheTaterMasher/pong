from graphics import Window, Rect, Circle
from time import sleep
class Pong():
    def __init__(self, width=800, height=600):
        self.win = Window(width, height, self.stop)
        self.width = width
        self.height = height
        self.ball_size = 40
        self.ball = Circle(width//2, height//2, width//2 + self.ball_size, height//2 + self.ball_size, self.win.canvas)
        self.left_rect = Rect(20, 20, 40, 20, 40, 160, 20, 160, self.win.canvas)
        self.right_rect = Rect(width-30, 20, width-10, 20, width-10, 160, width-30, 160, self.win.canvas)
        self.game_active = False
    
    def start(self):
        self.game_active = True
        self.win.active = True
        self.update()

    # main game loop
    def update(self):
        left_rect_speed = 5
        right_rect_speed = -5
        circle_x_speed = 4
        circle_y_speed = 2
        while self.game_active:
            # check if the ball hits and edge
            if self.ball.x2 > self.width:
                circle_x_speed = 0
                circle_y_speed = 0
            elif self.ball.x1 < 8:
                circle_x_speed = 0
                circle_y_speed = 0
            if self.ball.y2 > self.height:
                circle_y_speed = -circle_y_speed
            elif self.ball.y1 < 8:
                circle_y_speed = -circle_y_speed
            self.ball.update_pos(circle_x_speed, circle_y_speed)
            
            # check if the ball intersects left rect
            if self.left_rect.x1 < self.ball.x1 < self.left_rect.x2 and self.ball.y2 > self.left_rect.y1 and self.ball.y1 < self.left_rect.y4:
                circle_x_speed = -circle_x_speed
            
            # check if the ball intersects right rect
            if self.right_rect.x1 < self.ball.x2 < self.right_rect.x2 and self.ball.y2 > self.right_rect.y1 and self.ball.y1 < self.right_rect.y4:
                circle_x_speed = -circle_x_speed

            # move the rects / change to get user input to move the rects
            if self.left_rect.y4 > self.height:
                left_rect_speed = -5
            elif self.left_rect.y1 < 0:
                left_rect_speed = 5
            if self.right_rect.y4 > self.height:
                right_rect_speed = -5
            elif self.right_rect.y1 < 0:
                right_rect_speed = 5
            self.left_rect.update_pos(left_rect_speed)
            self.right_rect.update_pos(right_rect_speed)
            
            # redraw and sleep to get 60fps
            self.win.redraw()
            sleep(1/60)

    def stop(self):
        self.game_active = False
        self.win.active = False