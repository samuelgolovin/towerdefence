import pygame

class Enemy:
    def __init__(self, radius, color, speed, position, tower_position):
        self.health = 100
        self.position = pygame.Vector2(position)
        self.tower_position = pygame.Vector2(tower_position)
        self.direction = pygame.Vector2(tower_position) - self.position
        self.direction.normalize_ip()
        self.color = color
        self.radius = radius
        self.speed = speed
        self.rect = pygame.Rect(self.position.x - self.radius * 0.75, self.position.y - self.radius * 0.75, self.radius * 1.5, self.radius * 1.5)

    def move_towards_tower(self, tower_position):
        self.direction = pygame.Vector2(tower_position) - self.position
        self.direction.normalize_ip()
        self.position += self.direction * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.position.x, self.position.y), self.radius)
        # draws the square hitbox of the enemy
        # pygame.draw.rect(surface, (255, 255, 255, 100), self.rect)

    def update(self):
        self.rect = pygame.Rect(self.position.x - self.radius * 0.75, self.position.y - self.radius * 0.75, self.radius * 1.5, self.radius * 1.5)
        self.move_towards_tower(self.tower_position)