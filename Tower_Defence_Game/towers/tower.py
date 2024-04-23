import pygame
from towers.projectiles import Projectile

class Tower:
    def __init__(self, position, fire_rate):
        self.position = pygame.Vector2(position)
        self.health = 100
        self.projectile_damage = 20
        self.attack_range = 200
        self.projectiles = []
        self.fire_rate = fire_rate
        self.fire_cooldown = 0
        # subtract half of the width and height to maintain center of the tower
        self.rect = pygame.Rect(self.position.x - 25, self.position.y - 25, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, (240, 240, 240), self.rect)

    def shoot_projectile(self, target_position):
        direction = pygame.Vector2(target_position) - self.position
        direction.normalize_ip()
        self.projectiles.append(Projectile(self.position, direction))

    def update_projectiles(self, enemies):
        for projectile in self.projectiles:
            projectile.move()
            for enemy in enemies:
                if projectile.position.distance_to(enemy.position) < 20:
                    enemy.health -= self.projectile_damage
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