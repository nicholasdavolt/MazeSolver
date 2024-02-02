from tkinter import Tk, BOTH, Canvas
import time
def main():
    win = Window(800, 600)
    p1 = Point(0,0)
    p2 = Point(800, 600)
    line1 = Line(p1, p2)
    line2 = Line(Point(0, 600), Point(800, 0))

    win.draw_line(line1,"red")
    win.draw_line(line2,"red")
    win.wait_for_close()
    

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "MAZE SOLVER"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg="white", height=self.height, width=self.width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.point_1 = p1
        self.point_2 = p2

    def draw(self, canvas, fill_color):
        x1 = self.point_1.x
        y1 = self.point_1.y
        x2 = self.point_2.x
        y2 = self.point_2.y

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)
        
main()