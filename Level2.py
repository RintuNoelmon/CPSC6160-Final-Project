import pygame
from Tile import Tile
from settings import tile_size,screen_width
from akio import Hero

class Level2:
	def __init__(self,level_data,surface):
		self.display_surface = surface
		self.setup_level(level_data)
		self.screen_shift = 3


	def setup_level(self,layout):
		self.Tile = pygame.sprite.Group()
		self.akio = pygame.sprite.GroupSingle()


		for row_index, row in enumerate(layout):
			for col_index, colm in enumerate(row):
				if colm == 'X':
					x = col_index * tile_size
					y = row_index * tile_size
					tile_sprite = Tile((x,y),tile_size)
					self.Tile.add(tile_sprite)

				if colm == 'P':
					x = col_index * tile_size
					y = row_index * tile_size
					player_sprite = Hero((x,y))
					self.akio.add(player_sprite)

	def scroll(self):
		player = self.akio.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		if player_x < screen_width/4 and direction_x < 0:
			self.screen_shift = 8
			player.speed = 0

		elif player_x > screen_width - (screen_width/4) and direction_x > 0:
			self.screen_shift = -8
			player.speed = 0

		else:
			self.screen_shift = 0
			player.speed = 8

	def horizontal_collision(self):
		player = self.akio.sprite
		player.rect.x += player.direction.x


		for sprite in self.Tile.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0:
					player.rect.left = sprite.rect.right

				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left


	def vertical_collision(self):
		player = self.akio.sprite
		player.get_gravity()


		for sprite in self.Tile.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0:
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True

				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False

		if player.on_ceiling and player.direction.y > 0:
			player.on_ceiling = False



	def run(self):
		self.Tile.update(self.screen_shift)
		self.Tile.draw(self.display_surface)
		self.scroll()

		self.akio.update()
		self.horizontal_collision()
		self.vertical_collision()
		self.akio.draw(self.display_surface)




