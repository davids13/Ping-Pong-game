# Bounce Ball Game

from tkinter import *
import random
import time

# creating the ball
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        # changing the balls direction
        starts =[-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)# here we mix up the list by calling random.shuffle
        self.x = starts[0]# here set the value of x to the first item in the list, so that x can be any number in te list, from -3 to 3
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        '''
        # making the ball bounce
        self.x = 0
        self.y = -1 
        self.canvas_height = self.canvas.winfo_height() # this function return the next current height of the canvas
        '''

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    # adding some action - making the ball move
    def draw(self):
        self.canvas.move(self.id, self.x, self.y) # we change the call to the canvas move func by passing the object var x and y
        pos = self.canvas.coords(self.id) # we created a var called pos, by calling the canvas function coords, this returns the current x and y coordinates of anything drawn on the canvas as long as you know its identify number. in ths case we pass coords the ogbject var id, wich contains the oval´s identifier
        if pos[1] <= 0: # is less ha nor equal to 0 so if so we set the y object var to 1( we are saying if you hit the top of screen, stop subtractting one from the vertical position, and therefore stop moving up)
            self.y = 3
        if pos[3] >= self.canvas_height: # (bottom ball) is greater than or equal to the var canvas_height, if it is we set the y object var back to -1
            self.hit_bottom = True
        if self.hit_paddle(pos) == True: 
            self.y = -3 
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

# adding the paddle
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        # making the paddle move
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        # event, call the function when programming is still run
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        # pass

    # changing the direction
    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2
    
# create the canvas
tk = Tk()
tk.title('Game')
tk.resizable(0, 0) # window cannot be changed either horizontally or vertically
tk.wm_attributes('-topmost', 1) #  tell tkinter to place the window containingour canvas in front of all the others windowa ('-topmost')
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0) # bd=0 and ightlightthickness=0) make sure that there´s no border around the outside of the canvas  
canvas.pack() # tells the canvas to size itself according to the width and height parameters given in preceding line
tk.update() # tells tkinter to o«initialize itself for the animation in our game

# create an object of the Paddle class
paddle = Paddle(canvas, 'blue')

# create an object of the Ball class
ball = Ball(canvas, paddle, 'red')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)



