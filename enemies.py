# Module for game enemies

import items
import player

class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0

	# Enemies are basically all the same, with just different HP and damage.
class Guard(Enemy):
	def __init__(self):
		self.name = "Glomac Guard"
		self.hp = 20
		self.damage = 2

	# So that player can receive the drone. Not sure how to append an object to list.
	def death(self):
		print("\n--- You get {}! ---".format(items.Drone()))
		return items.Drone()
		death_init()

	# To change player.drone to 1. Not sure how else to do it upon enemy death.
	def death_init(self):
		return 1

class Coder(Enemy):
	def __init__(self):
		self.name = "Malnourished Coder"
		self.hp = 11
		self.damage = 1

	def death(self):
		print("\n--- You get {}! ---".format(items.Drone()))
		return items.Drone()
		death_init()

	def death_init(self):
		return 1
