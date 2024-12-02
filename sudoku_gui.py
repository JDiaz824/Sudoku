# Sudoku gui

import pygame, sys
from constants import *

# Sudoku Main Menu
def draw_game_start(screen):
    # Initialized title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    start_text = button_font.render("Start", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))

    # Initialize button background color and text
    start_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    start_surface.fill(LINE_COLOR)
    start_surface.blit(start_text, (10, 10))
    quit_surface = pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(start_text, (10, 10))

    # Initialize button rectangle
    start_rectangle = start_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 + 150))
    quit_rectangle = start_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(start_surface, start_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouse is on start button
                if start_rectangle.collidepoint(event.pos):
                    return # If the mouse is on start button, returns to main
                elif quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exits system
                    sys.exit()
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    screen.fill(BG_COLOR)

    draw_game_start(screen)

if __name__ == "__main__":
    main()


