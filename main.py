from tkinter import Tk, BOTH, Canvas
import time
def main():
    win = Window(800, 600)
    m = Maze(0,0,6,8,100,100,win)
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
        

    def draw_line(self, line, fill_color="black"):
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

    def draw(self, canvas, fill_color="black"):
        x1 = self.point_1.x
        y1 = self.point_1.y
        x2 = self.point_2.x
        y2 = self.point_2.y

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y1 = None
        self._win = win
    
    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        draw_color = "red"
        if undo:
            draw_color = "gray"
        start_center_x = self._x1 + ((self._x2 - self._x1) // 2)
        start_center_y = self._y1 + ((self._y2 - self._y1) // 2)
        dest_center_x = to_cell._x1 + ((to_cell._x2 - to_cell._x1) // 2)
        dest_center_y = to_cell._y1 + ((to_cell._y2 - to_cell._y1) // 2)
        line = Line(Point(start_center_x,start_center_y), Point(dest_center_x,dest_center_y))
        self._win.draw_line(line, draw_color)

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            cells =[]
            for j in range(self.num_rows):
                cells.append(Cell(self.win))
            self._cells.append(cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)


    def _draw_cell(self, i, j):
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, x2, y1, y2)

        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.05)
        

    

main()