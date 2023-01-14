from turtle import register_shape

kirby_right = 'images/chef_kirby_right.gif'
kirby_left = 'images/chef_kirby_left.gif'
fireball = 'images/fireball.gif'
apple_left = 'images/apple_left.gif'
apple_right = 'images/apple_right.gif'
raddish_left = 'images/raddish_left.gif'
raddish_right = 'images/raddish_right.gif'
green_fireball = 'images/green_fireball.gif'
kirby_jump_right = 'images/kirby_jumping_right.gif'
kirby_jump_left = 'images/kirby_jumping_left.gif'
heart = 'images/heart.gif'

def initialize_shapes():
  register_shape(kirby_right)
  register_shape(kirby_left)
  register_shape(fireball)
  register_shape(apple_right)
  register_shape(apple_left)
  register_shape(raddish_right)
  register_shape(raddish_left)
  register_shape(green_fireball)
  register_shape(kirby_jump_right)
  register_shape(kirby_jump_left)
  register_shape(heart)