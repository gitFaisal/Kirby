from turtle import Turtle
from utility import get_xy_cors
from shapes import *

class Kirby(Turtle):
  def __init__(self, position):
    self.fired = False
    self.fireball = False
    self.direction = 'Right'
    self.attack_direction = 'Right'
    self.lives = 3
    
    self.jumping = False
    self.jump_count = 0
    self.jump_number = 0
    self.falling = False

    self.immune = False 
    self.immune_time = 0
    self.lives = []
    
    super().__init__(shape=kirby_right)
    self.speed(0)
    self.penup()
    self.setposition(position)
   
  def move_left(self):
    self.direction = 'Left'
    self.set_image()
    current_x = self.xcor() 
    current_x -= 10 
    if current_x > -290:
      self.setx(current_x) 
  
  def move_right(self):
    self.direction = 'Right'
    self.set_image()
    current_x = self.xcor()
    current_x += 10
    if current_x < 290:
     self.setx(current_x)

  def reset_blast(self):
    self.fireball.hideturtle()
    self.fireball = False
    self.fired = False

  def attack(self):
    [x_cor, y_cor] = get_xy_cors(self)
    if self.direction == 'Right':
      x_cor += 10
      self.attack_direction = 'Right'
    else:
      x_cor -= 10
      self.attack_direction = 'Left'
    # Create the blast 
    position = (x_cor, y_cor)
    
    if self.fireball == False:
      self.fireball = Projectile(position, fireball)
      self.fired = True

  def set_image(self):
    if self.jumping or self.falling:
      if self.direction == 'Right':
        self.shape(kirby_jump_right)
      elif self.direction == 'Left':
        self.shape(kirby_jump_left)     
      
  def jump(self):
    self.jumping = True
    self.set_image()

  def reset_jump(self):
    self.jumping = False
    self.jump_count = 0
    self.falling = True

  def set_lives(self):
    x_cor = 280
    y_cor = 280

    if not self.lives:
      for i in range(3):
        heart = Heart((x_cor, y_cor))
        x_cor -= 35
        self.lives.append(heart)
    
class Enemy(Turtle):
  def __init__(self, position, right_image, left_image, direction):
    self.left_image = left_image
    self.right_image = right_image
    self.direction = direction
    self.fire_direction = 'Left'
    self.fireball = False
    self.location = 0
    
    super().__init__()
    self.speed(0)
    self.penup()
    self.shape(right_image)
    self.setposition(position)

  def move(self):
    if self.location >= 300:
      self.direction = 'Left'
    elif self.location <= -300:
      self.direction = 'Right'
    
    x_cor = self.xcor()
    
    if self.direction == 'Left':
      self.shape(self.left_image)
      self.location -= 1 
      self.setx(x_cor - .15)
    else:
      self.shape(self.right_image)
      self.location += 1 
      self.setx(x_cor + .15)

  def attack(self):
    [current_x, current_y] = get_xy_cors(self)

    if not self.fireball:
      self.fire_direction = self.direction
      position = (current_x, current_y)
      self.fireball = Projectile(position, green_fireball)
       
  def move_fireball(self):
    speed = 0.15
    if self.fire_direction == 'Left':
      speed *= -1 

    if self.fireball:
      x = self.fireball.xcor()
      self.fireball.setx(x + speed)
      self.reset_attack(x)
      
  def reset_attack(self, current_x):
    if current_x > 280 or current_x < -280:
      self.fireball.hideturtle()
      self.fireball.setx(1000)
      self.fireball = False    

class Projectile(Turtle):
  def __init__(self, position, shape):
    super().__init__(visible=False)
    self.shape(shape)
    self.penup()
    self.setposition(position)
    self.speed(0)
    self.showturtle()

class Platform(Turtle):
  def __init__(self, position):
    super().__init__(visible=False)
    self.shape('square')
    self.penup()
    self.setposition(position)
    self.speed(0)
    self.color('brown')
    self.showturtle()
    self.shapesize(.5, 10)

class Heart(Turtle):
  def __init__(self, position):
    super().__init__(visible=False)
    self.shape(heart)
    self.penup()
    self.setposition(position)
    self.speed(0)
    self.showturtle()