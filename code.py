import simplegui

class Circle:
    def __init__(self):
        self.center_point = (250,250)
        self.radius = 20

class ShapeAttribute:
    def __init__(self):
        self.line_width = 1
        self.line_color = "Blue"
        self.fill_color = "Black"
        
    def update_x(self, shift_x):
        self.center_point = (
            self.center_point[0] + shift_x,
            self.center_point[1] )
    def update_y(self, shift_y):
        self.center_point = (
        self.center_point[0] + shift_y, 
        self.center_point[1] )
class Cliq:
    key_map = {
            "right":39,
            "left":37,
            "up": 38,
            "down": 40
        
            }
    
    def __init__(self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttribute()
        self.move_dist = 10
    def draw_me(self, canvas):
        canvas.draw_circle(
            self.circle_shape.center_point,
            self.circle_shape.radius,
            self.shape_attributes.line_width,
            self.shape_attributes.line_color,
            self.shape_attributes.fill_color
        )
    def move(self, key):
        print key
cliq = Cliq()

def draw(canvas):
    cliq.draw_me(canvas)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(cliq.move)

# Start the frame animation
frame.start()
