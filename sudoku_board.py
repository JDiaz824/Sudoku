from constants import *
import pygame
import math
from sudoku_generator import SudokuGenerator
from sudoku_cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen

        removedCells = [EASY, MEDIUM, HARD]
        #creating the board, gathering the answered sudoku
        self.original_board = SudokuGenerator(removedCells[difficulty], 9)
        self.original_board.fill_values()
        self.completed_board = self.original_board.get_board()
        self.original_board.remove_cells()
        self.original_board.print_board()

        self.playing_board = []
        for row in range(width):
            self.playing_board.append([])
            for col in range(height):
                cell = Cell(self.original_board.get_board()[row][col], row, col, self.screen)
                self.playing_board[row].append(cell)

        self.selected_cell = self.playing_board[0][0]

    def draw(self):
        pygame.draw.rect(self.screen, "white", ((0, 0), (630, 630)), 0)
        for r in range(210, 631, 210):
            pygame.draw.line(self.screen, "black", (0, r), (630, r), 5)
        for c in range(210, 630, 210):
            pygame.draw.line(self.screen, "black", (c, 0), (c, 630), 5)
        for row in range(len(self.playing_board)):
            for col in range(len(self.playing_board[row])):
                self.playing_board[row][col].draw()

    def select(self, row, col):
        if (self.original_board.get_board()[row][col] == 0):
            self.selected_cell.selected = False
            self.selected_cell = self.playing_board[row][col]
            self.selected_cell.selected = True
        #im assuming redraw the cell with a red outline here?

    def click(self, x, y):
        cell_width = WIDTH/9
        row = int(math.floor(y/cell_width))
        col = int(math.floor(x/cell_width))
        if (row <= 8 and col <= 8):
            return (row, col)
        else:
            return None
        
    def clear(self):
        row = self.selected_cell.row
        col = self.selected_cell.col

        if (self.original_board.get_board()[row][col] == 0):
            self.playing_board[row][col].set_cell_value(0)
            self.playing_board[row][col].set_sketched_value(0)

    def sketch(self, value):
        row = self.selected_cell.row
        col = self.selected_cell.col
        if (self.original_board.get_board()[row][col] == 0):
            self.playing_board[row][col].set_sketched_value(value)

    def place_number(self, value):
        row = self.selected_cell.row
        col = self.selected_cell.col
        if (self.original_board.get_board()[row][col] == 0):
            self.playing_board[row][col].set_cell_value(value)
            self.playing_board[row][col].set_sketched_value(0)

    def reset_to_original(self):
        for row in range(len(self.playing_board)):
            for col in range(len(self.playing_board[row])):
                self.playing_board[row][col].set_cell_value(self.original_board.get_board()[row][col])
                self.playing_board[row][col].set_sketched_value(0)
    
    def is_full(self):
        for row in range(len(self.playing_board)):
            for col in range(len(self.playing_board[row])):
                if self.playing_board[row][col].value == 0:
                    return False
                
        return True
    
    def find_empty(self):
        for row in range(len(self.playing_board)):
            for col in range(len(self.playing_board[row])):
                if self.playing_board[row][col].value == 0:
                    return (row, col)
        return None
    
    def check_board(self):
        for row in range(len(self.playing_board)):
            for col in range(len(self.playing_board[row])):
                if self.playing_board[row][col].value != self.completed_board[row][col]:
                    return False
        return True