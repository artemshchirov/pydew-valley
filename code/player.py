import os
import pygame
from settings import *
from support import *



class Player(pygame.sprite.Sprite):
  def __init__(self, pos, group):
    super().__init__(group)
    
    self.import_assets()
    self.status = 'down'
    self.frame_index = 0    
    
    # general setup
    self.image = self.animations[self.status][self.frame_index]
    self.rect = self.image.get_rect(center = pos)
    
    # movement attributes
    self.direction = pygame.math.Vector2(0,0)
    self.pos = pygame.math.Vector2(self.rect.center)
    self.speed = 200
  
  
  def import_assets(self):
    self.animations = {
      'up': [], 'down': [], 'left': [], 'right':[],
      'up_idle': [], 'down_idle': [], 'left_idle': [],'right_idle': [], 
      'up_hoe':[], 'down_hoe': [],  'left_hoe': [], 'right_hoe': [],
      'up_axe':[], 'down_axe': [],  'left_axe': [], 'right_axe': [],
      'up_water':[], 'down_water': [],  'left_water': [], 'right_water': [],
    }
    
    for animation in self.animations.keys():
      absolute_path = os.path.dirname(__file__)
      relative_path = '../graphics/character/' + animation
      full_path = os.path.join(absolute_path, relative_path)
      
      self.animations[animation] = import_folder(full_path)
  
  
  def animate(self, dt):
    self.frame_index += 4 * dt
    if self.frame_index >= len(self.animations[self.status]):
      self.frame_index = 0
  
    self.image = self.animations[self.status][int(self.frame_index)]
  
  
  def input(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
      self.direction.y = -1
      self.status = 'up'
    elif keys[pygame.K_DOWN]:
      self.direction.y = 1
      self.status = 'down'
    else:
      self.direction.y = 0
    
    if keys[pygame.K_RIGHT]:      
      self.direction.x = 1
      self.status = 'right'
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
      self.status = 'left'
    else:
      self.direction.x = 0


  def get_status(self):
    
    # idle
    if self.direction.magnitude() == 0:
      self.status = self.status.split('_')[0] + '_idle'
      

  def move(self, dt):
    
    # normalizing a vector
    if self.direction.magnitude() > 0:
      self.direction = self.direction.normalize()
    
    # horizontal movement
    self.pos.x += self.direction.x * self.speed * dt
    self.rect.centerx = round(self.pos.x)

    # vertical movement
    self.pos.y += self.direction.y * self.speed * dt
    self.rect.centery = round(self.pos.y)


  def update(self, dt):
    self.input()
    self.get_status()
    self.move(dt)
    self.animate(dt)
  