import items, world, time, npc

class Player:
	def __init__(self):
		# Inventory
		self.inventory = [items.Laptop(),
                    	  items.Rock()
                         ]

		self.x = 1
		self.y = 2		# x, y coordinates for location
		self.hp = 30	
		self.drone = 0	# Determines if player can fly his drone
		self.money = 5

	# Checks if player is alive
	def is_alive(self):
		return self.hp > 0

	# Determines most powerful weapons available when attacking
	def most_powerful_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:
				if item.damage > max_damage:
					best_weapon = item
					max_damage = item.damage
			except AttributeError:
				pass

		if max_damage == 0:
			best_weapon = items.Fists()
		return best_weapon

	# When player attacks enemy
	def attack(self):
		best_weapon = self.most_powerful_weapon()
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		print("\nYou attack a {} with your {} for {} damage!".format(enemy.name, best_weapon, best_weapon.damage))
		enemy.hp -= best_weapon.damage
		if not enemy.is_alive():
			print("You killed a {}!".format(enemy.name))
			self.inventory.append(enemy.death())
			self.drone = enemy.death_init()
		else:
			print("{} has {} HP left.".format(enemy.name, enemy.hp))
			self.hp -= enemy.damage
			print("{} hit you for {} damage! ({} HP left)".format(enemy.name, enemy.damage, self.hp))

	# The drone launching sequence
	def launch(self):
		print("\nYou take out the drone and prepare it for flight.")
		time.sleep(1)
		print("\nReady for takeoff:\n")
		for i in range(3, 0, -1):
			print(i)
			time.sleep(1)
		print("\nLIFTOFF...")
		time.sleep(1)
		print("\nThe drone hovers 100 meters in the air...")
		time.sleep(1)
		print("\nBefore veering violently.")
		time.sleep(1)
		print("\nIt heads right for Worq, and smashes head-on into the concrete wall. BANG!")
		time.sleep(2.5)
		print("\nThe drone falls to its doom, its batteries and propellers splintering into pieces.")
		time.sleep(2.5)
		print("\nA wisp of smoke trails after it. You hear the drone whispering: \"Thank you.\"")
		time.sleep(2)
		print("\nYou have released another soul. Your job here is done.")
		time.sleep(2)
		print("\nYou can keep playing if you want. But you've already won at life.")
		time.sleep(1)
		print("Somebody scavenges the drone parts and gives you RM100 for them.")
		time.sleep(1)
		self.money += 100
		self.inventory.remove(self.remove_drone())
		self.drone = 0

	# So that player can drink beer
	def drink(self):
		print("You drink the beer. You get tipsy. You also get +20 max HP.")
		self.hp += 20
		self.inventory.remove(self.check_beer())

	# Eat mee method
	def eat(self):
		print("You eat the mee. It's so spicy... you've never felt this way before.")
		time.sleep(2)
		print("Something's wrong...")
		time.sleep(2)
		self.hp -= 100
		
	# Prints player's inventory
	def print_inventory(self):
		print("\nInventory:")
		for item in self.inventory:
			print('* ' + str(item))
		print("Money: {}".format(self.money))

	# This is to remove the damn drone from player's inventory. A lil crude but it's what I got.
	def remove_drone(self):
		for item in self.inventory:
			if isinstance(item, items.Special):
				return item

	# Similar to remove_drone
	def check_beer(self):
		for item in self.inventory:
			if isinstance(item, items.Consumables):
				return item

	# Similar to remove_drone/beer
	def check_mee(self):
		for item in self.inventory:
			if isinstance(item, items.Poison):
				return item

	# To check if player is able to trade on that square.
	def trade(self):
		room = world.tile_at(self.x, self.y)
		room.check_if_trade(self)

	# This is the movement mechanism using x, y axis	
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)

