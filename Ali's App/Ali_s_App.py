# Importing
import pygame

# Init
pygame.init()

# Variables
windowcolor = (0,0,0)
textcolor = (255,255,255)
textbase = pygame.font.SysFont("ComicSans",20)
size = (700,600)
clock = pygame.time.Clock()
Running = True
FPS = 60

# Window
screen = pygame.display.set_mode(size)

# Render Func
def Rendertext(text,position):
    textTBD = textbase.render(text,1,textcolor)
    screen.blit(textTBD,position)

# While loop
while Running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    Rendertext("This is my first App!",(0,0))
    Rendertext("Made by Ali",(0,25))
    pygame.display.update()
    clock.tick(FPS)

# Quit
pygame.quit()