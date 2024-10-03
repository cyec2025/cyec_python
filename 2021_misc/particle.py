import pygame,sys

#game initialization
pygame.init()
screen = pygame.display.set_mode((900,600),0,32)
pygame.display.set_caption('ooo pretty')
clock = pygame.time.Clock()
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
time = 100
#game loop
while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #rendering
    pygame.draw.circle(screen,white,(0,0),time)
    # various things
    screen.fill(
    pygame.display.update()
    clock.tick(60)
