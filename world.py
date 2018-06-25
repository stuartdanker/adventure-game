# The world map and its rooms

import random, enemies, npc

# All room descriptions below
class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")

class StartTile(MapTile):
	def intro_text(self):
		return """
		-- Event Hall (AG7) --
		You are in the Event Hall (AG7) of NEXT Academy.
		You see a door leading out, facing north.
		"""

class OutsideTile(MapTile):
	def intro_text(self):
		return """
		-- Outside --
		Sunlight sears your eyes. You see a 7-11 store to the east
		and Pedas-Pedas on your west.

		This looks like a great place to launch a drone.
		"""

class TraderTile(MapTile):
	def intro_text(self):
		return """
		-- 7-11 --
		You enter 7-11. It's pretty much a convenience store.

		(NPC) The cashier stands at the counter, waiting for you to buy or sell stuff.
		"""

	# Extra code for trading
	def __init__(self, x, y):
		self.trader = npc.Trader()
		super().__init__(x, y)

	# This part gets the player's choice for trade
	def trade(self, buyer, seller):
		for i, item in enumerate(seller.inventory, 1):
			print("{}. {} - {} Ringgit".format(i, item.name, item.value))
		while True:
			user_input = input("\nChoose an item or press Q to exit: ")
			if user_input in ["Q", "q"]:
				return
			else:
				try:
					choice = int(user_input)
					to_swap = seller.inventory[choice - 1]
					self.swap(seller, buyer, to_swap)
				except ValueError:
					print("Wrong choice lah.")

	# Remove/appends items, as well as money
	def swap(self, seller, buyer, item):
		if item.value > buyer.money:
			print("You can't afford that.\n")
			return
		seller.inventory.remove(item)
		buyer.inventory.append(item)
		seller.money += item.value
		buyer.money -= item.value
		print("Transaction done.")

	# Determines who buys and who sells
	def check_if_trade(self, player):
		while True:
			print("Would you like to (B)uy, (S)ell, or (Q)uit?")
			user_input = input()
			if user_input in ["Q", "q"]:
				return
			elif user_input in ["B", "b"]:
				print("Watcha wanna buy? ")
				print("\nYou have {} Ringgit.".format(player.money))
				self.trade(buyer=player, seller=self.trader)
			elif user_input in ["S", "s"]:
				print("Watchu wanna sell? \n")
				self.trade(buyer=self.trader, seller=player)
			else:
				print("You can't do that! Cannot read instructions ah?")


class PedasTile(MapTile):
	def intro_text(self):
		return """
		-- Pedas-Pedas --
		It's Pedas-Pedas. The smell of spicy food greets you.

		(NPC) The cook waits for your order.
		"""

	# Trading code below all similar to above
	def __init__(self, x, y):
		self.trader = npc.PedasSeller()
		super().__init__(x, y)

	def trade(self, buyer, seller):
		for i, item in enumerate(seller.inventory, 1):
			print("{}. {} - {} Ringgit".format(i, item.name, item.value))
		while True:
			user_input = input("\nChoose an item or press Q to exit: ")
			if user_input in ["Q", "q"]:
				return
			else:
				try:
					choice = int(user_input)
					to_swap = seller.inventory[choice - 1]
					self.swap(seller, buyer, to_swap)
				except ValueError:
					print("Wrong choice lah.")

	def swap(self, seller, buyer, item):
		if item.value > buyer.money:
			print("You can't afford that.\n")
			return
		seller.inventory.remove(item)
		buyer.inventory.append(item)
		seller.money += item.value
		buyer.money -= item.value
		print("Transaction done.")

	def check_if_trade(self, player):
		while True:
			print("Would you like to (B)uy, (S)ell, or (Q)uit?")
			user_input = input()
			if user_input in ["Q", "q"]:
				return
			elif user_input in ["B", "b"]:
				print("\nWatcha wanna buy? ")
				print("You have {} Ringgit.".format(player.money))
				self.trade(buyer=player, seller=self.trader)
			elif user_input in ["S", "s"]:
				print("Watchu wanna sell? \n")
				self.trade(buyer=self.trader, seller=player)
			else:
				print("You can't do that! Cannot read instructions ah?")


class EnemyTile(MapTile):
	# 50% chance of getting either enemy
	def __init__(self, x, y):
		r = random.random()
		if r < 0.5:
			self.enemy = enemies.Coder()
		else:
			self.enemy = enemies.Guard()

		super().__init__(x, y)

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			-- The Streets --
			This is where the cars roam. You nearly avoid one.

			A {} wants to fight you!
			""".format(self.enemy.name)
		else:
			return """
			-- The Streets --
			This is where the cars roam. You nearly avoid one.

			The corpse of a {} lies here.
			""".format(self.enemy.name)

# The entire world in 3x3 grid
world_map = [
	[None,EnemyTile(1,0),None],
	[PedasTile(0,1),OutsideTile(1,1),TraderTile(2,1)],
	[None,StartTile(1,2),None]
]

# To determine where player is on the map
def tile_at(x, y):
	if x < 0 or y < 0:
		return None

	try:
		return world_map[y][x]
	except IndexError:
		return None