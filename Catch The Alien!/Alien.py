import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Catch the Aliens!!"

message = ""

#creating characters! yay

bob = Actor("alien")
bob.pos = (182,374)

def draw():
    global message
    screen.clear()
    screen.fill(color = "blue")
    bob.draw()
    screen.draw.text(message,fontsize = 40,center = (250,100))

def placeBob():
    bob.x = random.randint(50,450)
    bob.y = random.randint(50,450)

def on_mouse_down(pos):
    global message
    if bob.collidepoint(pos):
        placeBob()
        message = "you hit bob!"
    else:
        message = "you missed bob! "
        
placeBob()
pgzrun.go()