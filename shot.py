import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_TURN_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, SHOT_RADIUS)
        direction = pygame.Vector2(0, 1).rotate(self.y)
        self.velocity = direction * PLAYER_SHOT_SPEED
        self.image_original = pygame.image.load("bullet.png").convert_alpha()
        self.image_original = pygame.transform.scale(self.image_original, (25, 25))
        self.image = self.image_original
        self.rotation = 0
      

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.y + 180)
        rotated_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rotated_rect.topleft)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.position += self.velocity * dt