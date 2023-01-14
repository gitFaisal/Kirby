from utility import isCollision

def kirby_fireball(kirby):
  if kirby.fired == True:
    if kirby.attack_direction == 'Right':
      speed = 2
    else:
      speed = -2

    x_cor = kirby.fireball.xcor()
    x_cor += speed
    kirby.fireball.setx(x_cor)
  
    if x_cor > 280 or x_cor < -280: 
      kirby.reset_blast()




def kirby_jump(kirby_turtle, frame):
    if frame % 35 == 0:
      current_y = kirby_turtle.ycor()
      # Jump
      if kirby_turtle.jumping and kirby_turtle.jump_number < 2:
        kirby_turtle.sety(current_y + 10)
        kirby_turtle.jump_count += 1
  
        # Stop jumping after 10 mini jumps
        if kirby_turtle.jump_count == 10:
          kirby_turtle.reset_jump()
      # Fall
      elif kirby_turtle.falling:
        if current_y > -280:
          kirby_turtle.sety(current_y - 10)
        else:
          kirby_turtle.falling = False
          kirby_turtle.jump_number = 0


def kirby_collision(kirby, projectile):

  if isCollision(kirby, projectile):
    if kirby.immune:
      return
    else:
      kirby.immune = True
      kirby.lives[-1].hideturtle()
      kirby.lives.pop()

      # Check if player has lost (no lives left)
      if len(kirby.lives) == 0:
        print("YOU LOST TO VEGGIES AND FRUITS?!")

def reset_kirby_collision(kirby):
  '''
  Gives kirby time before getting hit again
  '''
  if kirby.immune:
    kirby.immune_time += 1

    if kirby.immune_time == 200:
      kirby.immune = False
      kirby.immune_time = 0




