from player import Player

class Action():
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.name = name
		self.hotkey = hotkey
		self.kwargs = kwargs

	def __str__(self):
		return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=Player.move_north, name='Move north', hotkey='n')

class MoveSouth(Action):
	def __init__(self):
		super().__init__(method=Player.move_south, name='Move south', hotkey='s')

class MoveEast(Action):
	def __init__(self):
		super().__init__(method=Player.move_east, name='Move east', hotkey='e')

class MoveWest(Action):
	def __init__(self):
		super().__init__(method=Player.move_west, name='Move west', hotkey='w')

class ViewInventory(Action):
	def __init__(self):
		super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')

class Attack(Action):
	def __init__(self, enemy):
		super().__init__(method=Player.attack, name='Attack', hotkey='a', enemy=enemy)

class Flee(Action):
	def __init__(self, tile):
		super().__init__(method=Player.flee, name='Flee', hotkey='f', tile=tile)

class Grab(Action):
	def __init__(self, tile):
		super().__init__(method=Player.grab, name='Grab', hotkey='g', tile=tile)

class Use(Action):
	def __init__(self, tile):
		super().__init__(method=Player.use, name='Use', hotkey='u', tile=tile)

class Talk(Action):
	def __init__(self, tile, enemy):
		super().__init__(method=Player.talk, name='Talk', hotkey='t', tile=tile, enemy=enemy)

class Quit(Action):
	def __init__(self):
		super().__init__(method=Player.quit, name='Quit', hotkey='q')
#dev command
class MapInfo(Action):
	def __init__(self, tile):
		super().__init__(method=Player.mapinfo, name= 'Map Info', hotkey='mi', tile=tile)
#dev command
class Teleport(Action):
	def __init__(self):
		super().__init__(method=Player.teleport, name='Teleport', hotkey='tp')
#dev command
class Invin(Action):
	def __init__(self):
		super().__init__(method=Player.invin, name='Toggle Invincibility', hotkey='nv')
#dev command
class SetHp(Action):
	def __init__(self):
		super().__init__(method=Player.sethp, name='Set HP', hotkey='hp')

#dev command
class NpcHp(Action):
	def __init__(self, tile):
		super().__init__(method=Player.npchp, name='Set NPC HP', hotkey='np', tile=tile)

#dev command
class Settings(Action):
	def __init__(self):
		super().__init__(method=Player.settings, name='Settings', hotkey='st')
