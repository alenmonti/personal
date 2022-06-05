import pygame
from sys import exit
from random import randint , choices


class Bruja(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#stand
		bruja_stand_1 = pygame.transform.scale2x(pygame.image.load('bruja/bruja_stand1.png')).convert_alpha()
		bruja_stand_2 = pygame.transform.scale2x(pygame.image.load('bruja/bruja_stand2.png')).convert_alpha()
		bruja_stand_3 = pygame.transform.scale2x(pygame.image.load('bruja/bruja_stand3.png')).convert_alpha()
		bruja_stand_4 = pygame.transform.scale2x(pygame.image.load('bruja/bruja_stand4.png')).convert_alpha()
		bruja_stand_5 = pygame.transform.scale2x(pygame.image.load('bruja/bruja_stand5.png')).convert_alpha()
		bruja_stand_1_flip = pygame.transform.flip(bruja_stand_1,True,False).convert_alpha()
		bruja_stand_2_flip = pygame.transform.flip(bruja_stand_2,True,False).convert_alpha()
		bruja_stand_3_flip = pygame.transform.flip(bruja_stand_3,True,False).convert_alpha()
		bruja_stand_4_flip = pygame.transform.flip(bruja_stand_4,True,False).convert_alpha()
		bruja_stand_5_flip = pygame.transform.flip(bruja_stand_5,True,False).convert_alpha()
		self.stand = [bruja_stand_1, bruja_stand_2, bruja_stand_3, bruja_stand_4, bruja_stand_5]
		self.stand_flip = [bruja_stand_1_flip, bruja_stand_2_flip, bruja_stand_3_flip, bruja_stand_4_flip, bruja_stand_5_flip]
		self.stand_index = 0

		#run
		bruja_run_1 = pygame.transform.scale2x(pygame.image.load('bruja_run/bruja_run_1.png')).convert_alpha()
		bruja_run_2 = pygame.transform.scale2x(pygame.image.load('bruja_run/bruja_run_2.png')).convert_alpha()
		bruja_run_3 = pygame.transform.scale2x(pygame.image.load('bruja_run/bruja_run_3.png')).convert_alpha()
		bruja_run_4 = pygame.transform.scale2x(pygame.image.load('bruja_run/bruja_run_4.png')).convert_alpha()
		bruja_run_5 = pygame.transform.scale2x(pygame.image.load('bruja_run/bruja_run_5.png')).convert_alpha()
		bruja_run_6 = pygame.transform.scale2x(pygame.image.load('bruja_run/bruja_run_6.png')).convert_alpha()
		bruja_run_7 = pygame.transform.scale2x(pygame.image.load('bruja_run/bruja_run_7.png')).convert_alpha()
		bruja_run_8 = pygame.transform.scale2x(pygame.image.load('bruja_run/bruja_run_8.png')).convert_alpha()
		bruja_run_1_flip = pygame.transform.flip(bruja_run_1,True,False).convert_alpha()
		bruja_run_2_flip = pygame.transform.flip(bruja_run_2,True,False).convert_alpha()
		bruja_run_3_flip = pygame.transform.flip(bruja_run_3,True,False).convert_alpha()
		bruja_run_4_flip = pygame.transform.flip(bruja_run_4,True,False).convert_alpha()
		bruja_run_5_flip = pygame.transform.flip(bruja_run_5,True,False).convert_alpha()
		bruja_run_6_flip = pygame.transform.flip(bruja_run_6,True,False).convert_alpha()
		bruja_run_7_flip = pygame.transform.flip(bruja_run_7,True,False).convert_alpha()
		bruja_run_8_flip = pygame.transform.flip(bruja_run_8,True,False).convert_alpha()
		self.run = [bruja_run_1, bruja_run_2, bruja_run_3, bruja_run_4, bruja_run_5, bruja_run_6, bruja_run_7, bruja_run_8]
		self.run_flip = [bruja_run_1_flip, bruja_run_2_flip, bruja_run_3_flip, bruja_run_4_flip, bruja_run_5_flip, bruja_run_6_flip, bruja_run_7_flip, bruja_run_8_flip]
		self.run_index = 0

		#ataque
		bruja_atq_1 = pygame.transform.scale2x(pygame.image.load('bruja_atq/bruja_atq_1.png')).convert_alpha()
		bruja_atq_2 = pygame.transform.scale2x(pygame.image.load('bruja_atq/bruja_atq_2.png')).convert_alpha()
		bruja_atq_3 = pygame.transform.scale2x(pygame.image.load('bruja_atq/bruja_atq_3.png')).convert_alpha()
		bruja_atq_4 = pygame.transform.scale2x(pygame.image.load('bruja_atq/bruja_atq_4.png')).convert_alpha()
		bruja_atq_5 = pygame.transform.scale2x(pygame.image.load('bruja_atq/bruja_atq_5.png')).convert_alpha()
		bruja_atq_1_flip = pygame.transform.flip(bruja_atq_1,True,False).convert_alpha()
		bruja_atq_2_flip = pygame.transform.flip(bruja_atq_2,True,False).convert_alpha()
		bruja_atq_3_flip = pygame.transform.flip(bruja_atq_3,True,False).convert_alpha()
		bruja_atq_4_flip = pygame.transform.flip(bruja_atq_4,True,False).convert_alpha()
		bruja_atq_5_flip = pygame.transform.flip(bruja_atq_5,True,False).convert_alpha()
		self.atq = [bruja_atq_1, bruja_atq_2, bruja_atq_3, bruja_atq_4, bruja_atq_5]
		self.atq_flip = [bruja_atq_1_flip, bruja_atq_2_flip, bruja_atq_3_flip, bruja_atq_4_flip, bruja_atq_5_flip]
		self.atq_index = 0
		self.ataque = 0
		self.ataque_e = 0
		self.ataque_r = 0

		#estados
		self.flip_state = 0
		self.velocidad = [0, 0]
		self.atq_realizado = 0
		self.ajustar_rec = 0
		self.inmune = 0
		self.doble = 0

		#estadisticas
		self.stat_velocidad = 5
		self.stat_atq_vel = 0.15

		#autotimer
		self.pickup_timer = 0

		#imagen
		self.image = self.stand[self.stand_index]
		self.rect = self.image.get_rect(midbottom=(382,200))
		self.mask = pygame.mask.from_surface(self.image)
		

	def animacion(self):
		#ataque
		if self.ataque:
			#reiniciar animaciones 
			self.stand_index, self.run_index = 0, 0

			#animacion actual
			self.atq_index += self.stat_atq_vel
			if self.atq_index >= len(self.atq):
				self.atq_index = 0
				self.atq_realizado = 0

			#direccion	
			if self.flip_state:
				self.image = self.atq_flip[int(self.atq_index)]
				self.mask = pygame.mask.from_surface(self.image)
			else:
				self.image = self.atq[int(self.atq_index)]
				self.mask = pygame.mask.from_surface(self.image)

			#ajustar rec	
			if self.ajustar_rec:
				self.rect = self.image.get_rect(topleft = (self.rect.x-18,self.rect.y-12))
				self.ajustar_rec = 0

		#correr	
		elif self.velocidad != [0, 0]:
			#ajustar rec

			#animacion actual	
			self.run_index +=0.12
			if self.run_index >= len(self.run): self.run_index = 0

			#direccion
			if self.flip_state:
				self.image = self.run_flip[int(self.run_index)]
				self.mask = pygame.mask.from_surface(self.image)
			else:
				self.image = self.run[int(self.run_index)]
				self.mask = pygame.mask.from_surface(self.image)

			if not self.ajustar_rec:
				self.rect = self.image.get_rect(topleft = (self.rect.x+18, self.rect.y+12))


		#parado
		else:

			#ajustar rec
			
			#animacion actual
			self.stand_index +=0.12
			if self.stand_index >= len(self.stand):	self.stand_index = 0

			#direccion
			if self.flip_state:
				self.image = self.stand_flip[int(self.stand_index)]
				self.mask = pygame.mask.from_surface(self.image)
			else:
				self.image = self.stand[int(self.stand_index)]
				self.mask = pygame.mask.from_surface(self.image)
			if not self.ajustar_rec:
				self.rect = self.image.get_rect(topleft = (self.rect.x+18, self.rect.y+12))

	def input_usuario(self):
		teclas = pygame.key.get_pressed()

		#ataque rapido
		if teclas[pygame.K_e] and self.ataque_e == 0:
				self.ataque_e = 10
		if teclas[pygame.K_r] and self.ataque_r == 0:
			self.ataque_r = 20
		#ataque cargado
		if teclas[pygame.K_q] :
			self.ataque = 1
			self.velocidad = [0, 0]


		else:
			#reiniciar estados de ataque
			self.ataque = 0
			self.atq_index = 0
			self.atq_realizado = 0

			#movimiento
			if teclas[pygame.K_UP] or teclas[pygame.K_w]:
				self.velocidad[1] = -self.stat_velocidad
			elif teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
				self.velocidad[1] = self.stat_velocidad
			else:
				self.velocidad[1] = 0
			if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
				self.flip_state = 1
				self.velocidad[0] = -self.stat_velocidad
			elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
				self.flip_state = 0
				self.velocidad[0] = self.stat_velocidad
			else:
				self.velocidad[0] = 0
		
	def ejecutar_acciones(self):
		#lanzar ataque cargado
		if int(self.atq_index) == len(self.atq)-1 and not self.atq_realizado: 
			pygame.event.post(pygame.event.Event(pygame.USEREVENT+1, pos = self.rect.midleft, flip = self.flip_state * 180, play = True))
			self.atq_realizado = 1
			if self.doble:
				pygame.event.post(pygame.event.Event(pygame.USEREVENT+1, pos = (self.rect.left, self.rect.centery + 20), flip = self.flip_state*180, play = False))
		
		#lanzar ataque rapido
		if self.ataque_e == 10:
			pygame.event.post(pygame.event.Event(pygame.USEREVENT+3, pos = self.rect.midleft, flip = 0, play = True))
			pygame.event.post(pygame.event.Event(pygame.USEREVENT+3, pos = self.rect.midleft, flip = 180, play = False))

		if self.ataque_r == 20:
			pygame.event.post(pygame.event.Event(pygame.USEREVENT+1, pos = self.rect.midleft, flip = 'all', play = True))

		#cooldown ataque rapido	
		if self.ataque_e > 0:
			self.ataque_e -= 0.016
		elif self.ataque_e < 0:
			self.ataque_e = 0

		if self.ataque_r > 0:
			self.ataque_r -= 0.016
		elif self.ataque_r < 0:
			self.ataque_r = 0

		#ajuste de rec
		if not self.ajustar_rec and (self.run_index or self.stand_index):
			self.ajustar_rec = 1

		#movimiento
		self.rect.x += self.velocidad[0]
		self.rect.y += self.velocidad[1]
		if self.rect.bottom < 0:
			self.rect.midtop = (self.rect.x+20, 400)
		if self.rect.top > 400:
			self.rect.midbottom = (self.rect.x+20,0)
		if self.rect.right < 0:
			self.rect.midleft = (800, self.rect.y+42)
		if self.rect.left > 800:
			self.rect.midright = (0,self.rect.y+42)

		#timer
		if self.pickup_timer:
			print(self.pickup_timer)
			self.pickup_timer -= 0.0166
			if self.pickup_timer < 0:
				self.pickup_timer = 0
		else:
			self.reset_stats()

		#inmunidad
		if self.inmune:
			self.mask.clear()


	def pickup_stats(self, pickup):
		if not pickup:
			return 

		#pickups de velocidad
		elif pickup == 'slow':
			self.stat_velocidad = 2
			self.pickup_timer = 10
		elif pickup == 'fast':
			self.stat_velocidad = 7
			self.pickup_timer = 10
		elif pickup == 'freeze':
			self.stat_velocidad = 0
			self.pickup_timer = 3.5

		#pickups de ataque
		elif pickup == 'ataquedown':
			self.stat_atq_vel = 0.08
			self.pickup_timer = 8

		elif pickup == 'ataqueup':
			self.stat_atq_vel = 0.22
			self.pickup_timer = 10

		#pickups locos
		elif pickup == 'inmune':
			self.inmune = 1
			self.pickup_timer = 7
			return self.inmune
		elif pickup == 'doble':
			self.doble = 1
			self.pickup_timer = 10

	def reset_stats(self):
		self.stat_velocidad = 5
		self.stat_atq_vel = 0.15
		self.inmune = 0
		self.doble = 0




	def update(self, pickup = None):
		self.pickup_stats(pickup)
		self.input_usuario()
		self.animacion()
		self.ejecutar_acciones()

class Spell(pygame.sprite.Sprite):
	def __init__(self, pos, flip):
		super().__init__()
		#fireball
		fireball_1 = pygame.transform.rotate(pygame.transform.scale2x(pygame.image.load('fireball/fireball2_1.png')), flip).convert_alpha()
		fireball_2 = pygame.transform.rotate(pygame.transform.scale2x(pygame.image.load('fireball/fireball2_2.png')), flip).convert_alpha()
		fireball_3 = pygame.transform.rotate(pygame.transform.scale2x(pygame.image.load('fireball/fireball2_3.png')), flip).convert_alpha()
		fireball_4 = pygame.transform.rotate(pygame.transform.scale2x(pygame.image.load('fireball/fireball2_4.png')), flip).convert_alpha()
		self.fireball = [fireball_1,   fireball_2, fireball_3, fireball_4]
		self.flip_state = 1 if 90 < flip < 270 else 0
		self.flip = flip
		self.fireball_index = 0
		self.image = self.fireball[self.fireball_index]

		#direccion
		if self.flip_state:
			self.rect = self.image.get_rect(midright = (pos[0]+120, pos[1]))
		else:
			self.rect = self.image.get_rect(midleft = pos)

	def animacion(self):
		#animacion actual
		self.fireball_index +=0.1
		if self.fireball_index >= len(self.fireball): self.fireball_index = 0
		self.image = self.fireball[int(self.fireball_index)]

	def update(self):
		#movimiento
		if self.flip == 45:
			self.rect.x += 3.5
			self.rect.y -= 3.5
		elif self.flip == 135:
			self.rect.x -= 3.5
			self.rect.y -= 3.5
		elif self.flip == 180:
			self.rect.x -=5
		elif self.flip == 225:
			self.rect.x -= 3.5
			self.rect.y +=3.5
		elif self.flip == 315:
			self.rect.x += 3.5
			self.rect.y += 3.5
		else:
			self.rect.x += 5

		self.animacion()
		self.destroy()
	def destroy(self):

		#limite de pantalla
		if self.rect.x >= 800 or self.rect.right <= 0:
			self.kill()

class Enemy(pygame.sprite.Sprite):
	def __init__(self, flip):
		super().__init__()
		#fungant
		fungant_1 = pygame.transform.scale2x(pygame.image.load('fungant/fungant_1.png').convert_alpha())
		fungant_2 = pygame.transform.scale2x(pygame.image.load('fungant/fungant_2.png').convert_alpha())
		fungant_3 = pygame.transform.scale2x(pygame.image.load('fungant/fungant_3.png').convert_alpha())
		fungant_4 = pygame.transform.scale2x(pygame.image.load('fungant/fungant_4.png').convert_alpha())
		fungant_1_flip = pygame.transform.flip(fungant_1,True,False)
		fungant_2_flip = pygame.transform.flip(fungant_2,True,False)
		fungant_3_flip = pygame.transform.flip(fungant_3,True,False)
		fungant_4_flip = pygame.transform.flip(fungant_4,True,False)
		self.fungant = [fungant_1, fungant_2, fungant_3, fungant_4]
		self.fungant_flip = [fungant_1_flip, fungant_2_flip, fungant_3_flip, fungant_4_flip]
		self.fun_index = 0
		self.flip = flip
		self.velocidad = randint(2,6)

		#direccion y rect
		if self.flip:
			self.image = self.fungant_flip[self.fun_index]
			self.rect = self.image.get_rect(topleft = (800, randint(0,370)))
		else:
			self.image = self.fungant[self.fun_index]
			self.rect = self.image.get_rect(topright = (0, randint(0,370)))

		#mask	
		self.mask = pygame.mask.from_surface(self.image)

	def animacion(self):
		#animacion actual
		self.fun_index += 0.12
		if self.fun_index >= len(self.fungant): self.fun_index = 0

		#direccion
		if self.flip:
			self.image = self.fungant_flip[int(self.fun_index)]
		else:
			self.image = self.fungant[int(self.fun_index)]

	def mover(self):
		#movimiento
		if self.flip:
			self.rect.x -= self.velocidad
		else:
			self.rect.x += self.velocidad

	def destroy(self):
		#limite de pantalla
		if self.flip and self.rect.right < 0:
			self.kill()
		elif not self.flip and self.rect.left > 800:
			self.kill()

	def update(self):
		self.animacion()
		self.mover()
		self.destroy()

class Pickup(pygame.sprite.Sprite):
	def __init__(self, tipo):
		#tipos: 'doble', 'ataquedown', 'ataqueup', 'freeze', 'inmune', 'fast', 'slow' 

		self.tipo = tipo


def ataque_cd(cd_actual):
	if cd_actual > 0:
		cd_actual -= 0.016
	elif cd_actual < 0:
		cd_actual = 0

	return cd_actual

def timer_render(start_time, fuente, color):
	actual_time_s = pygame.time.get_ticks()//1000 - start_time
	m = (actual_time_s//60)%60
	h = (actual_time_s//60)//60
	s = actual_time_s % 60
	timer_surf = fuente.render(f'{h:02d}:{m:02d}:{s:02d}', False, color)
	timer_rect = timer_surf.get_rect(center = (400,40))
	return timer_surf, timer_rect, actual_time_s

def main():
	#inicializar pygame y screen
	pygame.init()
	screen = pygame.display.set_mode((800,400))
	pygame.display.set_caption('Blue Witch')
	fps = pygame.time.Clock()
	icono = pygame.image.load('varios/witch.png').convert()
	pygame.display.set_icon(icono)

	#activo
	game_active = True

	#font
	fuente = pygame.font.Font('font/Pixeltype.ttf', 40)
	fuente_time = pygame.font.Font('font/Pixeltype.ttf', 30)

	#sonidos
	spawn = pygame.mixer.Sound('audio/spawn.wav')
	muerte = pygame.mixer.Sound('audio/muerte.wav')
	restart = pygame.mixer.Sound('audio/restart.wav')
	bg_music = pygame.mixer.music.load('audio/musica.wav')
	bg_music = pygame.mixer.Sound('audio/musica.wav')
	fire = pygame.mixer.Sound('audio/fire.wav')
	kill = pygame.mixer.Sound('audio/kill.wav')
	nextlvl = pygame.mixer.Sound('audio/next.wav')
	fire.set_volume(0.12)
	restart.set_volume(0.4)
	muerte.set_volume(0.8)
	pygame.mixer.music.set_volume(0.2)
	pygame.mixer.music.play(loops = -1)


	#fondo
	fondo_surf 	= pygame.image.load('varios/fondo2.png').convert()
	fondo_rec 	= fondo_surf.get_rect(topleft=(0,0))
	fondo_muerto_surf = pygame.image.load('varios/fondo_muerto.png').convert()
	arbusto_fondo = pygame.image.load('varios/arbustos.png')

	#muerte
	muerte_surf = pygame.transform.scale2x(pygame.image.load('varios/muerte.png')).convert_alpha()
	muerte_rec = muerte_surf.get_rect(center = (400,200))

	#score
	score = 0
	color = (200,200,200)
	score_surf = fuente.render(f'Score: {score}', False, color)
	score_rec = score_surf.get_rect(center = (400,20))
	lvl = 1

	#Bruja
	bruja = pygame.sprite.GroupSingle()
	bruja.add(Bruja())

	#spell
	spells = pygame.sprite.Group()
	spell_event = pygame.event.Event(pygame.USEREVENT+1)
	icon_rap_surf = pygame.image.load('iconos/skill.png').convert()
	iconcd_rap_surf = pygame.image.load('iconos/skillcd.png').convert()
	iconcd_rap_rec = icon_rap_surf.get_rect(midbottom = (350,380))
	icon_fuerte_surf = pygame.image.load('iconos/skill_r.png').convert()
	iconcd_fuerte_surf = pygame.image.load('iconos/skill_r_cd.png').convert()
	iconcd_fuerte_rec = icon_rap_surf.get_rect(midbottom = (450,380))

	#iconos

	icono_freeze = pygame.image.load('iconos/icono_freeze.png').convert_alpha()
	icono_slow = pygame.image.load('iconos/icono_slow.png').convert_alpha()
	icono_fast = pygame.image.load('iconos/icono_fast.png').convert_alpha()
	icono_ataqueup = pygame.image.load('iconos/icono_ataqueup.png').convert_alpha()
	icono_ataquedown = pygame.image.load('iconos/icono_ataquedown.png').convert_alpha()
	icono_doble = pygame.image.load('iconos/icono_doble.png').convert_alpha()
	icono_inmune = pygame.image.load('iconos/icono_inmune.png').convert_alpha()
	pickups = {'freeze': icono_freeze, 'slow': icono_slow, 'fast': icono_fast, 'ataqueup': icono_ataqueup, 'ataquedown': icono_ataquedown, 'doble': icono_doble, 'inmune': icono_inmune}


	#enemigo
	enemigos = pygame.sprite.Group()

	#clock
	start_time = 0
	tiempo = 0
	enemigos_cd = 700
	enemigos_timer = pygame.USEREVENT + 2
	pygame.time.set_timer(enemigos_timer, enemigos_cd)
	pickups_timer = pygame.USEREVENT + 5
	pygame.time.set_timer(pickups_timer, 12000)

	#ataque cd
	ataque_rapido_cd = 0
	ataque_fuerte_cd = 0
	ataque_rap_surf = fuente.render(f'{int(ataque_rapido_cd)}', False, color)
	ataque_rap_rec = ataque_rap_surf.get_rect(midbottom = (410,380))
	ataque_fuerte_surf = fuente.render(f'{int(ataque_fuerte_cd)}', False, color)
	ataque_fuerte_rec = ataque_fuerte_surf.get_rect(midbottom = (410,380))

	#pickup
	pickup = None
	pickup_2 = None

	#loop principal
	while True:

		#event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #cierre de ventana
					pygame.quit()
					exit()
			if game_active: #ingame

				if event.type == pygame.USEREVENT+1: #lanzar ataque cargado
					if event.flip == 'all':
						[spells.add(Spell((event.pos[0]-30,event.pos[1]+5),ang)) for ang in (0,45,135,180,225,315)]
						ataque_fuerte_cd = 20
					else:
						spells.add(Spell((event.pos[0]-30,event.pos[1]+5),event.flip))
					if event.play == True:
						fire.play()

				if event.type == pygame.USEREVENT+3: #lanzar ataque rapido
					ataque_rapido_cd = 10
					spells.add(Spell((event.pos[0]-30,event.pos[1]+5),event.flip))
					if event.play == True:
						fire.play()

				if event.type == pygame.USEREVENT+2: #spawnear enemigo
					enemigos.add(Enemy(randint(0,1)))
					spawn.play()
					pygame.time.set_timer(enemigos_timer, enemigos_cd - score * 14 - tiempo*2)
				if event.type == pygame.USEREVENT + 5:
					pickup = choices(list(pickups), k = 1)[0]
					pickup_2 = pickup
					

			else:

				if event.type == pygame.KEYDOWN: #reiniciar partida
					if event.key == pygame.K_SPACE:
						restart.play()
						pygame.mixer.music.set_volume(0.5)
						game_active = True
						bruja.add(Bruja())
						score = 0
						score_surf = fuente.render(f'Score: {score}', False, color)
						score_rec = score_surf.get_rect(center = (400,20))
						ataque_rapido_cd = 0
						ataque_fuerte_cd = 0
						start_time = pygame.time.get_ticks()//1000
						pygame.time.set_timer(pickups_timer, 12000)
						pygame.time.set_timer(enemigos_timer, enemigos_cd)

		if game_active:	

			if score == 40 and lvl == 1: #puntuacion alcanzada
				lvl = 2
				nextlvl.play()
				enemigos.empty()
				pygame.time.set_timer(enemigos_timer, 0)

			if pygame.sprite.groupcollide(spells, enemigos, True, True): # enemigo alcanzado
				kill.play()
				score += 1
				score_surf = fuente.render(f'Score: {score}', False, color)
				score_rec = score_surf.get_rect(center = (400,20))

			if any([pygame.sprite.collide_mask(bruja.sprite, spr) for spr in enemigos.sprites()]) or tiempo >= 120: #jugador alcanzado o tiempo max
				muerte.play()
				pygame.mixer.music.set_volume(0.2)
				enemigos.empty()
				bruja.empty()
				spells.empty()
				game_active = False
				continue

			#tiempo actual
			timer_surf, timer_rect, tiempo = timer_render(start_time, fuente_time, color)
			
			#mostrar en pantalla
			screen.blit(fondo_surf,fondo_rec)
			enemigos.draw(screen)
			bruja.draw(screen)
			screen.blit(score_surf, score_rec)
			screen.blit(arbusto_fondo, fondo_rec)
			screen.blit(timer_surf, timer_rect)
			spells.draw(screen)

			#updatear clases
			spells.update()
			enemigos.update()
			bruja.update(pickup)
			pickup = None

			#cooldowns
			ataque_rapido_cd = ataque_cd(ataque_rapido_cd)
			ataque_fuerte_cd = ataque_cd(ataque_fuerte_cd)
			
			if ataque_rapido_cd !=0:
				ataque_rap_surf = fuente.render(f'{int(ataque_rapido_cd+0.9)}', False, color)
				ataque_rap_rec = ataque_rap_surf.get_rect(center = (351,368))
				screen.blit(iconcd_rap_surf, iconcd_rap_rec)
				screen.blit(ataque_rap_surf, ataque_rap_rec)

			else:
				screen.blit(icon_rap_surf, iconcd_rap_rec)

			if ataque_fuerte_cd !=0:
				ataque_fuerte_surf = fuente.render(f'{int(ataque_fuerte_cd+0.9)}', False, color)
				ataque_fuerte_rec = ataque_fuerte_surf.get_rect(center = (451,368))
				screen.blit(iconcd_fuerte_surf, iconcd_fuerte_rec)
				screen.blit(ataque_fuerte_surf, ataque_fuerte_rec)
			else:
				screen.blit(icon_fuerte_surf, iconcd_fuerte_rec)

			if tiempo != 0 and (tiempo-9) % 12 < 3:
				spell_time_surf = fuente.render(str( 3 - ((tiempo-1) % 4)), False, color)
				spell_time_rect = spell_time_surf.get_rect(center = (bruja.sprite.rect.midtop))
				screen.blit(spell_time_surf, spell_time_rect)

			if bruja.sprite.pickup_timer:
				pickup_rect = pickups[pickup_2].get_rect(center = (bruja.sprite.rect.topright))
				screen.blit(pickups[pickup_2], pickup_rect)
			
		else: #pantalla de muerte
			#surfaces y rects
			if tiempo >= 120:
				perdiste_surf = fuente.render('Tiempo  fuera',False, color)
			else:
				perdiste_surf = fuente.render('Has muerto',False, color)
			perdiste_rec = perdiste_surf.get_rect(center = (400,100))
			score_surf = fuente.render(f'Score: {score}', False, color)
			score_rec = score_surf.get_rect(center = (400,300))
			timer_rect = timer_surf.get_rect(center = (400,330))

			#mostrar en pantalla
			screen.blit(fondo_muerto_surf, fondo_rec)
			screen.blit(perdiste_surf, perdiste_rec)
			screen.blit(muerte_surf, muerte_rec)
			screen.blit(score_surf,score_rec)
			screen.blit(timer_surf, timer_rect)


		#display y fps	
		pygame.display.update()
		fps.tick(60)


main()