import turtle as tt
from tkinter.messagebox import askyesno

import random
import mouse

y = 450
x = -500
lines= 15

playing = False
play = True

tt.setup(width=1900, height=1000)
tt.title("Turtle Racing!")
# tt.bgcolor("green")

def set_up():
    bob = tt.Turtle()
    bob.speed(0)

    bob.up()
    bob.setpos(x, y)
    bob.right(90)

    for line in range(lines):
        cur_x = bob.xcor()

        bob.up()
        bob.setpos(cur_x + 50, y)

        bob.write(line)

        for _ in range(8):
            bob.up()
            bob.forward(30)
            bob.down()
            bob.forward(45)
    bob.up()
    bob.hideturtle()
    return cur_x, line, bob


# This function is stolen from https://stackoverflow.com/questions/34823206/turtle-delete-writing-on-screen-and-rewrite
def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = tt.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser


def race(sur_x, line, bob, r):
    if r == 0:
        turtles = tt.numinput("Race", "How many turtles?", 5, minval=2, maxval=11)
        for turtle in range(int(turtles)):
            tt.Turtle()
    else:
        cleaner = tt.Turtle()
        cleaner.reset()
        cleaner.hideturtle()

    players = [p for p in tt.turtles() if p.isvisible()]
    meters = [0 for _ in players]


    for player in players:
        player.speed(5)
        player.shape("turtle")
        color = f"#{random.randint(0, 0xFFFFFF):06x}"
        player.color(color)

        player.up()
        p = players.index(player) # the current player
        player.setpos(cur_x - (line - 0.5) * 50 - 20, (y - 50*p) - 75)
        player.write(p + 1)
        player.forward(20)
        player.down()

        player.speed(10)


    bob.setpos((cur_x + (cur_x - lines*50))/2, -250)
    txt = erasableWrite(bob, "Click to start", font=("Arial", 16, "normal"), align="center")
    mouse.wait()
    txt.clear()

    while True:
        for p in players:
            step = random.randint(0, 10)
            p.forward(step)
            meters[players.index(p)] += step

            if meters[players.index(p)] >= 50 * lines: # 50 * 15 becasue I have 15 lines and they have 50px between them
                winner = players.index(p)
                return winner


r = 0 # round
cur_x, line, bob = set_up()
while play:
    winner = race(cur_x, line, bob, r) + 1
    r += 1

    play = askyesno("winner", f"The winner is turtle #{winner}\nDo you want to go again?")

tt.bye()
tt.done()
