from tkinter import *
from tkinter.ttk import *
import random

class VARIABLES:
    global WIDTH_BOX, CANT_BOXES, NAIL_FLOORS, NAIL_RAD, NUM_BALLS
    WIDTH_BOX = 40
    CANT_BOXES = 11
    NAIL_FLOORS = 11
    NAIL_RAD = 2.5
    NUM_BALLS = 50
    
    global WIDTH_WINDOW,HEIGHT_WINDOW
    WIDTH_WINDOW = WIDTH_BOX * CANT_BOXES
    HEIGHT_WINDOW = WIDTH_WINDOW* 3/2
    
    global BALL_RADIUS
    BALL_RADIUS = 5
    
    global REFRESH_TIME
    REFRESH_TIME = 5
    
    global WIDTH_CONT, HEIGHT_CONT
    WIDTH_CONT = WIDTH_WINDOW
    HEIGHT_CONT = HEIGHT_WINDOW * 3/5
    
class MAIN:
    def __init__ (self, master = None):
        self.master = master
        
        self.x = 0
        self.y = 1
        
        self.canvas = Canvas(width=WIDTH_WINDOW, height=HEIGHT_WINDOW)
        self.canvas['bg'] = 'black'

   
        self.canvas.pack()
        self.balls = []
        for _ in range(NUM_BALLS):
            ball = MAIN(self.canvas)
            self.balls.append(ball)

        self.drawDiv()
        self.drawNails()
        self.animate()
        
    def drawBall(self):
        self.ball = self.canvas.create_oval((WIDTH_WINDOW/2)-BALL_RADIUS,
                                            0,
                                            (WIDTH_WINDOW/2)+BALL_RADIUS,
                                            BALL_RADIUS*2,
                                            fill='green')
        
    def moveBall(self):
        self.canvas.move(self.ball, self.x, self.y)
        self.canvas.after(REFRESH_TIME,self.moveBall)
        
        for x in range(NAIL_FLOORS):
            if self.getCoords()[1] == HEIGHT_CONT/NAIL_FLOORS*x:
                DIRECTION = random.randint(0,1)
                if DIRECTION == 1:
                        self.x = .55
                else:
                    self.x = -.55
                    
                if self.getCoords()[0] < WIDTH_WINDOW and DIRECTION == 1:
                    self.x = .55
                elif self.getCoords()[0] >= WIDTH_WINDOW and DIRECTION == 1:
                    self.x = -.55
                elif self.getCoords()[0] > 0 and DIRECTION == 0:
                    self.x = -.55
                elif self.getCoords()[0] <= 0 and DIRECTION == 0:
                    self.x = .55
                    
        if self.getCoords()[1] >= HEIGHT_CONT:
            self.x = 0
        if self.getCoords()[1] >= HEIGHT_WINDOW-BALL_RADIUS*2:
            self.y = 0
        
    def drawDiv(self):
        self.division = self.canvas.create_line(0,
                                                HEIGHT_CONT,
                                                WIDTH_WINDOW,
                                                HEIGHT_CONT,
                                                fill='yellow')
        
        for x in range(CANT_BOXES):
            self.box = self.canvas.create_line(WIDTH_BOX * x,
                                               HEIGHT_CONT,
                                               WIDTH_BOX * x,
                                               HEIGHT_WINDOW,
                                               fill='orange')
        
    def drawNails(self):
        for i in range(1, NAIL_FLOORS, 2):
            for x in range(1, CANT_BOXES*2, 2):
                self.nail = self.canvas.create_oval(WIDTH_CONT/(CANT_BOXES*2) * x - NAIL_RAD,
                                                    (HEIGHT_CONT / NAIL_FLOORS) * i,
                                                    WIDTH_CONT/(CANT_BOXES*2) * x + NAIL_RAD,
                                                    (HEIGHT_CONT / NAIL_FLOORS) * i + NAIL_RAD*2,
                                                    fill='white')
        for i in range(2, NAIL_FLOORS, 2):  
            for x in range(0, CANT_BOXES*2, 2):
                self.nail = self.canvas.create_oval(WIDTH_CONT/(CANT_BOXES*2) * x - NAIL_RAD,
                                                    (HEIGHT_CONT / NAIL_FLOORS) * i,
                                                    WIDTH_CONT/(CANT_BOXES*2) * x + NAIL_RAD,
                                                    (HEIGHT_CONT / NAIL_FLOORS) * i + NAIL_RAD*2,
                                                    fill='white')
            
        
            # print([WIDTH_BOX*x - NAIL_RAD,HEIGHT_CONT / NAIL_FLOORS,WIDTH_BOX*x + NAIL_RAD,HEIGHT_CONT / NAIL_FLOORS + NAIL_RAD*2])
            
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
    
    def animate(self):
        for ball in self.balls:
            ball.()
        self.canvas.after(REFRESH_TIME, self.animate)
        
master = Tk()   
main = MAIN(master)     
mainloop()