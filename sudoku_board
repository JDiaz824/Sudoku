import pygame
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = SudokuGenerator.get_board()
        self.original_board = SudokuGenerator.get_board()
        self.selected_cell = None

    def draw(self):
        #pygame drawing to do after logic
        pass

    def select(self, row, col):
        self.selected_cell = self.board[row][col]
        #im assuming redraw the cell with a red outline here?

    def click(self, row, col):
        self.selected_cell = self.board[row][col]
        #im assuming redraw the cell with a red outline here?

    