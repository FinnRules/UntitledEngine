class Item():
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

	def use_item(self):
		print("\n{} doesn't seem to do anything\n".format(self.name))

class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)

	def __str__(self):
		return "{}\n====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Health(Item):
	def __init__(self, name, description, value, heal):
		self.heal = heal
		super().__init__(name, description, value)

class Key(Item):
	def __init__(self, name, description, value, unlockx, unlocky):
		self.unlockx = unlockx
		self.unlocky = unlocky
		super().__init__(name, description, value)

#Items:
class Syringe(Weapon):
	def __init__(self):
		super().__init__(name="Syringe", description="Empty, but still sharp", value=2, damage=1)

class Cash(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Cash", description="A pile of {} bills".format(str(self.amt)), value=self.amt)

class Scalpel(Weapon):
	def __init__(self):
		super().__init__(name="Scalpel", description="Small, but sharp", value=3, damage=3)

#Appears in StartingCloset
class StartingClosetPaper(Item):
	def __init__(self):
		super().__init__(name="Paper", description="A notice of some sort", value=1)

	def use_item(self):
		print("""\nRed Sector Closet Borrowing Sheet:\n3/5: Harry Allen\n3/6: Harry Allen\n3/7: Harry Allen\n3/8: Harry Allen\n3/9: Harry Al\n3/10: Harry Alfred\n<The rest of the sheet is obscurred with heavy pen scribbles>""")

#Shovel: appears in TunnelSociety
class Shovel(Weapon):
	def __init__(self):
		super().__init__(name="Shovel", description="A small metal shovel, heavily worn", value=1, damage=7)

class ComputerNote(Item):
	def __init__(self):
		super().__init__(name="Note", description="A sticky note with a few words", value=0)

	def use_item(self):
		print("\nDarrel, if you ask me again I'm gonna kill you\nbash commands:\ncat views text files\nls lists files\n")

class Diamond(Item):
	def __init__(self):
		super().__init__(name="Diamond", description="A glittering gem", value=10)

class Pickaxe(Weapon):
	def __init__(self):
		super().__init__(name="Pickaxe", description="A heavy digging tool, but still sharp", value=4, damage=5)

class HealthPack(Health):
	def __init__(self):
		super().__init__(name="First Aid Kit", description="A tool for healing", value=5, heal=10)

class HexDriver(Key):
	def __init__(self):
		super().__init__(name="Screwdriver", description="A screwdriver meant for removing hex screws", value=2, unlockx=15, unlocky=37)

	def use_item(self):
		pass

class BrassKnuckles(Weapon):
	def __init__(self):
		super().__init__(name="Brass Knuckles", description="Slip em on and start punching", value=2, damage=5)

class Carrot(Health):
	def __init__(self):
		super().__init__(name="Carrot", description="A small snack, but a sight for sore eyes underground", value=5, heal=3)

class Potato(Health):
	def __init__(self):
		super().__init__(name="Potato", description="Starchy goodness", value=6, heal=5)
