import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
	if spin_chamber()==bullet_position:
		result = "You are dead!"
	else: result = "Keep playing!"
	
	return result




print(fire_gun())