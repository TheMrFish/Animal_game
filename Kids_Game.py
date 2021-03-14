import pygame
import random, os

pygame.init()

width = 1500
height = 750

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Kids Game")


run = True

tiger = pygame.mixer.Sound('sounds/tiger6.wav')
dog = pygame.mixer.Sound('sounds/bark.wav')
kitten = pygame.mixer.Sound('sounds/a_cat_kitten.wav')
bear = pygame.mixer.Sound('sounds/b_bear.wav')
cat = pygame.mixer.Sound('sounds/c_cat_meow2.wav')
#dog = pygame.mixer.Sound('sounds/d_dog_bark2.wav')
elephant = pygame.mixer.Sound('sounds/e_elephant.wav')
frog = pygame.mixer.Sound('sounds/f_frog.wav')
goat = pygame.mixer.Sound('sounds/g_goat.wav')
horse = pygame.mixer.Sound('sounds/h_horse.wav')
duck = pygame.mixer.Sound('sounds/i_duck_quack.wav')
dogWhine = pygame.mixer.Sound('sounds/j_dog_whine.wav')
dogGrowl = pygame.mixer.Sound('sounds/k_dog_growl3.wav')
lion = pygame.mixer.Sound('sounds/l_lion_roar.wav')
monkey = pygame.mixer.Sound('sounds/m_monkey1.wav')
lionGrowl = pygame.mixer.Sound('sounds/n_lion_growl.wav')
owl = pygame.mixer.Sound('sounds/o_owl.wav')
pig = pygame.mixer.Sound('sounds/p_pig.wav')
pigSqueal = pygame.mixer.Sound('sounds/q_pig_squeal2.wav')
rooster = pygame.mixer.Sound('sounds/r_rooster.wav')
sheep = pygame.mixer.Sound('sounds/s_sheep521.wav')
chicken = pygame.mixer.Sound('sounds/t_chicken.wav')
sheep2 = pygame.mixer.Sound('sounds/u_sheep.wav')
seagull = pygame.mixer.Sound('sounds/v_seagull2.wav')
wolf = pygame.mixer.Sound('sounds/w_wolf_howl.wav')
piggy = pygame.mixer.Sound('sounds/x_pig3.wav')
piggySqueal = pygame.mixer.Sound('sounds/y_pig_squeal.wav')
monkey2 = pygame.mixer.Sound('sounds/z_monkey2.wav')

def left():
	if keys[pygame.K_a]:
		if pygame.mixer.get_busy() == False:
			dog.play()
			randDog = random.choice(os.listdir("dog"))
			dogPic = pygame.image.load("dog/"+ randDog)
			dogPic = pygame.transform.scale(dogPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(dogPic, (0,0))
				pygame.display.update()

def right():
	if keys[pygame.K_RIGHT]:
		if pygame.mixer.get_busy() == False:
			tiger.play()
			randTiger = random.choice(os.listdir("tiger"))
			tigerPic = pygame.image.load("tiger/"+ randTiger)
			tigerPic = pygame.transform.scale(tigerPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(tigerPic, (0,0))
				pygame.display.update()

def a():
	if keys[pygame.K_a]:
		if pygame.mixer.get_busy() == False:
			kitten.play()
			randCat = random.choice(os.listdir("cat"))
			catPic = pygame.image.load("cat/"+ randCat)
			catPic = pygame.transform.scale(catPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(catPic, (0,0))
				pygame.display.update()
def b():
	if keys[pygame.K_b]:
		if pygame.mixer.get_busy() == False:
			bear.play()
			randBear = random.choice(os.listdir("bear"))
			bearPic = pygame.image.load("bear/"+ randBear)
			bearPic = pygame.transform.scale(bearPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(bearPic, (0,0))
				pygame.display.update()

def c():
	if keys[pygame.K_c]:
		if pygame.mixer.get_busy() == False:
			cat.play()
			randCat = random.choice(os.listdir("cat"))
			catPic = pygame.image.load("cat/"+ randCat)
			catPic = pygame.transform.scale(catPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(catPic, (0,0))
				pygame.display.update()

def d():
	if keys[pygame.K_d]:
		if pygame.mixer.get_busy() == False:
			dog.play()
			randDog = random.choice(os.listdir("dog"))
			dogPic = pygame.image.load("dog/"+ randDog)
			dogPic = pygame.transform.scale(dogPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(dogPic, (0,0))
				pygame.display.update()

def e():
	if keys[pygame.K_e]:
		if pygame.mixer.get_busy() == False:
			elephant.play()
			randElephant = random.choice(os.listdir("elephant"))
			elephantPic = pygame.image.load("elephant/"+ randElephant)
			elephantPic = pygame.transform.scale(elephantPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(elephantPic, (0,0))
				pygame.display.update()

def f():
	if keys[pygame.K_f]:
		if pygame.mixer.get_busy() == False:
			frog.play()
			randFrog = random.choice(os.listdir("frog"))
			frogPic = pygame.image.load("frog/"+ randFrog)
			frogPic = pygame.transform.scale(frogPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(frogPic, (0,0))
				pygame.display.update()

def g():
	if keys[pygame.K_g]:
		if pygame.mixer.get_busy() == False:
			goat.play()
			randGoat = random.choice(os.listdir("goat"))
			goatPic = pygame.image.load("goat/"+ randGoat)
			goatPic = pygame.transform.scale(goatPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(goatPic, (0,0))
				pygame.display.update()

def h():
	if keys[pygame.K_h]:
		if pygame.mixer.get_busy() == False:
			horse.play()
			randHorse = random.choice(os.listdir("horse"))
			horsePic = pygame.image.load("horse/"+ randHorse)
			horsePic = pygame.transform.scale(horsePic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(horsePic, (0,0))
				pygame.display.update()

def i():
	if keys[pygame.K_i]:
		if pygame.mixer.get_busy() == False:
			duck.play()
			randDuck = random.choice(os.listdir("duck"))
			duckPic = pygame.image.load("duck/"+ randDuck)
			duckPic = pygame.transform.scale(duckPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(duckPic, (0,0))
				pygame.display.update()

def j():
	if keys[pygame.K_j]:
		if pygame.mixer.get_busy() == False:
			dogWhine.play()
			randDog = random.choice(os.listdir("dog"))
			dogPic = pygame.image.load("dog/"+ randDog)
			dogPic = pygame.transform.scale(dogPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(dogPic, (0,0))
				pygame.display.update()

def k():
	if keys[pygame.K_k]:
		if pygame.mixer.get_busy() == False:
			dogGrowl.play()
			randDog = random.choice(os.listdir("dog"))
			dogPic = pygame.image.load("dog/"+ randDog)
			dogPic = pygame.transform.scale(dogPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(dogPic, (0,0))
				pygame.display.update()

def l():
	if keys[pygame.K_l]:
		if pygame.mixer.get_busy() == False:
			lion.play()
			randLion = random.choice(os.listdir("lion"))
			lionPic = pygame.image.load("lion/"+ randLion)
			lionPic = pygame.transform.scale(lionPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(lionPic, (0,0))
				pygame.display.update()

def m():
	if keys[pygame.K_m]:
		if pygame.mixer.get_busy() == False:
			monkey.play()
			randMonkey = random.choice(os.listdir("monkey"))
			monkeyPic = pygame.image.load("monkey/"+ randMonkey)
			monkeyPic = pygame.transform.scale(monkeyPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(monkeyPic, (0,0))
				pygame.display.update()

def n():
	if keys[pygame.K_n]:
		if pygame.mixer.get_busy() == False:
			lionGrowl.play()
			randLion = random.choice(os.listdir("lion"))
			lionPic = pygame.image.load("lion/"+ randLion)
			lionPic = pygame.transform.scale(lionPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(lionPic, (0,0))
				pygame.display.update()

def o():
	if keys[pygame.K_o]:
		if pygame.mixer.get_busy() == False:
			owl.play()
			randOwl = random.choice(os.listdir("owl"))
			owlPic = pygame.image.load("owl/"+ randOwl)
			owlPic = pygame.transform.scale(owlPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(owlPic, (0,0))
				pygame.display.update()

def p():
	if keys[pygame.K_p]:
		if pygame.mixer.get_busy() == False:
			pig.play()
			randPig = random.choice(os.listdir("pig"))
			pigPic = pygame.image.load("pig/"+ randPig)
			pigPic = pygame.transform.scale(pigPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(pigPic, (0,0))
				pygame.display.update()

def q():
	if keys[pygame.K_q]:
		if pygame.mixer.get_busy() == False:
			pigSqueal.play()
			randPig = random.choice(os.listdir("pig"))
			pigPic = pygame.image.load("pig/"+ randPig)
			pigPic = pygame.transform.scale(pigPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(pigPic, (0,0))
				pygame.display.update()

def r():
	if keys[pygame.K_r]:
		if pygame.mixer.get_busy() == False:
			rooster.play()
			randRooster = random.choice(os.listdir("rooster"))
			roosterPic = pygame.image.load("rooster/"+ randRooster)
			roosterPic = pygame.transform.scale(roosterPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(roosterPic, (0,0))
				pygame.display.update()

def s():
	if keys[pygame.K_s]:
		if pygame.mixer.get_busy() == False:
			sheep.play()
			randSheep = random.choice(os.listdir("sheep"))
			sheepPic = pygame.image.load("sheep/"+ randSheep)
			sheepPic = pygame.transform.scale(sheepPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(sheepPic, (0,0))
				pygame.display.update()

def t():
	if keys[pygame.K_t]:
		if pygame.mixer.get_busy() == False:
			chicken.play()
			randChicken = random.choice(os.listdir("chicken"))
			chickenPic = pygame.image.load("chicken/"+ randChicken)
			chickenPic = pygame.transform.scale(chickenPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(chickenPic, (0,0))
				pygame.display.update()

def u():
	if keys[pygame.K_u]:
		if pygame.mixer.get_busy() == False:
			sheep2.play()
			randSheep = random.choice(os.listdir("sheep"))
			sheepPic = pygame.image.load("sheep/"+ randSheep)
			sheepPic = pygame.transform.scale(sheepPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(sheepPic, (0,0))
				pygame.display.update()

def v():
	if keys[pygame.K_v]:
		if pygame.mixer.get_busy() == False:
			seagull.play()
			randSeagull = random.choice(os.listdir("seagull"))
			seagullPic = pygame.image.load("seagull/"+ randSeagull)
			seagullPic = pygame.transform.scale(seagullPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(seagullPic, (0,0))
				pygame.display.update()

def w():
	if keys[pygame.K_w]:
		if pygame.mixer.get_busy() == False:
			wolf.play()
			randWolf = random.choice(os.listdir("wolf"))
			wolfPic = pygame.image.load("wolf/"+ randWolf)
			wolfPic = pygame.transform.scale(wolfPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(wolfPic, (0,0))
				pygame.display.update()
def x():
	if keys[pygame.K_x]:
		if pygame.mixer.get_busy() == False:
			pig.play()
			randPig = random.choice(os.listdir("pig"))
			pigPic = pygame.image.load("pig/"+ randPig)
			pigPic = pygame.transform.scale(pigPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(pigPic, (0,0))
				pygame.display.update()

def y():
	if keys[pygame.K_y]:
		if pygame.mixer.get_busy() == False:
			piggySqueal.play()
			randPig = random.choice(os.listdir("pig"))
			pigPic = pygame.image.load("pig/"+ randPig)
			pigPic = pygame.transform.scale(pigPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(pigPic, (0,0))
				pygame.display.update()

def z():
	if keys[pygame.K_z]:
		if pygame.mixer.get_busy() == False:
			monkey2.play()
			randMonkey = random.choice(os.listdir("monkey"))
			monkeyPic = pygame.image.load("monkey/"+ randMonkey)
			monkeyPic = pygame.transform.scale(monkeyPic, (1500, 750))
			while pygame.mixer.get_busy() == True:
				win.blit(monkeyPic, (0,0))
				pygame.display.update()



while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	left()
	right()
	a()
	b()
	c()
	d()
	e()
	f()
	g()
	h()
	i()
	j()
	k()
	l()
	m()
	n()
	o()
	p()
	q()
	r()
	s()
	t()
	u()
	v()
	w()
	x()
	y()
	z()

	win.fill((0,0,0))		
	pygame.display.update()

pygame.quit()