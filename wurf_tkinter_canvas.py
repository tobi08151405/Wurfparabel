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
  
  ## zeichnen der Mauer
  cv.create_line(mauer_*75, 0, mauer_*75, 20*75, width=4)

## Berechnung und zeichnen der Punkte
  while y >= 0:
    c += 1
    ot += dt
    vyn = vy + g*dt
    y += ((vy + vyn)/2)*dt
    vy = vyn
    x += (vx * dt)
    cv.create_oval(x*75, cv.winfo_height() - y*75, x*75, cv.winfo_height() - y*75)
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

## Groesze des Canvas
w_ = 800
h_ = 600

root = Tk()
root.title("Wurf")
## Erzeugung des Canvas
cv = Canvas(root, width=w_, height=h_)
cv.pack(side = LEFT, fill=BOTH, expand=YES)
frame = Frame(root)
frame.pack(side = RIGHT, fill=BOTH, expand=YES)

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
