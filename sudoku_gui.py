# Sudoku gui

import pygame, sys
from constants import *

# Sudoku Main Menu
def draw_game_start(screen):
    # Initialized title font
    start_title_font = pygame.font.Font(None, 80)
    select_mode_font = pygame.font.Font(None, 65)
    button_font = pygame.font.Font(None, 40)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku!", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw select_mode button
    select_mode_surface = select_mode_font.render("Select Game Mode:", 0, LINE_COLOR)
    select_mode_rectangle = select_mode_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(select_mode_surface, select_mode_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 125, HEIGHT // 2 + 125))

    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2 , HEIGHT // 2 + 125))

    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 125, HEIGHT // 2 + 125))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouse is on easy button
                if easy_rectangle.collidepoint(event.pos):
                    return # If the mouse is on easy button, returns to main
                elif medium_rectangle.collidepoint(event.pos):
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    return
        pygame.display.update()

def draw_game_won(screen):
    # Initialized title font
    win_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = win_title_font.render("Game Won!", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    exit_text = button_font.render("Exit", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))

    # Initialize button background color and text
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    exit_rectangle = exit_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouse is on exit button
                if exit_rectangle.collidepoint(event.pos):
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


