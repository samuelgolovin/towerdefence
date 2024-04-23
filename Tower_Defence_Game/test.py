import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ENEMY_SPEED = 2
PROJECTILE_SPEED = 5
ATTACK_RANGE = 150
PROJECTILE_DAMAGE = 20

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Tower:
    def __init__(self, position, fire_rate):
        self.position = pygame.Vector2(position)
        self.health = 100
        self.attack_range = ATTACK_RANGE
        self.projectiles = []
        self.fire_rate = fire_rate
        self.fire_cooldown = 0

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.position.x, self.position.y, 50, 50))

    def shoot_projectile(self, target_position):
        direction = pygame.Vector2(target_position) - self.position
        direction.normalize_ip()
        self.projectiles.append(Projectile(self.position, direction))

    def update_projectiles(self, enemies):
        for projectile in self.projectiles:
            projectile.move()
            for enemy in enemies:
                if projectile.position.distance_to(enemy.position) < 20:
                    enemy.health -= PROJECTILE_DAMAGE
                    self.projectiles.remove(projectile)
                    break

    def update(self, enemies):
        if self.fire_cooldown <= 0:
            for enemy in enemies:
                if enemy.position.distance_to(self.position) <= self.attack_range:
                    self.shoot_projectile(enemy.position)
                    self.fire_cooldown = self.fire_rate
                    break
        else:
            self.fire_cooldown -= 1

class Enemy:
    def __init__(self, position, tower_position):
        self.position = pygame.Vector2(position)
        self.direction = pygame.Vector2(tower_position) - self.position
        self.direction.normalize_ip()
        self.speed = ENEMY_SPEED
        self.health = 100

    def move_towards_tower(self, tower_position):
        self.direction = pygame.Vector2(tower_position) - self.position
        self.direction.normalize_ip()
        self.position += self.direction * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.position.x), int(self.position.y)), 20)

class Projectile:
    def __init__(self, position, direction):
        self.position = pygame.Vector2(position)
        self.velocity = direction * PROJECTILE_SPEED

    def move(self):
        self.position += self.velocity

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defence")

# Create objects
towers = [Tower((SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT // 2 - 25), fire_rate=60)]  # Fire rate in frames
enemies = [Enemy((100, 100), towers[0].position)]

clock = pygame.time.Clock()

# Main game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update towers and projectiles
    for tower in towers:
        tower.update(enemies)
        tower.update_projectiles(enemies)

    # Check if enemies are within range of the towers
    for enemy in enemies:
        for tower in towers:
            enemy.move_towards_tower(tower.position)
            enemy.draw(screen)

    # Draw towers and projectiles
    for tower in towers:
        tower.draw(screen)
        for projectile in tower.projectiles:
            pygame.draw.circle(screen, WHITE, (int(projectile.position.x), int(projectile.position.y)), 5)

    pygame.display.flip()
    clock.tick(60)
