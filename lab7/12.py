import pygame 
import math
import datetime

pygame.init()

display = pygame.display.set_mode((640, 640), pygame.RESIZABLE)
pygame.display.set_caption('Clock')
FPS = 50
clock = pygame.time.Clock()

def convert_degrees(R, theta):
    y = math.cos(2*math.pi*theta/360)*R
    x = math.sin(2*math.pi*theta/360)*R
    return x + 320, 320-y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        display.fill((255, 255, 255))
        mickey = pygame.image.load("C:/Users/77785/Downloads/mickey-mouse-glass-wall-clock.webp").convert()
        scale = pygame.transform.scale(mickey, ((640, 640)))
        display.blit(scale, (0, 0) )

        

        current_time = datetime.datetime.now()
        minute = current_time.minute
        hour = current_time.hour

        #minute
        R = 270
        theta = minute*(360/60)
        pygame.draw.line(display, (0, 0, 0), (320, 320), convert_degrees(R, theta), 4)

        #hour
        R = 220
        theta = hour*(360/12)
        pygame.draw.line(display, (255, 0, 0), (320, 320), convert_degrees(R, theta), 4)





        pygame.display.update()
