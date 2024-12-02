# sudoku gui

import pygame, sys

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Sudoku")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)

                screen.fill("White")
                pygame.display.flip()
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()