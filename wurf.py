import turtle as t
import math as m

## Abfrage der Variablen
vi = float(input("Abwurfgeschwindigkeit [m/s] = "))
alpha = float(input("Wurfwinkel [°]= "))
mauer = float(input("Mauer [m]= "))
stosz = float(input("Stoszeffizenz = "))

## Berechnung des Geschwindigkeitsvektors
vx = vi * m.cos(m.radians(alpha))
vy = vi * m.sin(m.radians(alpha))
v = [vx, vy]
print("\n********************************\n", v, "\n********************************\n")
dt = 0.005 ## Zeit zwischen den berechneten Punkten
ot = 0 ## Gesammtzeit
x = 0 ## X-Koordinate
y = 0 ## Y-Koordinate
g = -9.81 ## Erdbeschleunigung
c = 0 ## Zaehlvariable fuer while-Schleife

## Definition des turtle-canvas
window = t.Screen()
t.ht()
## zeichen der Mauer
t.width(5)
t.pu()
t.goto(mauer*75, 0)
t.pd()
t.goto(mauer*75, 20*75)
t.pu()
t.goto(0, 0)
t.pd()
t.width(2)

##Berechnung und zeichen der Punkte
while y >= 0:
  c += 1
  ot += dt
  vyn = vy + g*dt
  y += ((vy + vyn)/2)*dt
  vy = vyn
  x += (vx * dt)
  t.goto(x*75, y*75)
  if x > mauer:
    vx = -vx * stosz
    vy = vy * stosz

## Enduebersicht ueber die Rechenschritte
print(ot)
print(c)
window.exitonclick()