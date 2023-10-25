from tkinter import *
from tkinter.ttk import *
import random

class VARIABLES_AND_CONSTS:
    # CREATE WINDOW
    global WIDTH_WINDOW, HEIGHT_WINDOW, BALL_SIZE, REFRESH_TIME, STEP_SIZE, LEFT_TURN, RIGHT_TURN
    WIDTH_WINDOW = 500
    HEIGHT_WINDOW = 500
    
    # CREATE MACHINE CONTAINER
    global WIDTH_MACHINE, HEIGHT_MACHINE, CENTER_MACHINE, START_POS_X_MACHINE, START_POS_Y_MACHINE, END_POS_X_MACHINE, END_POS_Y_MACHINE
    WIDTH_MACHINE = WIDTH_WINDOW * 6/7
    HEIGHT_MACHINE = HEIGHT_WINDOW * 19/20
    CENTER_MACHINE = WIDTH_WINDOW / 2
    START_POS_X_MACHINE = CENTER_MACHINE - (WIDTH_MACHINE/2)
    START_POS_Y_MACHINE = 0
    END_POS_X_MACHINE = CENTER_MACHINE + (WIDTH_MACHINE/2)
    END_POS_Y_MACHINE = HEIGHT_MACHINE
    
    # CREATE BOXES
    global START_POS_X_BOX, START_POS_Y_BOX, END_POS_X_BOX, END_POS_Y_BOX, NUM_BOXES, WIDTH_BOXES
    NUM_BOXES = 7
    START_POS_X_BOX = START_POS_X_MACHINE
    START_POS_Y_BOX = HEIGHT_MACHINE * 3/4
    END_POS_X_BOX = START_POS_X_BOX + (WIDTH_MACHINE/NUM_BOXES)
    END_POS_Y_BOX = HEIGHT_MACHINE
    WIDTH_BOXES = END_POS_X_BOX - START_POS_X_BOX
    
    # CREATE BALL
    global BALL_START_POS_X1,BALL_START_POS_Y1,BALL_START_POS_X2,BALL_START_POS_Y2,BALL_DIAMETER
    BALL_DIAMETER = 10
    # FIRST COORD
    BALL_START_POS_X1 = CENTER_MACHINE - (BALL_DIAMETER/2)
    BALL_START_POS_Y1 = 0
    # SECOND COORD
    BALL_START_POS_X2 = CENTER_MACHINE + (BALL_DIAMETER/2)
    BALL_START_POS_Y2 = BALL_DIAMETER
    
    # CREATE NAILS
    global NAIL_START_POS_X1, NAIL_START_POS_X2, NAIL_START_POS_Y1, NAIL_START_POS_Y2, NAIL_DIAMETER, NAIL_FLOORS, HEIGHT_FLOORS, BOUNCE_AREA, NAILS_MAP
    BOUNCE_AREA = (START_POS_Y_BOX) - HEIGHT_MACHINE
    NAIL_FLOORS = 11
    NAIL_DIAMETER = 5
    NAIL_START_POS_X1 = (START_POS_X_MACHINE+WIDTH_BOXES/2) - NAIL_DIAMETER/2
    NAIL_START_POS_Y1 = START_POS_Y_BOX/NAIL_FLOORS - NAIL_DIAMETER/2
    NAIL_START_POS_X2 = (START_POS_X_MACHINE+WIDTH_BOXES/2) + NAIL_DIAMETER/2
    NAIL_START_POS_Y2 = START_POS_Y_BOX/NAIL_FLOORS + NAIL_DIAMETER/2
    NAIL_CENTER = (NAIL_START_POS_Y2-NAIL_START_POS_Y1) / (NAIL_START_POS_X2-NAIL_START_POS_X1)
    HEIGHT_FLOORS = HEIGHT_MACHINE/NAIL_FLOORS
    NAILS_MAP = []
    
    # BALL MOVEMENT
    global STEP_Y, STEP_X, REFRES_TIME, SLOPE, X,Y
    REFRESH_TIME = 10
    STEP_Y = .7
    
    
class MAIN:
    def __init__ (self, master = None):
        self.master = master
        
        # CREATE CANVAS
        self.canvas = Canvas(width=WIDTH_WINDOW, height=HEIGHT_WINDOW)
        self.canvas['bg'] = 'black'
        
        self.x = 0
        self.y = STEP_Y
        
        self.drawBox()
        self.drawBall()
        self.drawNails()
        self.moveBall()
        self.canvas.pack()
        
        
    def drawBall(self):
        self.ball = self.canvas.create_oval(BALL_START_POS_X1,
                                BALL_START_POS_Y1,
                                BALL_START_POS_X2,
                                BALL_START_POS_Y2,
                                fill='green')
        
    def drawBox(self):
        for i in range(NUM_BOXES):
            self.canvas.create_rectangle(START_POS_X_BOX + (WIDTH_BOXES*i),
                                         START_POS_Y_BOX,
                                         END_POS_X_BOX + (WIDTH_BOXES*i),
                                         END_POS_Y_BOX,
                                         outline='white')
        
        self.canvas.create_rectangle(START_POS_X_MACHINE, 
                                     START_POS_Y_MACHINE, 
                                     END_POS_X_MACHINE,
                                     END_POS_Y_MACHINE, 
                                     outline='yellow')
        
    def moveBall(self):
        self.canvas.move(self.ball,self.x,self.y)
        self.canvas.after(REFRESH_TIME,self.moveBall)
        
        X = NAILS_MAP[-1][0] - NAILS_MAP[0][0]
        Y = NAILS_MAP[-1][1] - NAILS_MAP[0][1]
        SLOPE = Y/X
        
        flag = False
        if int(self.getCoords()[1]) > int(START_POS_Y_BOX):
            flag = True
            self.x = 0
        if int(self.getCoords()[1]) == int(END_POS_Y_BOX):
            flag = True
            self.y = 0
        
        if flag == False:
            for x in range(NAIL_FLOORS):
                DIRECTION = random.randint(0,1)
                # IF 0 GO LEFT, IF 1 GO RIGHT
                if int(self.getCoords()[1]) == int(NAIL_START_POS_Y1*x):
                    if DIRECTION == 0:
                        if int(self.getCoords()[0]) < int(END_POS_X_MACHINE):
                            self.x = -SLOPE
                        else:
                            self.x = SLOPE
                    else:
                        if int(self.getCoords()[0]) > int(START_POS_X_MACHINE):
                            self.x = SLOPE
                        else:        
                            self.x = -SLOPE
                        
                        
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
        
    def getCoordsNails(self):
        # GET START AND FINAL X POSITION
        ACTUAL_NAIL_X1 = self.canvas.coords(self.nail)[0]
        ACTUAL_NAIL_X2 = self.canvas.coords(self.nail)[2]
        # GET START AND FINAL Y POSITION
        ACTUAL_NAIL_Y1 = self.canvas.coords(self.nail)[1]
        ACTUAL_NAIL_Y2 = self.canvas.coords(self.nail)[3]
        
        
        # REST FINAL POSITION MINUS HALF THE DIFERENCE WITH START TO FIND THE MID PART
        NAIL_X = ACTUAL_NAIL_X2 - ((ACTUAL_NAIL_X2 - ACTUAL_NAIL_X1) / 2)
        NAIL_Y = ACTUAL_NAIL_Y2 - ((ACTUAL_NAIL_Y2 - ACTUAL_NAIL_Y1) / 2)
        
        NAIL_POS = [int(NAIL_X),int(NAIL_Y)]
        
        return NAIL_POS
        
    def drawNails(self):
        for x in range(0, NAIL_FLOORS-1, 2):
            for i in range(0, NUM_BOXES*2, 2):
                self.nail = self.canvas.create_oval(NAIL_START_POS_X1 + WIDTH_BOXES/2*i,
                                                        NAIL_START_POS_Y1 + NAIL_START_POS_Y1*x,
                                                        NAIL_START_POS_X2 + WIDTH_BOXES/2*i,
                                                        NAIL_START_POS_Y2 + NAIL_START_POS_Y1*x,
                                                        fill='white')
                NAILS_MAP.append(self.getCoordsNails())
                
        for x in range(1, NAIL_FLOORS-1, 2):
            for i in range(1, (NUM_BOXES*2)-1, 2):
                self.nail = self.canvas.create_oval(NAIL_START_POS_X1 + WIDTH_BOXES/2*i,
                                                        NAIL_START_POS_Y1 + NAIL_START_POS_Y1*x,
                                                        NAIL_START_POS_X2 + WIDTH_BOXES/2*i,
                                                        NAIL_START_POS_Y2 + NAIL_START_POS_Y1*x,
                                                        fill='orange')
                NAILS_MAP.append(self.getCoordsNails())
                
        
        
master = Tk()   
main = MAIN(master)     
mainloop()