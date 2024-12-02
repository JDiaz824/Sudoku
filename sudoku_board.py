from constants import *
import pygame
import math
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen

        removedCells = [EASY, MEDIUM, HARD]
        self.board = SudokuGenerator(9, removedCells[difficulty])

        self.board = SudokuGenerator.get_board()
        self.original_board = SudokuGenerator.get_board()
        self.selected_cell = (0, 0)

    def draw(self):
        #pygame drawing to do after logic
        pass

    def select(self, row, col):
        self.selected_cell = (row, col)
        #im assuming redraw the cell with a red outline here?

    def click(self, y, x):
        cell_width = WIDTH/9
        row = int(math.floor(x/cell_width))
        col = int(math.floor(y/cell_width))
        if (row <= 8 & col <= 8):
            return (row, col)
        else:
            return None
        
    def clear(self):
        row = self.selected_cell[0]
        col = self.selected_cell[1]

        if (self.original_board[row][col].value == 0):
            self.board[row][col].set_cell_value(0)

    def sketch(self, value):
        row = self.selected_cell[0]
        col = self.selected_cell[1]
        if (self.original_board[row][col].value == 0):
            self.board[row][col].set_sketched_value(value)

    def place_number(self, value):
        row = self.selected_cell[0]
        col = self.selected_cell[1]
        if (self.original_board[row][col].value == 0):
            self.board[row][col].set_cell_value(value)

    def reset_to_original(self):
        self.board = SudokuGenerator.get_board()
    
    def is_full(self):
        isFull = True
        for row in self.board:
            for cell in row:
                if cell.value == 0:
                    isFull = False
        return isFull
    
    def find_empty(self):
        row = 0
        for row in self.board:
            col = 0
            for cell in row:
                if cell.value == 0:
                    return (row, col)
                col += 1
            row += 1



        

    