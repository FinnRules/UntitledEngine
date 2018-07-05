import items, enemies, actions, world

class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.locked = False
		self.key = None

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, the_player):
		raise NotImplementedError()

	def adjacent_moves(self):
		moves = []
		if world.tile_exists(self.x + 1, self.y) and not world.is_locked(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y) and not world.is_locked(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		if world.tile_exists(self.x, self.y - 1) and not world.is_locked(self.x, self.y - 1):
			moves.append(actions.MoveNorth())
		if world.tile_exists(self.x, self.y + 1) and not world.is_locked(self.x, self.y + 1):
			moves.append(actions.MoveSouth())
		return moves

	def devcommands(self, the_player): #houses all dev commands and extends the moves list if the player is in dev mode
		devcommandslist = []
		devcommandslist.append(actions.Teleport())
		devcommandslist.append(actions.MapInfo(tile=self))
		devcommandslist.append(actions.Invin())
		devcommandslist.append(actions.SetHp())
		devcommandslist.append(actions.NpcHp(tile=self))
		devcommandslist.append(actions.Settings())
		return devcommandslist

	def available_actions(self, the_player):
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())
		moves.append(actions.Use(tile=self))
		moves.append(actions.Quit())
		if the_player.fsm:
			moves.extend(self.devcommands(the_player))

		return moves


class StartingRoom(MapTile):
	def intro_text(self):
		return """\nYou wake up on the floor of a lab. You do not remember who you are or how you got here. In all four directions there lie doors\n"""

	def modify_player(self, the_player):
		pass #no effect

class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)

	def add_loot(self, the_player):
		the_player.inventory.append(self.item)

	def modify_player(self, the_player):
		self.add_loot(the_player)

class GrabLootRoom(MapTile):
	def __init__(self, x, y, *args):
		self.item = []
		for arg in args:
			self.item.append(arg)
		super().__init__(x, y)


	def modify_player(self, the_player):
		pass

	def available_actions(self, the_player):
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())
		moves.append(actions.Use(tile=self))
		moves.append(actions.Quit())
		if len(self.item) != 0:
			moves.append(actions.Grab(tile=self))

		if the_player.fsm:
			moves.extend(self.devcommands(the_player))

		return moves

class MobRoom(MapTile):
	def __init__(self, x, y, enemy, *args):
		self.enemy = enemy
		self.item = []
		for arg in args:
			self.item.append(arg)
		super().__init__(x, y)

	def modify_player(self, the_player):
		if self.enemy.is_alive() and self.enemy.aggro:
			if not the_player.nv:
				the_player.hp = the_player.hp - self.enemy.damage
				print("\n{} does {} damage to you. You have {} HP remaining\n".format(self.enemy.name, self.enemy.damage, the_player.hp))
			elif the_player.nv:
				print("{} attempts to do {} damage [Prevented by Invincibility]\n".format(self.enemy.name, self.enemy.damage))

	def available_actions(self, the_player):
		if self.enemy.is_alive() and self.enemy.aggro:
			moves = []
			moves.append(actions.ViewInventory())
			moves.append(actions.Use(tile=self))
			moves.append(actions.Flee(tile=self))
			moves.append(actions.Attack(enemy=self.enemy))
			moves.append(actions.Talk(tile=self, enemy=self.enemy))
			moves.append(actions.Quit())
			if the_player.fsm:
				moves.extend(self.devcommands(the_player))

			return moves

		elif self.enemy.is_alive() and not self.enemy.aggro:
			moves = self.adjacent_moves()
			moves.append(actions.ViewInventory())
			moves.append(actions.Use(tile=self))
			moves.append(actions.Quit())
			moves.append(actions.Attack(enemy=self.enemy))
			moves.append(actions.Talk(tile=self, enemy=self.enemy))
			if the_player.fsm:
				moves.extend(self.devcommands(the_player))

			return moves
		else:
			moves = self.adjacent_moves()
			moves.append(actions.ViewInventory())
			moves.append(actions.Use(tile=self))
			moves.append(actions.Quit())
			if len(self.item) != 0:
				moves.append(actions.Grab(tile=self))

			if the_player.fsm:
				moves.extend(self.devcommands(the_player))

			return moves

class WinRoom(MapTile):
	def intro_text(self):
		return """\nYou feel the hot sun beat down on your face. Your eyes strain as its glow reaches you in what feels like a lifetime. You are free\n"""

	def modify_player(self, player):
		player.victory = True

#============================================================================================================
 
