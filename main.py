import pygame
from asteroidfield import AsteroidField
import asteroidfield
from asteroids import Asteroids
import constants
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clk = pygame.time.Clock()
    dt = 0

    gupdatable = pygame.sprite.Group()
    gdrawable = pygame.sprite.Group()
    gasteroids = pygame.sprite.Group()
    gshots = pygame.sprite.Group()

    Player.containers = (gupdatable, gdrawable)
    Asteroids.containers = (gasteroids, gupdatable, gdrawable)
    AsteroidField.containers = (gupdatable,)
    Shot.containers = (gshots, gupdatable, gdrawable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroidF = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clk.tick(60) / 1000
        for obj in gupdatable:
            obj.update(dt)

        for obj in gasteroids:
            if obj.check_collosion(player):
                print("Game over!")
                exit()

        screen.fill((0, 0, 0))
        for obj in gdrawable:
            obj.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
