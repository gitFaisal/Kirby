from turtle import Turtle, Screen, delay, listen, onkey
from shapes import initialize_shapes
from objects import Kirby, Enemy

def setup_screen():
  window = Screen()
  window.bgcolor("green")
  window.title("Kirby's showdown!")

def setup_border():
  border = Turtle() 
  border.speed(0)
  border.color("red")
  border.penup()
  border.setposition(-300, -300)
  border.pendown()
  
  for i in range(0, 4):
    border.forward(600) 
    border.left(90) 
  
  border.hideturtle() 

def register_action_keys(kirby):
  listen()
  onkey(kirby.move_left, 'Left')
  onkey(kirby.move_right, 'Right')
  onkey(kirby.attack, 'space')
  onkey(kirby.jump, 'Up')

def initialize_game_setup():
  setup_screen()
  setup_border()
  delay(0)
  initialize_shapes()

