from game import asteroid_game
from interface import gameover
import pygame
if __name__=="__main__":
    pygame.init()
    pygame.display.set_caption("Asteroid Game")
    screen=pygame.display.set_mode((720,480))
    current="game"
    window=asteroid_game(screen)
    while 1:
        if current=="game":
            window=asteroid_game(screen)
        if current=="GameOver":
            window=gameover(screen)
        current=window.mainloop()