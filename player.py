import pygame
from circleshape import CircleShape, PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
class Player(CircleShape):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

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
                print(f"{dt}")
            elif self.timer > 0:
                exit
        if self.timer > 0:
            self.timer -= dt 
        if self.timer < 0:
            self.timer = 0 
        
                
                

            

