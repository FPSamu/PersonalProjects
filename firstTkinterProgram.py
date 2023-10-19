from tkinter import *
from tkinter.ttk import *

class GFG:


    # GLOBAL CONSTANTS
    global WIDTH_CANVAS
    global HEIGHT_CANVAS
    global BALL_SIZE
    global REFRESH_TIME
    global STEP_SIZE
    
    # ASSIGN GLOBAL CONSTANTS A VALUE
    WIDTH_CANVAS = 1280; HEIGHT_CANVAS = 720    # CANVAS SIZE
    BALL_SIZE = 10                              # BALL SIZE
    REFRESH_TIME = 10                           # REFRESH RATE
    STEP_SIZE = 5                             # STEPS SIZE
    
    def __init__ (self, master = None):
        self.master = master
        
        # MOVEMENT IN X AXIS
        self.x = STEP_SIZE
        # MOVEMENT IN Y AXIS
        self.y = STEP_SIZE
        
        # CREATE CANVAS
        self.canvas = Canvas(width=WIDTH_CANVAS, height=HEIGHT_CANVAS)
        self.canvas['bg'] = 'black'
        
        
        # CREATE BALL
        # BALL START POSITION
        BALL_START_X1 = (WIDTH_CANVAS/2) - (BALL_SIZE/2)
        BALL_START_Y1 = 0
        BALL_START_X2 = (WIDTH_CANVAS/2) + (BALL_SIZE/2)
        BALL_START_Y2 = BALL_SIZE
        
        self.ball = self.canvas.create_oval(BALL_START_X1,
                                            BALL_START_Y1,
                                            BALL_START_X2,
                                            BALL_START_Y2,
                                            fill = 'white')
        self.canvas.pack()
        
        
        # CREATE BOXES
        # MAIN CONTAINER COORDS
        CONT_X1 = WIDTH_CANVAS/5
        CONT_Y1 = (HEIGHT_CANVAS/3) *2
        CONT_X2 = (WIDTH_CANVAS/5) * 4
        CONT_Y2 = (HEIGHT_CANVAS/25) * 24
        # DRAW MAIN CONTAINER
        self.container = self.canvas.create_rectangle(CONT_X1,
                                                      CONT_Y1,
                                                      CONT_X2,
                                                      CONT_Y2,
                                                      outline='white')
        
        # CREATE BOXES
        BOX_X1_X2 = (WIDTH_CANVAS/10) * 3
        BOX_Y1 = (HEIGHT_CANVAS/3) *2
        BOX_Y2 = (HEIGHT_CANVAS/25) * 24
        # DRAW BOXES DIVISIONS
        for x in range(4,9,1):
            self.box = self.canvas.create_line(BOX_X1_X2,
                                               BOX_Y1,
                                               BOX_X1_X2,
                                               BOX_Y2,
                                               fill='white')
            BOX_X1_X2 = (WIDTH_CANVAS/10 * x)
        
        
        # AUTOMOVE FUNCTION CALL
        self.mainMovement()
    
    
    
    # GET BALL CORDS
    def getBallPosition(self):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        return (x1, y1, x2, y2)

    
    
    # AUTOMOVE FUNCTION
    def mainMovement(self):
        self.canvas.move(self.ball, self.x, self.y)
        self.canvas.after(REFRESH_TIME,self.mainMovement)
        
        
        
        # CHECK IF THE BALL IS IN THE BOX
        ball_position = ((self.canvas.coords(self.ball)[3])-(self.canvas.coords(self.ball)[1]))/2
        ball_position += self.canvas.coords(self.ball)[1]
        if ball_position == HEIGHT_CANVAS/2:
            self.x = 0
            self