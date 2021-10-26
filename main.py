from ursina import *
import Game

c = False
p = (0,0,0)

app = Ursina()

game = Game.Game(2)

camera.orthographic = True
camera.position = (0, 0, -20)
camera.origin = (0, 0)
camera.fov = 6



def update():
    global c
    global p
    camera.x += held_keys['d'] * 2 * time.dt    # move camera left
    camera.x -= held_keys['a'] * 2 * time.dt    # right
    camera.y += held_keys['w'] * 2 * time.dt    # up
    camera.y -= held_keys['s'] * 2 * time.dt    # down
    camera.z += held_keys['q'] * 4 * time.dt    # zoom in
    camera.z -= held_keys['e'] * 4 * time.dt    # zoom out

    if mouse.middle:
        if c:
            p = mouse.position
            c = True
        else:
            camera.x += (mouse.position[0] - p[0]) * .25 * camera.fov * .15
            camera.y += (mouse.position[1] - p[1]) * .25 * camera.fov * .15
    else:
        c = False

def input(key):
    if key == Keys.scroll_up:
        #camera.z += 5 * time.dt
        camera.fov -= 1
    if key == Keys.scroll_down:
        #camera.z -= 5 * time.dt
        camera.fov += 1


app.run()