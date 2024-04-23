import pygame

class Projectile:
    def __init__(self, x, y, velocity_x, velocity_y, bullet):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        
        if bullet == "basic":
            self.width = 50
            self.height = 50
            self.color = (240, 240, 240)
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if bullet == "super":
            self.width = 75
            self.height = 75
            self.color = (240, 240, 240)
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0, 100), self.rect)

    # def update(self):
    