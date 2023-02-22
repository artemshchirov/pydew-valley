import pygame 
from settings import *

class Level:
  def __init__(self):
    # get the display surface
    self.display_surface = pygame.display.get_surface()
    
    # sprite groups
    self.all_sprites = pygame.sprite.Group()
  
  def run(self, dt):
    self.display_surface.fill('black')
    self.all_sprites.draw(self.display_surface)
    self.all_sprites.update()