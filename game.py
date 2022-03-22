import pygame
class asteroid_game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroid Game")
        self.screen=pygame.display.set_mode((720,480))
        self.active=True
        self.spacecraft=spacecraft()
        self.bullets=bullets()
        self.clock=pygame.time.Clock()
    def mainloop(self):
        while True:
            self.clock.tick(60)
            self.game_process()
            if self.active:
                self.input_check()
                self.draw()
    def game_process(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            match event.type:
                case pygame.WINDOWHIDDEN:
                    self.active=False
                case pygame.WINDOWSHOWN:
                    self.active=True
        self.bullets.update_all()
    def input_check(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.spacecraft.forward()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.spacecraft.left()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.spacecraft.backward()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.spacecraft.right()
        if keys[pygame.K_SPACE]:
            self.bullets.create(self.spacecraft.loc[0]+36,self.spacecraft.loc[1])
    def draw(self):
        self.screen.fill((82,82,255))
        self.screen.blit(self.spacecraft.image,self.spacecraft.loc)
        for image,j in self.bullets:
            self.screen.blit(image,j)
        pygame.display.update()
class spacecraft:
    def __init__(self):
        self.image=pygame.image.load("spacecraft.png").convert_alpha()
        self.loc=[324,324]
    def forward(self):
        self.loc[1]=max(self.loc[1]-8,0)
    def left(self):
        self.loc[0]=max(self.loc[0]-8,0)
    def backward(self):
        self.loc[1]=min(self.loc[1]+8,480)
    def right(self):
        self.loc[0]=min(self.loc[0]+8,648)
class bullets:
    def __init__(self):
        self.coordinates=[]
        self.image=pygame.image.load("bullet.png").convert()
        self.cooldown=0
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<len(self.coordinates):
            loc=self.coordinates[self.n]
            self.n+=1
            return self.image,loc
        else:
            raise StopIteration
    def create(self,x,y):
        if self.cooldown==0:
            self.coordinates.append([x,y])
            self.cooldown=14
        else:
            self.cooldown-=1
    def update_all(self):
        temp=[]
        for i in range(len(self.coordinates)):
            self.coordinates[i][1]-=8
            if self.coordinates[i][1]<=0:
                temp.append(self.coordinates[i])
        for i in temp:
            self.coordinates.remove(i)