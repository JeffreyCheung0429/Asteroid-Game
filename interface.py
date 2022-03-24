import pygame
class gameover:
    def __init__(self,surface):
        self.screen=surface
        self.active=True
        self.clock=pygame.time.Clock()
        pygame.time.delay(2000)
        self.screen.blit(pygame.image.load("GameOver.png").convert_alpha(),(0,0))
        pygame.display.update()
        pygame.time.delay(1000)
        self.screen.blit(pygame.image.load("again.png").convert_alpha(),(120,288))
        pygame.display.update()
    def mainloop(self):
        while 1:
            self.clock.tick(30)
            if self.process()=="game":
                return "game"
    def process(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.MOUSEBUTTONUP:
                pos=event.pos
                if pos[0]>=120 and pos[0]<=600 and pos[1]>=288 and pos[1]<=384:
                    return "game"
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    return "game"