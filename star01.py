#Drawing star using python turtle and fill.

from turtle import *

color('blue', 'red')
begin_fill()
while True:
    forward(100)
    left(216)
    if abs(pos()) < 1:
        break
end_fill()
done()
