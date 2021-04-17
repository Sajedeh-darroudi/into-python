import math
def equation2D(a, b, c):
	delta = (b**2) - (4*a*c)
	if delta > 0:
		m = math.sqrt(delta)
		x1 = (-b-m)/(2*a)
		x2 = (-b+m)/(2*a)
		print("This equation has two answers:" + str(x1) + "and" + str(x2))
	elif delta < 0:
		print("This equation has no answer!")
	else:
		x = (-b)/(2*a)
		print("This equation has one answers:" + str(x))
    
    

print(equation2D(1, 2, -3))
print(equation2D(1, 3, 3))
print(equation2D(1, -4, 4))
