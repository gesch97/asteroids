import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS >= self.radius:
            return

        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_velocity_a = self.velocity.rotate(angle)
        new_velocity_b = self.velocity.rotate(-angle)

        new_asteroid_a = Asteroids(self.position.x, self.position.y, new_radius)
        new_asteroid_b = Asteroids(self.position.x, self.position.y, new_radius)

        new_asteroid_a.velocity = new_velocity_a * 1.2
        new_asteroid_b.velocity = new_velocity_b * 1.2
