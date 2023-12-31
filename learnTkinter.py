from tkinter import *
from tkinter.ttk import *

class GFG:
    def __init__ (self, master = None):
        self.master = master
        
        # COORDENADAS INICIALES
        self.x = 1
        self.y = 0
        
        # CREAR FIGURA
        # self.canvas = Canvas(master)
        self.canvas = Canvas(master)
        
        # CREAR RECTANGULO
        self.rectangle = self.canvas.create_rectangle(5,5,25,25, fill = 'white')
        self.canvas.pack()

        # COLOR FONDO
        self.canvas['bg'] = 'black'
        
        # LLAMADA A FUNCION MOVIMIENTO
        self.movimiento()
        
    def movimiento(self):
        # MOVER FIGURA
        self.canvas.move(self.rectangle, self.x, self.y)
        self.canvas.after(100, self.movimiento)
        
    # MOVIMIENTO A LA IZQUIERDA
    def izquierda(self, event):
        print(event.keysym)
        self.x = -5
        self.y = 0
        
    # MOVIMIENTO A LA DERECJA
    def derecha(self, event):
        print(event.keysym)
        self.x = 5
        self.y = 0
        
    # MOVIMIENTO HACIA ARRIBA
    def arriba(self, event):
        print(event.keysym)
        self.x = 0
        self.y = -5
        
    # MOVIMIENTO HACIA ABAJO
    def abajo(self, event):
        print(event.keysym)
        self.x = 0
        self.y = 5

if __name__ == '__main__':
    # MOSTRAR VENTANA
    master = Tk()
    # gfg = GFG(master)
    gfg = GFG(master)
    
    # CONTROLAR MOVIMIENTO POR TECLADO
    master.bind('<KeyPress-Left>', lambda e: gfg.izquierda(e))
    master.bind('<KeyPress-Right>', lambda e: gfg.derecha(e))
    master.bind('<KeyPress-Up>', lambda e: gfg.arriba(e))
    master.bind('<KeyPress-Down>', lambda e: gfg.abajo(e))
    mainloop()