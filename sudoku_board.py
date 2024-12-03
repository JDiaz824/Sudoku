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
        self.completed_board = SudokuGenerator(removedCells[difficulty], 9)
        self.original_board = self.completedBoard.get_board()
        self.completed_board.fill_values()

        self.playing_board = []
        for row in range(width):
            self.playing_board.append([])
            for col in range(height):
                cell = Cell(self.original_boardboard[row][col], row, col, self.screen)
                self.playing_board[row].append(cell)

        self.selected_cell = self.playing_board[0][0]

    def draw(self):
        #pygame drawing to do after logic
        pass

    def select(self, row, col):
        self.selected_cell = self.playing_board[0][0]
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
        row = self.selected_cell.row
        col = self.selected_cell.col

        if (self.original_board[row][col] == 0):
            self.playing_board[row][col].set_cell_value(0)

    def sketch(self, value):
        row = self.selected_cell.row
        col = self.selected_cell.col
        if (self.original_board[row][col] == 0):
            self.playing_board[row][col].set_sketched_value(value)

    def place_number(self, value):
        row = self.selected_cell.row
        col = self.selected_cell.col
        if (self.original_board[row][col] == 0):
            self.playing_board[row][col].set_cell_value(value)

    def reset_to_original(self):
        for row in range(len(self.playing_board)):
            for col in range(len(self.playing_board[row])):
                self.playing_board[row][col].set_cell_value(self.original_board[row][col])
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

        

    