import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketeched_value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value
    
    def set_sketched_value(self, value):
        self.sketeched_value = value

    def draw(self):
        cell_color = "black"
        if self.selected:
            cell_color = "red"
        pygame.draw.rect(self.screen, cell_color, ((self.row*70, self.col*70), (self.row*70 + 70, self.col*70 + 70)), 1)
        if self.value != 0:
            number_font = pygame.font.Font(None, 40)
            number_surface = number_font.render(str(self.value), 0, "Black")
            number_rectangle = number_surface.get_rect(
                center=(self.row*70 + 70/2, self.col*70 + 70/2))
            self.screen.blit(number_surface, number_rectangle)