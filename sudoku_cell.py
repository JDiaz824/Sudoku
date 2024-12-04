import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketeched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value
    
    def set_sketched_value(self, value):
        self.sketeched_value = value

    def draw(self):
        cell_width = 1
        cell_color = "black"
        if self.selected:
            cell_color = "red"
            cell_width = 3
        square = pygame.Rect(self.col*70, self.row*70, 70, 70)
        pygame.draw.rect(self.screen, cell_color, square, cell_width)

        if self.value != 0:
            number_font = pygame.font.Font(None, 60)
            number_surface = number_font.render(str(self.value), 0, "Black")
            number_rectangle = number_surface.get_rect(
                center=(self.col*70 + 70/2, self.row*70 + 70/2))
            self.screen.blit(number_surface, number_rectangle)

        if (self.sketeched_value != 0):
            number_font = pygame.font.Font(None, 50)
            number_surface = number_font.render(str(self.sketeched_value), 0, (128, 128, 128))
            number_rectangle = number_surface.get_rect(
                center=(self.col * 70 + 15, self.row * 70 + 20))
            self.screen.blit(number_surface, number_rectangle)