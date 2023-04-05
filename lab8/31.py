# imports
import pygame
import math

# initialize
pygame.init()

# Clock
clock=pygame.time.Clock()

# rgb 
BLACK=(0,0,0)
BLUE=(0,0,255)
CYAN=(0,255,255)
GREEN=(0,255,0)
PURPLE=(255,0,255)
RED=(255,0,0)
WHITE=(255,255,255)

# SET UP WINDOW
wn=pygame.display.set_mode((600,600))
pygame.display.set_caption("Paint")

# while loop
ok=True
while ok:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            ok=False
    wn.fill(WHITE)
    startx=0;starty=270;endx=600;endy=150;wd=5
    pygame.draw.line(wn,BLACK,(startx,starty),(endx,endy))

    # filled rect
    x=100;y=120;wd=50;h=30
    pygame.draw.rect(wn,RED,(x,y,wd,h))

    # open rect
    x=250;y=240;wd=50;h=30;linewidth=3
    pygame.draw.rect(wn,RED,(x,y,wd,h),linewidth)

    # filled square
    x=300;y=80;wd=50;h=50
    pygame.draw.rect(wn,GREEN,(x,y,wd,h))

    # filled circle
    x=200;y=150;rad=20
    pygame.draw.circle(wn,BLUE,(x,y),rad)

    # open circle
    x=200;y=300;rad=20;wd=3
    pygame.draw.circle(wn,BLUE,(x,y),rad,wd)

    # filled elliipse
    x=350;y=260;wd=60;h=40
    pygame.draw.ellipse(wn,PURPLE,(x,y,wd,h))

    # arc. This is an elliptical arc
    x=100;y=260;wd=60;h=40;startangle=0;endangle=math.pi/2;linewidth=5
    pygame.draw.arc(wn,GREEN,(x,y,wd,h),startangle,endangle,linewidth)

    # open triangle
    x1=200;y1=100;x2=120;y2=200;x3=280;y3=180;wd=5
    pygame.draw.polygon(wn,CYAN,[[x1,y1],[x2,y2],[x3,y3]],wd)

    pygame.display.update()
    clock.tick(30)

# Line



# pygame quit
pygame.quit()
quit()
