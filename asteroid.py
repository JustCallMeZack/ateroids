import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self, player,score):
        self.kill()
        player.add_score(2)
        score.update(player.get_score())
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)

        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y,new_radius)
        ast_2 = Asteroid(self.position.x, self.position.y,new_radius)
        ast_1.velocity = new_vel1
        ast_2.velocity = new_vel2
