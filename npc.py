# NPC module for traders

import items

class NonPlayableCharacter():
	def __init__(self):
		raise NotImplementedError("Don't create raw NPC objects.")

	def __str__(self):
		return self.name

class Trader(NonPlayableCharacter):
	def __init__(self):
		self.name = "7-11 Cashier"
		self.money = 100
		self.inventory = [items.Beer(),
						items.Beer()]
						
# Yeah naming convention sucks, will address later
class PedasSeller(NonPlayableCharacter):
	def __init__(self):
		self.name = "Pedas-Pedas Cook"
		self.money = 100
		self.inventory = [items.Mee()]