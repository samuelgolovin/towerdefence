import pygame

class Enemy:
    def __init__(self, position, tower_position):
        self.position = pygame.Vector2(position)
        self.direction = pygame.Vector2(tower_position) - self.position
        self.direction.normalize_ip()
        self.speed = 2
        self.health = 20

    def move_towards_tower(self, tower_position):
        self.direction = pygame.Vector2(tower_position) - self.position
        self.direction.normalize_ip()
        self.position += self.direction * self.speed

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def draw(self, screen):
        pygame.draw.circle(screen, (240, 0, 0), (int(self.position.x), int(self.position.y)), 20)