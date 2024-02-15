from tkinter import Tk, BOTH, Canvas
from maze import Maze
from window import Window, Line, Cell, Point

def main():
    win = Window(800, 600)
    m = Maze(0,0,6,8,100,100,win)
    win.wait_for_close()

    
    

main()