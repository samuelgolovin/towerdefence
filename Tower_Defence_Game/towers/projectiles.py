import pygame

class Projectile:
    def __init__(self, position, direction):
        self.speed = 5
        self.position = pygame.Vector2(position)
        self.velocity = direction * self.speed

    def move(self):
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 240, 0), (int(self.position.x), int(self.position.y)), 5)