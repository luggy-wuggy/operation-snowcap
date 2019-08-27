from set_Circles import Platform, Button, randRGB, Circle, SetCircles, start_game, start_menu
import pygame
import random

pygame.init()
worldx = 400
worldy = 700
world = pygame.display.set_mode((worldx,worldy))
pygame.display.set_caption("Color Game")

def end_screen(world, score):

	scoreString = str(score)

	endText = Button((0,0,0), (10, 120), (380,65), (255,255,255), 'You scored: ')
	end_score = Button((0,0,0), (10, 190), (380,65), (255,255,255), scoreString)

	play_again = Button((30,200,60), (74, 320) , (260, 80), (0,0,0),  'Play\nAgain')
	end_game = Button((255,30,50), (74, 450) , (260, 80), (0,0,0),  'No')


	end_menu = True
	while end_menu:
		world.fill((0,0,0))
		endText.text_word(world)
		end_score.text_word(world)
		play_again.draw(world)
		end_game.draw(world)

		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()

			if event.type == pygame.QUIT:
				end_menu = False
				pygame.quit()
				quit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if play_again.isOver(pos):
					end_menu = False
				if end_game.isOver(pos): 
					end_menu = False
					pygame.quit()
					quit()

			elif event.type == pygame.MOUSEMOTION:
				if play_again.isOver(pos): play_again.color = (0,255,0)
				else: play_again.color = (0, 180, 0)

				if end_game.isOver(pos): end_game.color = (255,0,0)
				else: end_game.color = (180,0,0)


		pygame.display.update()

end_screen(world, 3)




