from setup import initialize_game_setup, register_action_keys
from objects import Kirby, Enemy, Platform
from utility import enemy_collision, move_enemies
from kirby_actions import kirby_fireball, kirby_jump, reset_kirby_collision, kirby_collision
from platform import *
from shapes import *

initialize_game_setup()


# Create Kirby and Enemies
position = (0, 0)
kirby = Kirby( position )
kirby.set_lives()
# Register Kirby actions
register_action_keys(kirby)



apple = Enemy((195, 23), apple_right, apple_left, 'Left')
raddish = Enemy((-120, -260), raddish_right, raddish_left, 'Right')
# Put all enemies in an array. Allowing us to loop over them
enemy_array = [apple, raddish]


# Platform
platform1 = Platform((0,-150))
platform2 = Platform((-195, -10))
platform3 = Platform((195, -10))
platform_array = [platform1, platform2, platform3]

# Used to measure time by measuring how many frames have passed
frame = 0

while True:
  frame += 1

  kirby_fireball(kirby) # Displays fireball if fired
  
  move_enemies(enemy_array) # Moves all enemies

  enemy_collision(kirby, enemy_array) # Checks for collisions 

  kirby_jump(kirby, frame)
  reset_kirby_collision(kirby)

  # Function that checks kirbys Y while falling
  # If kirby lands above a platform, he should stop
  # checkPlatform(kirby)

  # for platform in platform_array:
  #   platform_contact(kirby, platform) 
  #   off_platform(kirby) # When kirby walks off a platform he falls
  
  # Using this loop to check if any of the enemy are hitting kirby
  for enemy in enemy_array:
    kirby_collision(kirby, enemy)
    enemy.move_fireball()

    if enemy.fireball:
      kirby_collision(kirby, enemy.fireball)
    
    if frame % 1000 == 0:
      enemy.attack()
      

    
      
      
      
    
 

  

















  
  

   

