import turtle
from tkinter import *
import math as m

def draw():
## Übernehmen der Variablen aus dem Textfeld
  vi_ = float(vi.get())
  alpha_ = float(alpha.get())
  mauer_ = float(mauer.get())
  stosz_ = float(stosz.get())
  vx = vi_ * m.cos(m.radians(alpha_))
  vy = vi_ * m.sin(m.radians(alpha_))
  dt = 0.001 ## Zeit zwischen den berechneten Punkten
  ot = 0 ## Gesammtzeit
  x = 0 ## X-Koordinate
  y = 0 ## Y-Koordinate
  g = -9.81 ## Erdbeschleunigung
  c = 0 ## Zaehlvariable fuer while-Schleife

## Definition des turtle-canvas
  t.ht()
  t.speed(0)
## Zeichnen der Mauer
  t.width(5)
  t.pu()
  t.goto(mauer_*75, 0)
  t.pd()
  t.goto(mauer_*75, 20*75)
  t.pu()
  t.goto(0, 0)
  t.pd()
  t.width(2)

## Berechnung und zeichnen der Punkte
  while y >= 0:
    c += 1
    ot += dt
    vyn = vy + g*dt
    y += ((vy + vyn)/2)*dt
    vy = vyn
    x += (vx * dt)
    t.goto(x*75, y*75)
    if x > mauer_:
      x = mauer_
      vx = -vx * stosz_
      vy = vy * stosz_

## Aktion zum löschen aller Ein- und Ausgabefelder
def reset():
  vi.delete(0, END)
  alpha.delete(0, END)
  mauer.delete(0, END)
  stosz.delete(0, END)
  cv.delete(ALL)

## AKtion um das Fenster zu schlieszen
def quitHandler():
  root.destroy()
  root.quit()

## Definition des Fensters
root = Tk()
root.title("Wurf")
## erzeuge turtle-canvas
cv = Canvas(root, width=800, height=800)
cv.pack(side = LEFT, fill=BOTH, expand=YES)
t = turtle.RawTurtle(cv)
screen = t.getscreen()
screen.setworldcoordinates(0,0,800,800)
screen.bgcolor("white")
frame = Frame(root)
frame.pack(side = RIGHT, fill=BOTH, expand=YES)
t = turtle.RawTurtle(cv)

## Eingabefelder fuer Variablen
Label(frame, text="Abwurfgeschwindigkeit [m/s]").pack()
vi = Entry(frame)
vi.pack()

Label(frame, text="Abwurfwinkel [°]").pack()
alpha = Entry(frame)
alpha.pack()

Label(frame, text="Mauer [m]").pack()
mauer = Entry(frame)
mauer.pack()

Label(frame, text="Stoszeffizienz").pack()
stosz = Entry(frame)
stosz.pack()

## Knöpfe fuer Bedienung 
Button(frame, text = "Start", command=draw).pack(padx = 10, pady = 10)

Button(frame, text = "Reset", command=reset).pack(padx = 10, pady = 10)

Button(frame, text = "Quit", command=quitHandler).pack(padx = 10, pady =10)

root.mainloop()