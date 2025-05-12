import pygame
from asteroid import Asteroid
from shot import Shot
from circleshape import CircleShape

class Score:
    def __init__(self, number):
        self.number = number

    def draw(self, screen):
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render(f"Score: {self.number}", True, "white", None)
        screen.blit(text_surface, (10, 10))

    def update(self, dt):
        self.number += 10