from window import Window, Line, Cell, Point
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if self.seed is not None:
            random.seed(self.seed)
        self._create_cells()
        self._break_enterance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        


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
        if self.win is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, x2, y1, y2)

        self._animate()

    def _break_enterance_and_exit(self):
        last_cell_col = len(self._cells) - 1
        last_cell_row = len(self._cells[last_cell_col]) - 1
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[last_cell_col][last_cell_row].has_bottom_wall = False
        self._draw_cell(last_cell_col, last_cell_row)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            dir_list = []
            if i > 0 and not self._cells[i - 1][j].visited:
                dir_list.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                dir_list.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                dir_list.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                dir_list.append((i, j + 1))

            if len(dir_list) == 0:
                self._draw_cell(i,j)
                return
            
            new_dir_i, new_dir_j = dir_list[random.randrange(len(dir_list))]

            if new_dir_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if new_dir_i == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if new_dir_j == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if new_dir_j == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            self._break_walls_r(new_dir_i, new_dir_j)
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
           
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i - 1][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i + 1][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j - 1].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j + 1].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        
        return False


            

            
            






    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(.05)
 