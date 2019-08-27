from set_Circles import Platform, Button, randRGB, Circle, SetCircles, start_game, start_menu, end_screen
import pygame
import random

####### SET UP CODE ########
pygame.init()
worldx = 400
worldy = 700
world = pygame.display.set_mode((worldx,worldy))
pygame.display.set_caption("Color Game")
############################

######## MAIN LOOP #########

start_menu(world)
score = start_game(world)
end_screen(world, score)


############################
