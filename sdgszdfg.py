import pygame
import numpy as np

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Размеры
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Инициализация
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

grid = np.zeros((ROWS, COLS))
running = False

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE if grid[y, x] else BLACK, rect)
    pygame.display.update()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid[y//CELL_SIZE, x//CELL_SIZE] ^= 1  # Инвертируем клетку
            draw_grid()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running  # Пауза/старт
            elif event.key == pygame.K_r:
                grid = np.zeros((ROWS, COLS))  # Сброс

    if running:
        new_grid = grid.copy()
        for y in range(ROWS):
            for x in range(COLS):
                neighbors = np.sum(grid[max(0, y-1):min(ROWS, y+2),
                                    max(0, x-1):min(COLS, x+2)]) - grid[y, x]
                if grid[y, x] and (neighbors < 2 or neighbors > 3):
                    new_grid[y, x] = 0
                elif not grid[y, x] and neighbors == 3:
                    new_grid[y, x] = 1
        grid = new_grid
        draw_grid()
        clock.tick(10)  # 10 FPS