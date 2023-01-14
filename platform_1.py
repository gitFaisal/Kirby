from utility import isCollision, get_xy_cors

PLATFORM = None
ON_PLATFORM = False

platform_ranges = {
  'middle': (-100, 100),
  'left': (-295, -95),
  'right': (95, 295)
}

platform_heights = [-10, -150]

def setPlatform(platform):
  global PLATFORM
  global ON_PLATFORM
  ON_PLATFORM = True
  [x, y] = get_xy_cors(platform)
  if x == 0 and y == -150:
    PLATFORM = 'middle'
  elif x == -195 and y == -10:
    PLATFORM = 'left'
  elif x == 195 and y == -10:
    PLATFORM = 'right'
    
def checkPlatform(kirby):
  [kirby_x,kirby_y] = get_xy_cors(kirby)

  if kirby_y in platform_heights:
    for range in platform_ranges.values():
      left_x = range[0]
      right_x = range[1]

      if left_x < kirby_x and right_x > kirby_x:
        ON_PLATFORM = True
        kirby.reset_jump()
        kirby.falling = False
        kirby.sety(kirby_y + 5)

def platform_contact(kirby_turtle, platform):
  
  kirby_y = kirby_turtle.ycor()
  platform_y = platform.ycor()
  if isCollision(kirby_turtle, platform):
    if kirby_y > platform_y:
      setPlatform(platform)
      kirby_turtle.reset_jump()
      kirby_turtle.falling = False
      kirby_turtle.sety(kirby_y + 5)  
        
def off_platform(kirby_turtle):
  global ON_PLATFORM
  current_x = kirby_turtle.xcor()
  if ON_PLATFORM:
    p_left = platform_ranges[PLATFORM][0]
    p_right = platform_ranges[PLATFORM][1]

    if current_x > p_right or current_x < p_left:
      kirby_turtle.falling = True
      ON_PLATFORM = False
      