import world
class Enemy:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.talknum = 0
		self.aggro = False

	def is_alive(self):
		return self.hp > 0
	
	def talk(self):
		print("\nNot much for words\n")


#class Guard(Enemy):
#	def __init__(self):
#		super().__init__(name='Guard', hp=10, damage=5)
#		self.aggro = True

#class TunnelDweller(Enemy):
#	def __init__(self):
#		super().__init__(name='Tunnel Dweller', hp=5, damage=3)
#
#	def talk(self):
#		self.dialog = ["\nTunnel Dweller: Who are you? Do you mean to hurt us?\n", "\nTunnel Dweller: In that case you are welcome, but disturb nothing\n"]
#		self.fightwords = ["\nTunnel Dweller: We will defend the tunnel at all costs!\n"]
#		if self.aggro != True:
#			print(self.dialog[0])
#			response = input('y/n: ')
#			if response != 'n':
#				print(self.fightwords[0])
#				self.aggro = True
#				return
#			print(self.dialog[1])
#			return

