import pygame
import sys

from enemies.enemy import Enemy
from towers.tower import Tower

# Constants
WIDTH, HEIGHT = 800, 450
BLACK = (0, 0, 0)
WHITE = (240, 240, 240)
RED = (240, 0, 0)
GREEN = (0, 240, 0)

tower01 = Tower((WIDTH // 2, HEIGHT // 2), "basic")
enemy01 = Enemy(20, RED, 1, (600, -50), tower01.position)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    enemy01.update()

    screen.fill(BLACK)
    tower01.draw(screen)
    enemy01.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
