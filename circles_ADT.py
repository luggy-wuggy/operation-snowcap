import pygame
import random
####### Objects/Functions ########

class Platform(object):

	def __init__(self,world,position):
		self.position = position
		self.world = world

	def draw(self):
		x = self.position[0]
		y = self.position[1]
		width = 100
		height = 20
		pygame.draw.rect(self.world, (255,255,255), (x,y,width,height))

	def Left(self):
		self.position[0] = 28

	def Right(self):
		self.position[0] = 268

	def Center(self):
		self.position[0] = 148

	def getPosition(self):
		return self.position

class Circle(object):

	def __init__(self,rgb,world,position):
		self.rgb = rgb
		self.world = world
		self.position = position

	def draw(self):
		pygame.draw.circle(self.world, self.rgb, self.position, 55)

	def move(self):
		self.position[1] += 5

	def loop(self, rgb):
		self.draw()
		self.move()
		
	def go_back(self, rgb, loc = -60):
		self.rgb = rgb
		self.position[1] = loc

	def setColor (self, rgb):
		self.rgb = rgb

	def getPositionCircle(self):
		return self.position[1]

def randRGB():
	rgb = [random.randrange(0,256), random.randrange(0,256), random.randrange(0,256)]
	new_RGB = [color+20 for color in rgb]

	for color in range(3):
		if new_RGB[color] > 255:
			new_RGB[color] = rgb[color]

	return (rgb, new_RGB)

class SetCircles(object):
	def __init__(self, world, y_position):
		circle_select = random.randrange(1,4)
		rgb = randRGB()
		if circle_select == 1:
			self.circle_1 = Circle(rgb[1], world, [80,y_position])
			self.circle_2 = Circle(rgb[0], world, [200, y_position])
			self.circle_3 = Circle(rgb[0], world, [320, y_position])
		elif circle_select == 2:
			self.circle_1 = Circle(rgb[0], world, [80,y_position])
			self.circle_2 = Circle(rgb[1], world, [200, y_position])
			self.circle_3 = Circle(rgb[0], world, [320, y_position])
		elif circle_select == 3:
			self.circle_1 = Circle(rgb[0], world, [80,y_position])
			self.circle_2 = Circle(rgb[0], world, [200, y_position])
			self.circle_3 = Circle(rgb[1], world, [320, y_position])	

		self.circle_position = circle_select

	def draw_set(self):
		self.circle_1.draw()
		self.circle_2.draw()
		self.circle_3.draw()

	def move_set(self):
		newRGB = randRGB()[0]
		if self.circle_1.position[1] != 565:
			self.circle_1.draw()
			self.circle_2.draw()
			self.circle_3.draw()
			self.circle_1.move()
			self.circle_2.move()
			self.circle_3.move()
		else:
			self.color_set()
			self.circle_1.position[1] = -60
			self.circle_2.position[1] = -60
			self.circle_3.position[1] = -60

	def color_set(self):
		circle_select = random.randrange(1,4)
		newRGB = randRGB()
		if circle_select == 1:
			self.circle_1.setColor(newRGB[1])
			self.circle_2.setColor(newRGB[0])
			self.circle_3.setColor(newRGB[0])
		elif circle_select == 2:
			self.circle_1.setColor(newRGB[0])
			self.circle_2.setColor(newRGB[1])
			self.circle_3.setColor(newRGB[0])
		elif circle_select == 3:
			self.circle_1.setColor(newRGB[0])
			self.circle_2.setColor(newRGB[0])
			self.circle_3.setColor(newRGB[1])

		self.circle_position = circle_select

	def colored_position(self, platform_position):
		if self.circle_1.getPositionCircle() >= 565:
			if self.circle_position == 1:
				if platform_position == [28,600] and self.circle_1.position[0] == 80:
					return 1
				else:
					return 0

			elif self.circle_position == 2:
				if platform_position == [148,600] and self.circle_2.position[0] == 200:
					return 1
				else:
					return 0

			elif self.circle_position == 3:
				if platform_position == [268, 600] and self.circle_3.position[0] == 320:
					return 1
				else:
					return 0

class Button():
	def __init__(self, color, coordinates, size , font_color = (0,0,0),  text=''):
		self.color = color
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.width = size[0]
		self.height = size[1]
		self.text = text
		self.font_color = font_color

	def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
		if outline:
			pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
		
		pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
		if self.text != '':
			font = pygame.font.SysFont('chalkboardsettc', 55)
			text = font.render(self.text, 1, self.font_color)
			win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
	def text_word(self, win):
		font = pygame.font.SysFont('chalkboardsettc', 55)
		text = font.render(self.text, 1, self.font_color)
		win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	def isOver(self, pos):
		#Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False

	def changeText(self, newText):
		newText =str(newText)
		self.text = newText

def start_menu(world):
	menu_platform = Platform(world, [148,500])
	menu_circle_set = SetCircles(world, -60)
	menu_circle_set_1 = SetCircles(world, -380)

	start_button = Button((30,200,60), (74, 560) , (250, 100), (0,0,0),  'Ready')
	title = Button((0,0,0), (10, 75), (380,65), (255,255,255), 'Colored Circles')

	score = 0
	main_menu = True

	while main_menu:
		world.fill((0,0,0))
		menu_circle_set.move_set()
		menu_circle_set_1.move_set()
		start_button.draw(world, (0,0,0))
		title.text_word(world)

		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()

			if event.type == pygame.QUIT:
				main_menu = False
				pygame.quit()
				quit()

			elif event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LEFT:

					if menu_platform.getPosition()[0] == 148: menu_platform.Left()
					elif menu_platform.getPosition()[0] == 268: menu_platform.Center()

				if event.key == pygame.K_RIGHT:

					if menu_platform.getPosition()[0] == 148: menu_platform.Right()
					elif menu_platform.getPosition()[0] == 28: menu_platform.Center()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if start_button.isOver(pos): main_menu = False

			elif event.type == pygame.MOUSEMOTION:
				if start_button.isOver(pos): start_button.color = (0,255,0)
				else: start_button.color = (0, 155,0 )

		menu_platform.draw()
		pygame.display.update()


def start_game(world):
		circle_set = SetCircles(world, -60)
		circle_set_1 = SetCircles(world, -380)

		game_platform = Platform(world, [148,600])
		scoreText = Button((0,0,0), (25,630), (180,50), (255,255, 255), 'Score: ')
		scoreNumber = Button((0,0,0), (175,632), (70,50), (255,255, 255), '0')

		score = 0
		gameplay = True
		while gameplay:
			world.fill((0,0,0))
			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					gameplay = False

				elif event.type == pygame.KEYDOWN:

					if event.key == pygame.K_LEFT:
						if game_platform.getPosition()[0] == 148: game_platform.Left()
						elif game_platform.getPosition()[0] == 268: game_platform.Center()

					if event.key == pygame.K_RIGHT:
						if game_platform.getPosition()[0] == 148: game_platform.Right()
						elif game_platform.getPosition()[0] == 28: game_platform.Center()

			circle_set.move_set()
			circle_set_1.move_set()

			first_set = circle_set.colored_position(game_platform.getPosition())
			second_set = circle_set_1.colored_position(game_platform.getPosition())

			if first_set == 1 or second_set == 1:
				score += 1
				scoreNumber.changeText(score)
			elif first_set == 0 or second_set == 0:
				gameplay = False
		
			scoreText.draw(world)
			scoreNumber.draw(world)
			game_platform.draw()

			pygame.display.update()

		return score

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
				main_menu = False
				pygame.quit()
				quit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if play_again.isOver(pos): end_menu = False
				if end_game.isOver(pos): end_menu = False

			elif event.type == pygame.MOUSEMOTION:
				if play_again.isOver(pos): play_again.color = (0,255,0)
				else: play_again.color = (0, 180, 0)

				if end_game.isOver(pos): end_game.color = (255,0,0)
				else: end_game.color = (180,0,0)


		pygame.display.update()

	pygame.quit()


##################################
if __name__ == '__main__':
######### Set Up Code ############
	pygame.init()
	worldx = 400
	worldy = 700
	world = pygame.display.set_mode((worldx,worldy))
	pygame.display.set_caption("Color Game")



