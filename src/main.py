from menu import main_menu
import pygame

IS_SINGLE_PLAYER = True

WIDTH            = 1280
HEIGHT           = 720

WIDTH_B          = 1280
HEIGHT_B         = 720

ROWS             = 10
COLS             = 10

SQUARE_SIZE      = WIDTH // COLS

DARK_RED         = (120, 6, 6)
RED              = (255, 0, 0)
WHITE            = (255, 255, 255)
BLACK            = (0, 0, 0)

FPS              = 60
WIN              = pygame.display.set_mode((WIDTH, HEIGHT))
BOARD            = pygame.display.set_mode((WIDTH_B, HEIGHT_B))

pos_x = 5
pos_y = 10

pygame.display.set_caption('Snakes & Ladders by David Filiks, Afsar Ali')

class Board:
    def __init__(self):
        self.board = []

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, DARK_RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_piece(self, screen, colour, col, row):
        radius = SQUARE_SIZE // 2 - 15
        x = SQUARE_SIZE * col - SQUARE_SIZE // 2
        y = SQUARE_SIZE * row - SQUARE_SIZE // 2
        pygame.draw.circle(screen, colour, (x, y), radius)

def main():
    run = True
    clock = pygame.time.Clock()

    board = Board()

    while run and IS_SINGLE_PLAYER:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(BOARD)
        board.draw_piece(WIN, RED, pos_x, pos_y)
        pygame.display.update()
        
    pygame.quit()

main()
