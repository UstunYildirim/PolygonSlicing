#!/usr/bin/python2

# Ustun Yildirim 11/10/18

from Drawing import Drawing
from Tkinter import *
from ttk import *

class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
        self.initDrawing()

    def initUI(self):
        self.parent.title("Polygon Slicing")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        self.fullscreen()
        self.initMenu()
        self.initCanvas()

    def initMenu(self):
        self.parent.option_add(self, '*tearOff', False)
        menubar = Menu(self.parent)
        menubar.add_command(label="Increase N", command=Drawing.incN)
        menubar.add_command(label="Decrease N", command=Drawing.decN)
        menubar.add_command(label="Dual", command=Drawing.dual)
        menubar.add_command(label="Exit", command=self.quit)
        self.parent.config(menu=menubar)

    def initCanvas(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.canvas = Canvas(self.parent, bg="white")
        self.canvas.pack()
        self.canvas.place(width=sw, height=sh, x=0,y=0)

    def initDrawing(self):
        Drawing.canvas = self.canvas
        Drawing.init()
    

    def fullscreen(self):
    	w = self.parent.winfo_screenwidth()
    	h = self.parent.winfo_screenheight()
    	self.parent.geometry('%dx%d+%d+%d' % (w, h, 0, 0))


def main():
    root = Tk()
    Window(root)
    root.mainloop()  

if __name__ == '__main__':
    main()
