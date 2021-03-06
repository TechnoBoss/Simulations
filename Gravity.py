import pygame, sys, math, random
from pygame.locals import *
from Vectors_exp import Point, Vect, dist

fpsclock = pygame.time.Clock()
Black = (0,0,0)
White = (255,255,255)
LIGHT_BLUE = (5,5,255)
DARK_BLUE = (5,5,155)
BLUE = (0,0,255)
GREEN = (0,255,0)


FPS = 30

pygame.init()
Width, Hieght = 1000, 750
display = (Width, Hieght)
Surf = pygame.display.set_mode(display)

G = 100000
k = 0

class Particle:
	def __init__(self, pos, r = 3):
		self.pos = Point(pos)
		self.r = r
		self.vel = Point((0, 0))
		self.acc = Point((1, 1))


	def attracted(self, target):
		global k
		h = dist(self.pos, target)
		p = (h ** 2) // G or 1
		ang = self.pos.get_angle(target)
		if p > 10:
			p = 10
		px = int(p * math.cos(math.radians(ang))) or 1
		py = int(p * math.sin(math.radians(ang))) or 1

		if self.pos.y < target.y:
			self.acc.y = +abs(py)
		else:
			self.acc.y = -abs(py)

		if self.pos.x < target.x:
			self.acc.x = +abs(px)
		else:
			self.acc.x = -abs(px)

	def update(self):
		self.vel += self.acc
		self.pos += self.vel


	def show(self):
		pygame.draw.circle(Surf, BLUE, self.pos.points, 2)



class Attractor:
	def __init__(self, pos):
		self.pos = Point(pos)

	def show(self):
		pygame.draw.circle(Surf, GREEN, self.pos.points, 3)



def game():
	lis = []
	for i in range(1):
		par = Particle((random.randint(0, Width), random.randint(0, Hieght)))
		lis.append(par)

	Att1 = Attractor((Width//2, Hieght//2))

	
	
	
	# Surf.fill(White)
	while True:
		Surf.fill(White)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				par = Particle(pos)
				lis.append(par)


		Att1.show()
		for par in lis:
			par.show()
			par.attracted(Att1.pos)
			par.update()

		


		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	game()