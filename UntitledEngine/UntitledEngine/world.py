_world = {}
starting_position = (0, 0)

def tile_exists(x, y):
	return _world.get((x, y))

def load_tiles():
	with open('resources/map.txt', 'r') as f:
		rows = f.readlines()
	x_max = len(rows[0].split('\t'))
	for y in range(len(rows)):
		cols = rows[y].split('\t')
		for x in range(x_max):
			tile_name = cols[x].replace('\n', '')
			if tile_name == 'StartingRoom':
				global starting_position
				starting_position = (x, y)
			_world[(x, y)] = None if tile_name == '' else getattr(__import__("tiles"), tile_name)(x, y)


def is_locked(x, y): #function to check if a room is locked, used by available_actions (True = locked)
	if _world.get((x, y)):
		return _world.get((x, y)).locked
	else:
		return False

def unlock(x, y, state): #open or close rooms (enemies.py: x, y will be absolute coords) state can only be boolean True or False or it will throw an error
	_world.get((x, y)).locked = state #room coords start at (0, 0)
	return
