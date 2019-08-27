import pygame
import random
score = 0


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

class HitBox(object):

	def __init__(self,circle):
		self.circle = circle.getPositionCircle()
		self.hitbox = (self.circle[0]-50, self.circle[1]-50, 100, 100)

	def draw(self):
		self.hitbox = (self.circle[0]-50, self.circle[1]-50, 100, 100)
		pygame.draw.rect(world, (255,0,0), self.hitbox, 2)

	def getPositionHitBox(self):
		return self.circle

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
		return self.position

def drawHitBox(circle):
	hit = HitBox(circle)
	hit.draw()
	return hit.getPositionHitBox()

def randRGB():
	rgb = [random.randrange(0,256), random.randrange(0,256), random.randrange(0,256)]
	new_RGB = [color+20 for color in rgb]

	for color in range(3):
		if new_RGB[color] > 255:
			new_RGB[color] = rgb[color]

	return (rgb, new_RGB)

def collision(hitbox_pos, platform, select):
	if select == 1:
		if(platform.getPosition() == [28,600] and hitbox_pos == [80,565]):
			return True

		elif(platform.getPosition()[1] == 600 and hitbox_pos[1] == 565):
			print("FAIL")

	elif select == 2:
		if(platform.getPosition() == [148,600] and hitbox_pos == [200, 565]):
			return True

		elif(platform.getPosition()[1] == 600 and hitbox_pos[1] == 565):
			print("FAIL")

	elif select == 3:
		if(platform.getPosition() == [268,600] and hitbox_pos == [320, 565]):
			return True

		elif(platform.getPosition()[1] == 600 and hitbox_pos[1] == 565):
			print("FAIL")

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







##################################


if __name__ == '__main__':
	######### Set Up Code ############
	pygame.init()

	worldx = 400
	worldy = 700
	rgb = randRGB()[0]
	world = pygame.display.set_mode((worldx,worldy))
	pygame.display.set_caption("Color Game")

	firstCircle = Circle(rgb,world,[80,-60])
	secondCircle = Circle(rgb,world,[200,-60])
	thirdCircle = Circle(rgb,world,[320,-60])

	game_platform = Platform(world, [148,600])

	##################################


	########## Main Loop #############
	gameplay = True
	circle_select = random.randrange(1,4)

	while gameplay:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				gameplay = False

			elif event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LEFT:

					if game_platform.getPosition()[0] == 148:
						game_platform.Left()
					elif game_platform.getPosition()[0] == 268:
						game_platform.Center()

				if event.key == pygame.K_RIGHT:

					if game_platform.getPosition()[0] == 148:
						game_platform.Right()
					elif game_platform.getPosition()[0] == 28:
						game_platform.Center()


		world.fill((0,0,0))
		if(firstCircle.getPositionCircle()[1] != 565):
			firstCircle.loop(rgb)
			secondCircle.loop(rgb)
			thirdCircle.loop(rgb)
			pygame.display.update()
		else:
			RGB = randRGB()
			circle_select = random.randrange(1,4)
			if circle_select == 1:
				firstCircle.go_back(RGB[1])
				secondCircle.go_back(RGB[0])
				thirdCircle.go_back(RGB[0])

			elif circle_select == 2:
				firstCircle.go_back(RGB[0])
				secondCircle.go_back(RGB[1])
				thirdCircle.go_back(RGB[0])
			else:
				firstCircle.go_back(RGB[0])
				secondCircle.go_back(RGB[0])
				thirdCircle.go_back(RGB[1])

		if circle_select == 1:
			hitbox_pos = drawHitBox(firstCircle)
			if collision(hitbox_pos, game_platform, circle_select):
				score += 1
				print(score)

		elif circle_select == 2:
			hitbox_pos = drawHitBox(secondCircle)
			if collision(hitbox_pos, game_platform, circle_select):
				score += 1
				print(score)
		else:
			hitbox_pos = drawHitBox(thirdCircle)
			if collision(hitbox_pos, game_platform, circle_select):
				score += 1
				print(score)



		game_platform.draw()
		pygame.display.update()


	pygame.quit()
	###################################

