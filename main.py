import pygame
pygame.init()
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from score import Score
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
    Score.containers = (drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable, )
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)

    score = Score(0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    space = pygame.transform.scale(pygame.image.load("space.png").convert_alpha(), (1280, 720))
    clock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    kepernyo = input("Képernyő stílusa (space/black)(s/b): ")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Black screen:
        if kepernyo == "b":
            screen.fill(0, None, 0)
        #Space screen:
        if kepernyo == "s":
            screen.blit(space, (0, 0))
        else:
            screen.fill(0, None, 0)
        #Keys, Position update:
        updateable.update(dt)
        player.gameover()
        #Collision, Score update:
        for asteroid in asteroids:
            if player.collision(asteroid) or asteroid.collision(player):
                print("Game Over!")
                raise SystemExit
        for o_asteroid in asteroids:
            for shot in shots:
                if shot.collision(o_asteroid) or o_asteroid.collision(shot):
                    shot.kill()
                    o_asteroid.split()
                    score.update(dt)
            
        #Draw object:
        for draws in drawable:
            draws.draw(screen)
        score.draw(screen)
        pygame.display.flip()
        clock.tick(120)
        dt = clock.tick(120) / 1000
        
        

if __name__ == "__main__":
    main()