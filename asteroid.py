import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_MOVE_SPEED


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        super().__init__(x, y, radius)
        self.velocity = self.y
        self.add(*self.containers)
        self.image_original = pygame.image.load("asteroid.png").convert_alpha()
        self.image = self.image_original
        self.rect = self.image.get_rect(center=self.position)
        self.rotation = 0
        self.asteroid_move = 1
    
    def draw(self, screen):
        actual_size_image = self.image = pygame.transform.scale(self.image, (self.radius * 2.25, self.radius * 2.25))
        rotated_image = pygame.transform.rotate(actual_size_image, self.rotation + 180)
        rotated_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rotated_rect.topleft)
      

    def update(self, dt):

        self.position += self.velocity * dt * ASTEROID_MOVE_SPEED * self.asteroid_move
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(-random_angle) * 2
        new_velocity2 = self.velocity.rotate(random_angle) * 2
        Asteroid(self.position, new_velocity1, self.radius - ASTEROID_MIN_RADIUS)
        Asteroid(self.position, new_velocity2, self.radius - ASTEROID_MIN_RADIUS)
        
        
