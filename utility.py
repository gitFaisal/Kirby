def isCollision(obj_one, obj_two):
  obj_two_position = get_xy_cors(obj_two)
  distance = obj_one.distance(obj_two_position)

  if distance < 20:
    return True
  else:
    return False


def enemy_collision(player, enemies):
  for enemy in enemies:
    if player.fireball and isCollision(player.fireball, enemy):
      player.reset_blast()
      enemy.hideturtle()
      enemy.sety(-1000)

def move_enemies(enemies):
  for enemy in enemies:
    enemy.move()

def get_xy_cors(turtle_obj):
  x_cor = turtle_obj.xcor()
  y_cor = turtle_obj.ycor()
  return (x_cor, y_cor)

