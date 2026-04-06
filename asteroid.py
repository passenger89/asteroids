import pygame, random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
      super().__init__(x, y, radius)
  
  def draw(self, surface):
      pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
  
  def update(self, dt):
    self.position += (self.velocity * dt)
    

  def split(self):
      self.kill()
      if (self.radius <= ASTEROID_MIN_RADIUS):
          return
      else:
          log_event("asteroid_split")
          random_angle = random.uniform(20, 50)
          a = self.velocity.rotate(random_angle)
          b = self.velocity.rotate(-random_angle)
          new_radius = self.radius - ASTEROID_MIN_RADIUS
          small_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
          small_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
          small_asteroid1.velocity = a * 1.2
          small_asteroid2.velocity = b * 1.2