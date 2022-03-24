import pygame,random
class asteroid_game:
    def __init__(self,surface):
        self.screen=surface
        self.active=True
        self.spacecraft=spacecraft()
        self.bullets=bullets()
        self.asteroids=asteroids()
        self.clock=pygame.time.Clock()
        self.frame=0
        self.previous_bullet=-16
    def mainloop(self):
        while 1:
            self.clock.tick(60)
            self.window_check()
            if self.active:
                self.input_check()
                if self.game_process()=="GameOver":
                    return "GameOver"
                self.draw()
            print(self.frame)
    def window_check(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    quit()
                case pygame.WINDOWFOCUSLOST:
                    self.active=False
                case pygame.WINDOWFOCUSGAINED:
                    self.active=True
    def game_process(self):
        self.bullets.update_all()
        if self.frame%20==0:
            self.asteroids.spawn()
        self.asteroids.update_all()
        spacecraft_loc=self.spacecraft.loc[:]
        spacecraft_loc[1]+=16
        spacecraft_rect=self.spacecraft.image.get_rect()[:]
        spacecraft_rect[3]-=16
        for i,j in self.asteroids:
            if self.detect_collosions(spacecraft_loc,spacecraft_rect,j[0:2],i.get_rect()):
                return "GameOver"
        for i,j in self.asteroids:
            for k,l in self.bullets:
                if self.detect_collosions(l[0:2],k.get_rect(),j[0:2],i.get_rect()):
                    self.asteroids.remove(j)
    def detect_collosions(self,coor1,rect1,coor2,rect2):
        if coor1[0]<coor2[0]:
            if coor1[0]+rect1[2]>=coor2[0]:
                pass
            else:
                return False
        elif coor1[0]>coor2[0]:
            if coor1[0]<=coor2[0]+rect2[2]:
                pass
            else:
                return False
        if coor1[1]<coor2[1]:
            if coor1[1]+rect1[3]>=coor2[1]:
                pass
            else:
                return False
        elif coor1[1]>coor2[1]:
            if coor1[1]<=coor2[1]+rect2[3]:
                pass
            else:
                return False
        return True
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
            if self.frame-self.previous_bullet>=8:
                self.bullets.create(self.spacecraft.loc[0]+21,self.spacecraft.loc[1])
                self.previous_bullet=self.frame
    def draw(self):
        self.screen.fill((82,82,255))
        self.screen.blit(self.spacecraft.image,self.spacecraft.loc)
        for image,j in self.asteroids:
            self.screen.blit(image,j)
        for image,j in self.bullets:
            self.screen.blit(image,j)
        self.frame+=1
        pygame.display.update()
class spacecraft:
    def __init__(self):
        self.image=pygame.image.load("spacecraft.png").convert_alpha()
        self.loc=[339,324]
    def forward(self):
        self.loc[1]=max(self.loc[1]-8,240)
    def left(self):
        self.loc[0]=max(self.loc[0]-8,0)
    def backward(self):
        self.loc[1]=min(self.loc[1]+8,408)
    def right(self):
        self.loc[0]=min(self.loc[0]+8,648)
class bullets:
    def __init__(self):
        self.coordinates=[]
        self.image=pygame.image.load("bullet.png").convert()
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
        self.coordinates.append([x,y])
    def update_all(self):
        temp=[]
        for i in range(len(self.coordinates)):
            self.coordinates[i][1]-=8
            if self.coordinates[i][1]<=0:
                temp.append(self.coordinates[i])
        for i in temp:
            self.coordinates.remove(i)
class asteroids:
    def __init__(self):
        self.coordinatesrotation=[]
        self.image=pygame.image.load("asteroid.png").convert_alpha()
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<len(self.coordinatesrotation):
            loc=self.coordinatesrotation[self.n][0:2]
            image=self.rotate(self.coordinatesrotation[self.n][2])
            self.n+=1
            return image,loc
        else:
            raise StopIteration
    def spawn(self):
        x=random.randint(0,720)
        self.coordinatesrotation.append([x,0,0])
    def update_all(self):
        temp=[]
        for i in range(len(self.coordinatesrotation)):
            self.coordinatesrotation[i][1]+=2
            self.coordinatesrotation[i][2]+=1
            if self.coordinatesrotation[i][1]>=480:
                temp.append(self.coordinatesrotation[i])
        for i in temp:
            self.coordinatesrotation.remove(i)
    def rotate(self,rotation):
        rotated_image=pygame.transform.rotate(self.image,(rotation%24)*15)
        return rotated_image
    def remove(self,removing):
        for i in range(len(self.coordinatesrotation)):
            if self.coordinatesrotation[i][0:2]==removing:
                self.coordinatesrotation.pop(i)
                return