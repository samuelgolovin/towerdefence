import pygame
import sys

from enemies.enemy import Enemy
from towers.tower import Tower
from enemies.enemy_spawner import EnemySpawner

# Constants
WIDTH, HEIGHT = 800, 450
BLACK = (0, 0, 0)
WHITE = (240, 240, 240)
RED = (240, 0, 0)
GREEN = (0, 240, 0)
ENEMY_SPAWN_INTERVAL = 60

towers = [Tower((WIDTH // 2 - 25, HEIGHT // 2 - 25), fire_rate=60)]  # Fire rate in frames
enemies = []
enemy_spawner = EnemySpawner()

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update towers and projectiles
    for tower in towers:
        tower.update(enemies)
        tower.update_projectiles(enemies)

    for enemy in enemies:
        if enemy.is_dead():
            enemies.remove(enemy)

    screen.fill((0, 0, 0))

# Spawn enemies at specific intervals
    if enemy_spawner.spawn_timer <= 0:
        enemies.append(enemy_spawner.spawn_enemy(WIDTH, HEIGHT))
        enemy_spawner.spawn_timer = ENEMY_SPAWN_INTERVAL
    else:
        enemy_spawner.spawn_timer -= 1

    # Draw towers and projectiles
    for tower in towers:
        tower.draw(screen)
        for projectile in tower.projectiles:
            projectile.draw(screen)

        # Check if enemies are within range of the towers
    # for enemy in enemies:
    #     for tower in towers:
    #         enemy.move_towards_tower(tower.position)
    #         enemy.draw(screen)

    # or do this instead of the above code since we only have one tower anyway.

    for enemy in enemies:
        enemy.move_towards_tower(towers[0].position)
        enemy.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
