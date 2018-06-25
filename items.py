# All in-game items

class Weapon:
	def __init__(self):
		raise NotImplementedError("Do not create raw Weapon objects.")

	def __str__(self): return self.name

class Rock(Weapon):
	def __init__(self):
		self.name = "Rock"
		self.description = "A fist-sized rock, best used against heads."
		self.damage = 5
		self.value = 1

class Laptop(Weapon): 
	def __init__(self):
		self.name = "Laptop"
		self.description = "A good ol' Dell laptop. " \
							"Heavy and nice to smack people with."
		self.damage = 10
		self.value = 50

class Fists(Weapon):
	def __init__(self):
		self.name = "Fists"
		self.description = "Bare knuckles."
		self.damage = 1
		self.value = 0

# Had to create this class to easily determine if drone is in inventory (with isinstance)
class Special:
	def __str__(self):
		return self.name

class Drone(Special):
	def __init__(self):
		self.name = "The Holy Drone"
		self.description = "A drone. You can feel its spirit humming within."

	def __str__(self):
		return self.name

# Future plans, add effects for getting drunk
class Consumables:
	def __str__(self):
		return self.name

class Beer(Consumables):
	def __init__(self):
		self.name = "Carlsberg Beer"
		self.description = "A can of Carlsberg, cold and wet from condensation."
		self.value = 10

# Also had to create this class for easy searching with isinstance
class Poison:
	def __str__(self):
		return self.name

class Mee(Poison):
	def __init__(self):
		self.name = "Mee Goreng Extra Spicy"
		self.description = "It's a plate of mee goreng, and even the smell makes your eyes water."
		self.value = 1
