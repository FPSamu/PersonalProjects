from tkinter import *
from tkinter.ttk import *
import random

class VARIABLES_AND_CONSTS:
    global WIDTH_CANVAS, HEIGHT_CANVAS
    global BALL_SIZE
    global REFRESH_TIME
    global STEP_SIZE
    global STEP_SIZE
    global LEFT_TURN
    global RIGHT_TURN
    
    global BALL_START_X1
    global BALL_START_Y1
    global BALL_START_X2
    global BALL_START_Y2
    
    global ACTUAL_START_X1
    global ACTUAL_START_Y1
    global ACTUAL_START_X2
    global ACTUAL_START_Y2
    
    global BALL_POS_X
    global BALL_POS_Y
    
    global NUM_BOXES
    
    global NUM_NAILS_FLOORS
    
    global NAIL_DIAMETER
    global NAIL_X
    global NAIL_Y
    global NAIL_CENTER
    
    global DIRECTION
    
    global NUM_BALLS
    
    NUM_BOXES = 9
    NUM_NAILS_FLOORS = 15
    
    
    WIDTH_CANVAS = 500; HEIGHT_CANVAS = 500
    BALL_SIZE = 10    
    REFRESH_TIME =  15
    
    
    
    # STARTING BALL COORDS
    BALL_START_X1 = (WIDTH_CANVAS/2) - (BALL_SIZE/2)
    BALL_START_Y1 = 0
    BALL_START_X2 = (WIDTH_CANVAS/2) + (BALL_SIZE/2)
    BALL_START_Y2 = BALL_SIZE

    NAIL_DIAMETER = 5
    NAIL_X = WIDTH_CANVAS/(NUM_BOXES + 2)
    NAIL_Y = ((HEIGHT_CANVAS/4) * 3) / NUM_NAILS_FLOORS
    NAIL_CENTER = NAIL_DIAMETER / 2
        
    # STEP_SIZE_X = NAIL_Y/(NAIL_X*2)
    # STEP_SIZE_X = ((HEIGHT_CANVAS*(3/4))/NUM_NAILS_FLOORS) / ((WIDTH_CANVAS/NUM_BOXES)/2)
    
    SLOPE_Y = ((HEIGHT_CANVAS/25) * 24) - ((HEIGHT_CANVAS/4) * 3)
    SLOPE_X = (WIDTH_CANVAS/(NUM_BOXES + 2)) * (NUM_BOXES + 1)-(WIDTH_CANVAS/(NUM_BOXES + 2))
    
    STEP_SIZE = .4
    
    global  SLOPE
    SLOPE = SLOPE_Y / SLOPE_X
    
    
    LEFT_TURN = -SLOPE
    RIGHT_TURN = SLOPE
    
    
    NUM_BALLS = 50
        
class MAIN:

    def __init__ (self, master = None):
        self.master = master
        
        self.x = 0
        self.y = STEP_SIZE
        
        # CREATE WINDOW
        self.canvas = Canvas(width=WIDTH_CANVAS, height=HEIGHT_CANVAS)
        self.canvas['bg'] = 'black'
        
        self.drawBall()
        self.drawBox()
        self.drawNail()
        self.canvas.pack()
        self.moveBall()
        print(SLOPE)
    
    
    
    def drawBall(self):
        self.ball = self.canvas.create_oval(BALL_START_X1,
                                            BALL_START_Y1,
                                            BALL_START_X2,
                                            BALL_START_Y2,
                                            fill = 'green')
        
        
        
    def getCoords(self):
        # GET START AND FINAL X POSITION
        ACTUAL_BALL_X1 = self.canvas.coords(self.ball)[0]
        ACTUAL_BALL_X2 = self.canvas.coords(self.ball)[2]
        # GET START AND FINAL Y POSITION
        ACTUAL_BALL_Y1 = self.canvas.coords(self.ball)[1]
        ACTUAL_BALL_Y2 = self.canvas.coords(self.ball)[3]
        
        
        # REST FINAL POSITION MINUS HALF THE DIFERENCE WITH START TO FIND THE MID PART
        BALL_CENTER_X = ACTUAL_BALL_X2 - ((ACTUAL_BALL_X2 - ACTUAL_BALL_X1) / 2)
        BALL_CENTER_Y = ACTUAL_BALL_Y2 - ((ACTUAL_BALL_Y2 - ACTUAL_BALL_Y1) / 2)
        
        BALL_POS = [BALL_CENTER_X,BALL_CENTER_Y]
        
        return BALL_POS
    
    
        
    def moveBall(self):
        self.canvas.move(self.ball,self.x,self.y)
        self.canvas.after(REFRESH_TIME,self.moveBall)
        
        BORDER_RIGHT = (WIDTH_CANVAS/(NUM_BOXES + 2)) * (NUM_BOXES + 1)
        BORDER_LEFT = WIDTH_CANVAS/(NUM_BOXES + 2)
        
        
        
        for x in range(1, NUM_NAILS_FLOORS, 1):
            if round(self.getCoords()[1]) == round(NAIL_Y * x):
                self.y = STEP_SIZE
                
                DIRECTION = random.randint(0,1)
                # 1 FOR RIGHT
                # 0 FOR LEFT
                if DIRECTION == 1:
                    # IF TOUCHING THE RIGHT BORDER, BOUNCE TO LEFT
                    if self.getCoords()[0] < BORDER_RIGHT:
                        self.x = RIGHT_TURN
                    else:
                        self.x = LEFT_TURN
                else:
                    # IF TOUCHING THE LEFT BORDER, BOUNCE TO RIGHT
                    if self.getCoords()[0] > BORDER_LEFT:
                        self.x = LEFT_TURN
                    else:
                        self.x = RIGHT_TURN
                    
            if self.getCoords()[1] >= (HEIGHT_CANVAS/4) * 3:
                self.x = 0
            if  round(self.getCoords()[1]) == (HEIGHT_CANVAS/25) * 24:
                self.y = 0        
        
        
    def drawBox(self):
        
        # NUM_BOXES += 2 TO ELIMINATE LEFT AND RIGHT BORDER
        # REST 1 TO NUM_BOXES TO STOP BEFORE RIGHT BORDER
        CONT_X1 = WIDTH_CANVAS/(NUM_BOXES + 2)
        CONT_X2 = (WIDTH_CANVAS/(NUM_BOXES + 2)) * (NUM_BOXES + 1)
        CONT_Y1 = (HEIGHT_CANVAS/4) * 3
        CONT_Y2 = (HEIGHT_CANVAS/25) * 24
        self.container = self.canvas.create_rectangle(CONT_X1,
                                                      CONT_Y1,
                                                      CONT_X2,
                                                      CONT_Y2,
                                                      outline='white')
        
        
        
        SEPARATOR_Y2 = CONT_Y2
        SEPARATOR_Y1 = CONT_Y1
        for i in range(2, NUM_BOXES+1, 1):
            SEPARATOR_X = (WIDTH_CANVAS/(NUM_BOXES + 2)) * i
            self.separation = self.canvas.create_line(SEPARATOR_X,
                                                      SEPARATOR_Y1,
                                                      SEPARATOR_X,
                                                      SEPARATOR_Y2,
                                                      fill='white')
        
            
        self.border_left = self.canvas.create_line(CONT_X1,
                                                   0,
                                                   CONT_X1,
                                                   CONT_Y2,
                                                   fill='red')
        
        self.border_right = self.canvas.create_line(CONT_X2,
                                                    0,
                                                    CONT_X2,
                                                    CONT_Y2,
                                                    fill='red')
        
        
    
    def drawNail(self):
        # THIS IS WHEN THE NAILS ARE IN THE MIDDLE OF THE BOXES
        for i in range(1, NUM_NAILS_FLOORS, 2):
            for x in range(3,(NUM_BOXES*2) + 2, 2):
                self.nail = self.canvas.create_oval(((NAIL_X * x) / 2) - NAIL_CENTER,
                                                    (NAIL_Y * i) - NAIL_CENTER,
                                                    ((NAIL_X * x) / 2) + NAIL_CENTER,
                                                    (NAIL_Y * i) + NAIL_CENTER,
                                                    fill='white')
            
        
        # THIS IS WHEN THE NAILS ARE IN THE BOXES' COORDS DIRECTION
        for i in range(2, NUM_NAILS_FLOORS, 2):
            for x in range(2,NUM_BOXES+1, 1):
                self.nail = self.canvas.create_oval((NAIL_X * x) - NAIL_CENTER,
                                                    (NAIL_Y * i) - NAIL_CENTER,
                                                    (NAIL_X * x) + NAIL_CENTER,
                                                    (NAIL_Y * i) + NAIL_CENTER,
                                                    fill='white')
            
        
        
        
        
master = Tk()   
main = MAIN(master)     
mainloop()