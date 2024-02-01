## -----------------------------------
## ------- EJERCICIO COLISION --------
## -----------------------------------

# ---- Collision Detection of Balls ----

import math

def ball_collide (ball1,ball2):
     x1, y1, radius1 = ball1
     x2, y2, radius2 = ball2

     distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return distance < (radius1 + radius2)

ball1 = (0, 0, 3)
ball2 = (5, 0, 3)

collision_result = ball_collide(ball1, ball2)
print(collision_result)

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715