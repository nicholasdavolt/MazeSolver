
from maze import Maze
from window import Window, Line, Cell, Point

def main():
    win = Window(800, 600)
    m = Maze(10,10,5,7,100,100,win)
    win.wait_for_close()

    
    

main()