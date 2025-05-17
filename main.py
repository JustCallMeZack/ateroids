# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from text import *


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score_text = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    TextSprite.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    score = TextSprite(24)


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    # Game loop
    while True: 
        screen.fill("black")
        screen.blit(score.text, score.rect)



        # container methods
        updatable.update(dt)
        for thing in asteroids:
            if thing.collision(player):
                print(f"Score: {player.score}")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if thing.collision(shot):
                    shot.kill() 
                    thing.split(player,score)
                    
            
        for entity in drawable:
            entity.draw(screen)



        pygame.display.flip()
        dt = game_clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(player.get_score())    
                return 
    




if __name__ == "__main__":
    main()