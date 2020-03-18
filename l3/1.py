from graph import *

eps = 1
x = 0
y = 200^2
moveTo(x, y)

while x < 400:
	moveTo(x, y)
	y = (x - 200)**2
	x = x + eps
	lineTo(x, y)

run();
