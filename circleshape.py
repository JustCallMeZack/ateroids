import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.score = 0

        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, player):
       distance = player.position.distance_to(self.position)
       if distance <= (player.radius + self.radius):
           return True
       return False
    
    def add_score(self, x):
        
        self.score += x
        
    def get_score(self):
        return self.score    

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    




