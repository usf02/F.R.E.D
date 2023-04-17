import pygame
import sys

pygame.init()
width = 1500
height = 600
screen = pygame.display.set_mode((width,height))

Titlefont = pygame.font.Font("Font.ttf", 150)
gamefont = pygame.font.Font("Font.ttf", 30)

Title = Titlefont.render("Fred" , True , (255,255,255))
textquit = gamefont.render("Quit" , True , (255,255,255))
textstart = gamefont.render("Start", True , (255,255,255))
textmenu = gamefont.render("Menü", True , (255,255,255))


while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type  == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 650 <= mouse[0] <= 850 and 430 <= mouse[1] <= 480 :
                sys.exit()

    screen.fill((65, 65, 65))

    mouse = pygame.mouse.get_pos()

    #if 650 <= mouse[0] <= 850 and 275 <= mouse[1] <= 325 :
    if 650 <= mouse[0] <= 850 and 270 <= mouse[1] <= 320:
        pygame.draw.rect(screen,(50,50,50),(650,270,200,50))
    else :
        pygame.draw.rect(screen, (170, 170, 170), (650, 270, 200, 50))

    if 650 <= mouse[0] <= 850 and 350 <= mouse[1] <= 400:
        pygame.draw.rect(screen, (50, 50, 50), (650, 350 , 200, 50))
    else:
        pygame.draw.rect(screen, (170, 170, 170), (650, 350, 200, 50))

    if 650 <= mouse[0] <= 850 and 430 <= mouse[1] <= 480:
        pygame.draw.rect(screen, (50, 50, 50), (650, 430 , 200, 50))
    else:
        pygame.draw.rect(screen, (170, 170, 170), (650, 430, 200, 50))


    screen.blit(Title, (575, 50))
    screen.blit(textstart, (709, 280))
    screen.blit(textmenu, (717, 360))
    screen.blit(textquit,(719,440))


    pygame.display.update()
