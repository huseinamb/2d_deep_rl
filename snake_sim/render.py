# render.py
import pygame

SCREEN_SIZE = 500
CELL_SIZE = 10

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

def render(world):
    screen.fill((30, 30, 30))

    for y in range(world.size):
        for x in range(world.size):
            value = world.grid[y][x]

            if value == 0:
                color = (40, 40, 40)
            elif value == 1:
                color = (235, 64, 52)   # agent
            else:
                color = (122, 189, 111) # goal

            rect = pygame.Rect(
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
    clock.tick(60)
