import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Groups:
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Containers:
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable, )
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Black screen:
        screen.fill(0, None, 0)
        #Keys, Position update:
        updateable.update(dt)
        #Collision:
        for asteroid in asteroids:
            if player.collision(asteroid) or asteroid.collision(player):
                print("Game Over!")
                raise SystemExit
        for o_asteroid in asteroids:
            for shot in shots:
                if shot.collision(o_asteroid) or o_asteroid.collision(shot):
                    shot.kill()
                    o_asteroid.split()
            

        #Draw object:
        for draws in drawable:
            draws.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()