import pygame

class UI:
	def __init__(self,surface):

		self.display_surface = surface 

		self.health_bar = pygame.image.load('../graphics/character/idle/1.png').convert_alpha()
		self.health_bar_rect = self.health_bar.get_rect(topleft = (64,64))

		self.coin = pygame.image.load('../graphics/ui/coin.png').convert_alpha()
		self.coin_rect = self.coin.get_rect(topleft = (64,160))
		self.font = pygame.font.Font('../graphics/ui/PressStart2P-vaV7.ttf',64)

	def show_health(self,current):
		self.display_surface.blit(self.health_bar,self.health_bar_rect)
		health_amount_surf = self.font.render(f"x{int(current)}",False,'#ffffff')
		health_amount_rect = health_amount_surf.get_rect(midleft = (self.health_bar_rect.right + 16,self.health_bar_rect.centery))
		self.display_surface.blit(health_amount_surf,health_amount_rect)
	def show_coins(self,amount):
		self.display_surface.blit(self.coin,self.coin_rect)
		coin_amount_surf = self.font.render(str(amount),False,'#ffffff')
		coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 16,self.coin_rect.centery))
		self.display_surface.blit(coin_amount_surf,coin_amount_rect)