import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, SHOT_RADIUS)
        direction = pygame.Vector2(0, 1).rotate(self.y)
        self.velocity = direction * PLAYER_SHOT_SPEED
      

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):

        self.position += self.velocity * dt