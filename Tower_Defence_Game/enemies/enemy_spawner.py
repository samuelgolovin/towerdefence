import pygame
import random
from enemies.enemy import Enemy

class EnemySpawner:
    def __init__(self):
        self.spawn_timer = 0

    def spawn_enemy(self, WIDTH, HEIGHT):
        side = random.randint(1, 4)  # Determine which side to spawn the enemy
        if side == 1:  # Top
            x = random.randint(0, WIDTH)
            y = -20
        elif side == 2:  # Right
            x = WIDTH + 20
            y = random.randint(0, HEIGHT)
        elif side == 3:  # Bottom
            x = random.randint(0, WIDTH)
            y = HEIGHT + 20
        else:  # Left
            x = -20
            y = random.randint(0, HEIGHT)
        return Enemy((x, y), (WIDTH // 2, HEIGHT // 2))