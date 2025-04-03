import pygame
def main():

    pygame.init()
    screen_width,screen_height=500,500
    screen=pygame.display.set_mode((screen_height,screen_width))
    pygame.display.set_caption("Color changing sprite")

    colors={
        "red":pygame.Colour('red'),
        "green":pygame.Colour('green'),
        "blue":pygame.Colour('blue'),
        "yellow":pygame.Colour('yellow'),
        "white":pygame.Colour('white'),
    }
    current_colour=colors['white']

    x,y=30,30
    sporite_width,sprite_height=60,60
    clock=pygame.time.Clock()
    done=False

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               done=True
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:x-=3  
        if pressed[pygame.K_RIGHT]:x+=3 
        if pressed[pygame.K_UP]:x-=3 
        if pressed[pygame.K_DOWN]:x+=3

        x=min(max(0,x),screen_width-sporite_width)
        y=min(max(0,y),screen_height-sprite_height)

        if x==0:current_colour=colors['blue']
        elif x==screen_width-sporite_width:current_colour=colors['yellow']
        elif y==0:current_colour=colors['red']
        elif y==screen_height-sprite_height:current_colour=colors['green']
        else:
            current_colour=colors['white']
        screen.fill((0,0,0))
        pygame.draw.rect(screen,current_colour,
                         (x,y,sporite_width,sprite_height))
        pygame.display.flip()
        clock.tick(90)    
    pygame.quit()
if __name__=="__main__":
    main()

    


