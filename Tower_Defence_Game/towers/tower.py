import pygame
from towers.projectiles import Projectile

class Tower:
    def __init__(self, position, tower):
        self.in_range = False
        self.position = pygame.Vector2(position)
        if tower == "basic":
            self.health = 100
            self.width = 50
            self.height = 50
            self.color = (240, 240, 240)
            self.range = 100
            self.rect = pygame.Rect(self.position.x - self.width // 2, self.position.y - self.height // 2, self.width, self.height)
        # if tower == "super":
        #     self.health = 300
        #     self.width = 75
        #     self.height = 75
        #     self.color = (255, 255, 255)
        #     self.range = 200
        #     self.rect = pygame.Rect(self.position.x - self.width // 2, self.position.y - self.height // 2, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.circle(surface, (111, 111, 111, 111), self.rect.center, self.range, 2)

    # def update(self):
