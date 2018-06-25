from player import Player
from collections import OrderedDict
import sys, world, os, items, npc

# Main part of game
def play():
	os.system('clear')
	print("""
		The NEXT Drone Adventure

		You are Liren, the drone whisperer.
		And you've been summoned to release
		the trapped souls of drones.

		This is your adventure...""")
	player = Player()
	while True:
		room = world.tile_at(player.x, player.y)
		print(room.intro_text())
		choose_action(room, player)

def get_available_actions(room, player):
	actions = OrderedDict()
	print("[Choose an action: ]")

	# Action based options
	if player.inventory:
		action_adder(actions, "i", player.print_inventory, "Look at your inventory")
	if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
		action_adder(actions, "a", player.attack, "Attack")
	if isinstance(room, world.OutsideTile) and player.drone == 1:
		action_adder(actions, "L", player.launch, "LAUNCH DRONE")
	if isinstance(room, world.TraderTile) or isinstance(room, world.PedasTile):
		action_adder(actions, "T", player.trade, "TRADE")
	if player.check_beer():
		action_adder(actions, "d", player.drink, "Drink beer")
	if player.check_mee():
		action_adder(actions, "m", player.eat, "Eat mee goreng spicy")
	
	# Movement based options
	if world.tile_at(room.x, room.y - 1):
		action_adder(actions, "n", player.move_north, "Go north")
	if world.tile_at(room.x, room.y + 1):
		action_adder(actions, "s", player.move_south, "Go south")
	if world.tile_at(room.x + 1, room.y):
		action_adder(actions, "e", player.move_east, "Go east")
	if world.tile_at(room.x - 1, room.y):
		action_adder(actions, "w", player.move_west, "Go west")

	if player.hp <= 0:
		print("Your journey has come to an end!")
		end()

	return actions

# Adds all available actions for user to do
def action_adder(action_dict, hotkey, action, name):
	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	print("{}: {}".format(hotkey, name))

# Allows player to choose action
def choose_action(room, player):
	action = None
	while not action:
		available_actions = get_available_actions(room, player)
		action_input = input("\nAction: ")
		action = available_actions.get(action_input)
		if action:
			action()
		else:
			print("Invalid action!\n")

# Death sequence
def end():
	os.system('clear')
	print("You died! Game over.")
	input("Thanks for playing!")
	sys.exit("Exiting game.")

play()