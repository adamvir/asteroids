import pygame
from circleshape import CircleShape, PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
class Player(CircleShape):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.image_original = pygame.image.load("spaceship.png").convert_alpha()
        self.image_original = pygame.transform.scale(self.image_original, (100, 100))
        self.image = self.image_original
        self.rect = self.image.get_rect(center=self.position)
        self.rotation = 0
        self.timer = 0
        # in the player class
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image_original, -self.rotation + 180)
        rotated_rect = rotated_image.get_rect(center=self.position)

        # Kirajzolás
        screen.blit(rotated_image, rotated_rect.topleft)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_MOVE_SPEED * dt

    def shoot(self, dt):
            return Shot(self.position, self.rotation)


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(- dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt) 
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(- dt)
        if keys[pygame.K_SPACE]:
            if self.timer == 0:
                self.shoot(dt)
                self.timer = PLAYER_SHOOT_COOLDOWN
            elif self.timer > 0:
                exit
        if self.timer > 0:
            self.timer -= dt 
        if self.timer < 0:
            self.timer = 0 
        
                
                

            

