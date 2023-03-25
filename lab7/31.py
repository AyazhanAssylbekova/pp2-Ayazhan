import pygame
import time
pygame.init()
scree=pygame.display.set_mode((500,500))
x=20
y=20
done=False
is_blue=True
clock = pygame.time.Clock()
# im=pygame.image.load("ball.png")
while not done:
    # press=pygame.key.get_pressed()
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
            if 0<=y-20<=500:
                    y-=20
    if pressed[pygame.K_DOWN]:
            if 0<=y+20<=500:
                y += 20
    if pressed[pygame.K_LEFT]:
            if 0<=x-20<=500: 
                x -= 20   
    if pressed[pygame.K_RIGHT]: 
            if 0<=x+20<=500:
                x += 20
    scree.fill((255,255,255))
    # if is_blue: color = (0, 128, 255)
    # else: color = (255, 100, 0) 

    pygame.draw.circle(scree,"red",(x,y),25)

    pygame.display.flip()
    time.sleep(1/60)
