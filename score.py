import pygame
from asteroid import Asteroid
from shot import Shot
from circleshape import CircleShape

class Score(CircleShape):
    def __init__(self):
        super().__init__(0, 0, 0)
        self.number = 0

    def draw(self, screen):
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render(f"Score: {self.number}", True, "white", None)
        screen.blit(text_surface, (100, 100))

    def update(self, dt):
        self.number += 10