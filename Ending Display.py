import pygame
import sys
from pygame.locals import *

#basic screen size
pygame.init()
width = 1500
height = 600
screen = pygame.display.set_mode((width,height))

#our font for message
messagefont = pygame.font.Font("Font.ttf", 150)
messagefont2 = pygame.font.Font("Font.ttf", 30)

#3 message for r and m button, YOU DIED

message = messagefont.render("YOU DIED",True,(255,0,0))
message2 = messagefont2.render("- Press R to Restart -",True,(255,255,255))
message3 = messagefont2.render("- Press M to go to Main Menu -" ,True, (255,255,255))

#letter one by one animation def
def display_text_animation(string):
    text = ""
    for i in range(len(string)):
        screen.fill((65,65,65))
        text = text + string[i]
        message = messagefont.render(text,True,(255,0,0))
        text_rect = message.get_rect()
        text_rect.center = (752, 166)
        screen.blit(message,text_rect)
        pygame.display.update()
        pygame.time.wait(150)
display_text_animation("YOU DIED")


while True :



    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type  == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
            sys.exit()



    screen.fill((65, 65, 65))


    screen.blit(message, (400, 100))
    screen.blit(message2, (560, 420))
    screen.blit(message3, (488,510))
    pygame.display.update()


