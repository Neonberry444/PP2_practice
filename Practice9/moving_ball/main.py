import pygame

x = 25
y = 25
pygame.init()
screen = pygame.display.set_mode((1535, 800))
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and 45 <= y: y -= 20
    if pressed[pygame.K_DOWN] and y <= 760: y += 20
    if pressed[pygame.K_LEFT] and x >= 45: x -= 20
    if pressed[pygame.K_RIGHT] and x <= 1504: x += 20
    
    pygame.draw.circle(screen, (255, 0, 0), (x,y), 25)
    pygame.display.flip()
    clock.tick(60)