import random
import items, world

class Player():
	def __init__(self):
		self.inventory = [items.Shovel(), items.HexDriver()] #creates array to store inv with starting items
		self.hp = 50
		self.location_x, self.location_y = world.starting_position
		self.victory = False
		self.isquit = False
		#dev settings
		self.fsm = False
		self.nv = False
		self.aa = True
		self.co = False
		self.dr = False

	def is_alive(self):
		return self.hp > 0 #returns true if the player is still alive

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action.method:
			action_method(**kwargs)

	def print_inventory(self):
		print('\n')
		for item in self.inventory:
			print(item, '\n')

	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy
		print(world.tile_exists(self.location_x, self.location_y).intro_text())
		if self.co: #listing of absolute coordinates can be done in settings
			print("({}, {})\n".format(self.location_x, self.location_y))

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)

	def attack(self, enemy):
		best_weapon = None
		max_dmg = 0
		for i in self.inventory:
			if isinstance(i, items.Weapon):
				max_dmg = i.damage
				best_weapon = i

		if best_weapon != None:
			print("\nYou use {} against {}!\n".format(best_weapon.name, enemy.name))
			enemy.hp -= best_weapon.damage
			enemy.aggro = True
			if not enemy.is_alive():
				print("\nYou killed {}!\n".format(enemy.name))
				print(world.tile_exists(self.location_x, self.location_y).intro_text())
			else:
				print("\n{} HP is {}.\n".format(enemy.name, enemy.hp))
		else:
			print("\nYou are regrettably unarmed\n")

	def flee(self, tile):
		available_moves = tile.adjacent_moves()
		r = random.randint(0, len(available_moves) - 1)
		self.do_action(available_moves[r])

	def grab(self, tile):
		check_item = input('Item to grab?: ')
		if len(tile.item) != 0:
			for i in range(len(tile.item)):
				print(tile.item[i].name.lower())
				if check_item.lower() == tile.item[i].name.lower():
					self.inventory.append(tile.item[i])
					print("\nYou pick up a {}\n".format(tile.item[i].name))
					del tile.item[i]
					return

			print("\nNo item by that name to pick up\n")

	def use(self, tile):
		check_item = input('Item to use? ')

		if check_item == "fsm" or check_item == "OwO":
			if not self.fsm:
				self.fsm = True
				print("\n<Developer Mode Active>\n")
			else:
				self.fsm = False
				print("\n<Developer Mode Inactive>\n")

			return

		for i in range(len(self.inventory)):
				if check_item.lower() == self.inventory[i].name.lower():
					if isinstance(self.inventory[i], items.Health):
						self.hp = self.hp + self.inventory[i].heal
						print("\n{} used, adding {} health\n".format(self.inventory[i].name, self.inventory[i].heal))
						del self.inventory[i]
						return
					elif isinstance(self.inventory[i], items.Key):
						print(world.tile_exists(self.location_x + 1, self.location_y).key)
						print(world.is_locked(0, 0))
						if world.is_locked(self.location_x + 1, self.location_y): #checks to see if the tile exists and if it's locked
							if world.tile_exists(self.location_x + 1, self.location_y).key.lower() == self.inventory[i].name.lower(): #checks to see if key name is equal to item used
								world.unlock(self.location_x + 1, self.location_y, False) #unlocks
						if world.is_locked(self.location_x - 1, self.location_y):
							if world.tile_exists(self.location_x - 1, self.location_y).key.lower() == self.inventory[i].name.lower():
								world.unlock(self.locaiton_x - 1, self.location_y, False)
						if world.is_locked(self.location_x, self.location_y + 1):
							if world.tile_exists(self.location_x, self.location_y + 1).key.lower() == self.inventory[i].name.lower():
								world.unlock(self.location_x, self.location_y + 1, False)
						if world.is_locked(self.location_x, self.location_y - 1):
							if world.tile_exists(self.location_x, self.location_y - 1).key.lower() == self.inventory[i].name.lower():
								world.unlock(self.location_x, self.location_y - 1, False)

					else:
						self.inventory[i].use_item()
						return

		print("\nNo item by that name to use\n")

	def talk(self, tile, enemy):
		tile.enemy.talk()

	def quit(self):
		self.isquit = True

	def mapinfo(self, tile):
		print("=====Tile=====")
		print("\nInternal Tile Name: " + tile.__class__.__name__ + "\n")
		print("Absolute Coords: (" + str(self.location_x) + ", " + str(self.location_y) + ")\n")
		print("Locked: {}\n".format(tile.locked))

		if hasattr(tile, 'item'): #checks for items in tile
			for i in range(len(tile.item)):
				print("=====Items=====\n")
				print("Internal Item Name: " + tile.item[i].__class__.__name__ + "\n")
				print("Description:")
				print(tile.item[i])
				print()

		if hasattr(tile, 'enemy'): #checks for enemies in tile
			print("=====Enemy=====\n")
			print("\nInternal Enemy Name: " + tile.enemy.__class__.__name__ + "\n")
			print("Ingame Name: " + tile.enemy.name + "\n")
			print("Stats:")
			print("Dmg: {}\nHP: {}\nAggro: {}\n".format(tile.enemy.damage, tile.enemy.hp, tile.enemy.aggro))

	def teleport(self):
		print("Teleport to (absolute coords):")
		movetox = int(input('x: '))
		movetoy = int(input('y: '))
		if world.tile_exists(movetox, movetoy):
			self.move(dx=(movetox - self.location_x), dy=(movetoy - self.location_y))
			self.mapinfo(world.tile_exists(movetox, movetoy))
		else:
			print("\ntp: Tile does not exist\n")

	def invin(self):
		if not self.nv:
			self.nv = True
			print("\nInvincibility ON\n")
		else:
			self.nv = False
			print("\nInvincibility OFF\n")

	def sethp(self):
		print("\nCurrent HP: {}\n".format(self.hp))
		self.hp = int(input('HP = '))
		print()

	def npchp(self, tile):
		if hasattr(tile, 'enemy'):
			temphp = tile.enemy.hp
			tile.enemy.hp = int(input('NPC HP = '))
			print("\n{}'s HP set to {} via [NPC HP] (Previous HP: {})\n".format(tile.enemy.name, tile.enemy.hp, temphp))
		else:
			print('\n{} has no NPC\n'.format(tile.__class__.__name__))

	def settings(self): #small in-game settings menu because I hate seeing the aa menu and other stuff
		self.options = ["aa: Toggle Available Actions List", "dr: Toggle Directional Actions Only List", "co: Show Coordinates On Tile Move"]

		for i in range(len(self.options)):
			print()
			print(self.options[i])
		print()

		setting_select = input('Setting: ')

		if setting_select == "aa":
			if self.aa:
				self.aa = False
				self.dr = False
				print("\naa Updated: No Available Actions List Shown\n")

			elif not self.aa:
				self.aa = True
				self.dr = False
				print("\naa Updated: Available Actions List Shown (default)\n")

		elif setting_select == "co":
			if not self.co:
				self.co = True
				print("\nco Updated: Coordinates Shown on Tile Move\n")

			elif self.co:
				self.co = False
				print("\nco Updated: No Coordinates Shown on Tile Move (default)\n")

		elif setting_select == "dr":
			if not self.dr:
				self.aa = False
				self.dr = True
				print("\ndr Updated: Showing Only Directional Actions\n")

			elif self.dr:
				self.dr = False
				self.aa = True
				print("\ndr Updated: Available Actions List Shown (default)\n")
