# Sudoku gui

import pygame, sys
from sudoku_board import Board
from constants import *

playing_board = None

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
        global playing_board
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouse is on easy button
                if easy_rectangle.collidepoint(event.pos):
                    playing_board = Board(9, 9, screen, 0)
                    draw_game_in_progress(screen) # If the mouse is on easy button, returns to main
                elif medium_rectangle.collidepoint(event.pos):
                    playing_board = Board(9, 9, screen, 1)
                    draw_game_in_progress(screen)
                elif hard_rectangle.collidepoint(event.pos):
                    playing_board = Board(9, 9, screen, 2)
                    draw_game_in_progress(screen)
        pygame.display.update()

def draw_game_in_progress(screen):
    # Initialized button font
    button_font = pygame.font.Font(None, 40)

    # Color background
    screen.fill(BG_COLOR)
    playing_board.draw()
    # Initialize and draw line grid
    # for r in range(210, 631, 210):
    #     for thin_r in range(70, 630, 70):
    #         pygame.draw.line(screen, LINE_COLOR, (0, thin_r), (630, thin_r), 2)
    #     pygame.draw.line(screen, LINE_COLOR, (0, r), (630, r), 5)
    # for c in range(210, 630, 210):
    #     for thin_c in range(70, 630, 70):
    #         pygame.draw.line(screen, LINE_COLOR, (thin_c, 0), (thin_c, 630), 2)
    #     pygame.draw.line(screen, LINE_COLOR, (c, 0), (c, 630), 5)

    # Initialize buttons
    # Initialize text first
    reset_text = button_font.render("Reset", 0, LINE_COLOR)
    restart_text = button_font.render("Restart", 0, LINE_COLOR)
    exit_text = button_font.render("Exit", 0, LINE_COLOR)

    pygame.draw.rect(screen, LINE_COLOR, ((0, 630), (630, 700)), 0)
    # Initialize button background color and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill("white")
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill("white")
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill("white")
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 2 - 125, HEIGHT - 35))

    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2 + 5, HEIGHT - 35))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 + 125, HEIGHT - 35))

    # Draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    playing = True

    while playing == True:
        playing_board.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouse is on buttons
                if reset_rectangle.collidepoint(event.pos):
                    playing_board.reset_to_original()
                elif restart_rectangle.collidepoint(event.pos):
                    draw_game_start(screen)
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()
                else:
                    selected_cell = playing_board.click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if selected_cell:
                        playing_board.select(selected_cell[0], selected_cell[1])
                        pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    playing_board.clear()
                if event.key == pygame.K_2:
                    playing_board.sketch(2)
                if event.key == pygame.K_3:
                    playing_board.sketch(3)
                if event.key == pygame.K_4:
                    playing_board.sketch(4)
                if event.key == pygame.K_5:
                    playing_board.sketch(5)
                if event.key == pygame.K_6:
                    playing_board.sketch(6)
                if event.key == pygame.K_7:
                    playing_board.sketch(7)
                if event.key == pygame.K_8:
                    playing_board.sketch(8)
                if event.key == pygame.K_9:
                    playing_board.sketch(9)
                if event.key == pygame.K_1:
                    playing_board.sketch(1)
                if event.key == pygame.K_RETURN:
                    playing_board.place_number(playing_board.selected_cell.sketeched_value)
                    if playing_board.is_full():
                        playing = False
                        if playing_board.check_board():
                            draw_game_won(screen)
                        else:
                            draw_game_over(screen)


def draw_game_won(screen):
    # Initialized title font
    win_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    win_surface = win_font.render("Game Won!", 0, LINE_COLOR)
    win_rectangle = win_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(win_surface, win_rectangle)

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

def draw_game_over(screen):
    end_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    end_surface = end_font.render("Game Over :(", 0, LINE_COLOR)
    end_rectangle = end_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(end_surface, end_rectangle)

    # Initialize buttons
    # Initialize text first
    restart_text = button_font.render("Restart", 0, (255, 255, 255))


    # Initialize button background color and text
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    # Initialize button rectangle
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))

    # Draw buttons
    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if mouse is on start button
                if restart_rectangle.collidepoint(event.pos):
                    draw_game_start(screen)  # If the mouse is on restart button, returns to game start

        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    screen.fill(BG_COLOR)

    draw_game_start(screen)

if __name__ == "__main__":
    main()


