import random
import math


from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y, radius,kind):
        super().__init__(x,y,radius)
        self.coord_list = []
        self.type = kind
        self.init_coord_list()
        




    def init_coord_list(self):
        self.coord_list = []
        self.__offset_coord_list = []
        calc_min_angle = (math.pi * 2) / ASTEROID_STEPS[self.type]
        px, py = self.position
        for i in range(0,ASTEROID_STEPS[self.type]):
            random_modifier =  random.uniform(-ASTEROID_RANDOMNESS[self.type], ASTEROID_RANDOMNESS[self.type])
            new_radius = self.radius - random_modifier
            theta = i * calc_min_angle
            self.__offset_coord_list.append(((math.cos(theta) * new_radius),(math.sin(theta) * new_radius)))
            self.coord_list.append(((math.cos(theta) * new_radius) + px,(math.sin(theta) * new_radius) + py))
        
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.coord_list,2)

    def update(self,dt):

# ===============Wrap Logic=======================
        sx, sy = self.position
        if -61 > sx:
            self.set_pos(SCREEN_WIDTH + 60,sy)
            self.position += (self.velocity * dt)
            self.new_poly_coords()
        elif sx > SCREEN_WIDTH + 61:
            self.set_pos(-60,sy)
            self.position += (self.velocity * dt)
            self.new_poly_coords()
        elif -61 > sy:
            self.set_pos(sx,SCREEN_HEIGHT + 60)
            self.position += (self.velocity * dt)
            self.new_poly_coords()
        elif sy > SCREEN_HEIGHT + 61:
            self.set_pos(sx,-60)
            self.position += (self.velocity * dt)
            self.new_poly_coords()
# ===============Update Pos=======================
        else:
            self.position += (self.velocity * dt)
            self.new_poly_coords()




    def new_poly_coords(self): #create new list of coordinates for pygame draw polygon
        new_coord_list = []
        for point in self.__offset_coord_list:
            px, py = point 
            sx, sy = self.position
            nx, ny = (sx + px), (sy + py)
            new_coord_list.append((nx,ny))
        self.coord_list = new_coord_list

    def split(self, player):
        new_type = self.type - 1
        self.kill()
        player.add_score(2)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)

        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        ast_1 = Asteroid(self.position.x, self.position.y,new_radius,new_type)
        ast_2 = Asteroid(self.position.x, self.position.y,new_radius,new_type)
        ast_1.velocity = new_vel1
        ast_2.velocity = new_vel2
