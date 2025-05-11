import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        super().__init__(x, y, radius)
        self.velocity = self.y
        self.add(*self.containers)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):

        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_angle = random.uniform(20, 50)
        Asteroid(self.position, self.velocity.rotate(-random_angle), self.radius - ASTEROID_MIN_RADIUS)
        Asteroid(self.position, self.velocity.rotate(random_angle), self.radius - ASTEROID_MIN_RADIUS)
        
        
