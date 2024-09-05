# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init
    print('Starting asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Draw screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Time (FPS)
    gametime = pygame.time.Clock()
    dt = 0

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    #Asteroid Field
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    #Shots
    Shot.containers = (shots, updatable, drawable)

    while True:
        #Close game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0,0,0)) #background (black)
        for u in updatable:
            u.update(dt)

        for i in asteroids:
            if player.collision(i):
                raise SystemExit('Game over!')
            for s in shots:
                if s.collision(i):
                    i.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)
        pygame.display.flip() #display update

        dt = gametime.tick(60) / 1000

if __name__ == "__main__":
    main()