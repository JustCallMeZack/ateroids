from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.PLAYER_SHOOT_COOLDOWN = 0
        self.score = 0



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        neg_dt = dt - (dt * 2)
        if keys[pygame.K_a]:
            self.rotate(neg_dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(neg_dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.PLAYER_SHOOT_COOLDOWN -= dt
        
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        

        if self.PLAYER_SHOOT_COOLDOWN <= 0:
            self.PLAYER_SHOOT_COOLDOWN = .25
            shot = Shot(self.position.x, self.position.y,SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1)
            shot.velocity = shot.velocity.rotate(self.rotation)
            shot.velocity *= PLAYER_SHOOT_SPEED

 