class Block:
	def __init__(adress_send, adress_get, count, time, hash_key, prev_hash_key):
		self.adress_send = adress_send
		self.adress_get = adress_get
		self.count = count
		self.time = time
		self.hash_key = hash_key
		self.prev_hash_key = prev_hash_key

	def hash_generate(self):
		self.arr = 'abcdefghijklmnopqrstuvwxyz'
		self.arr = self.arr + self.arr.upper() + '1234567890'

		return self.arr


a = Block(0,0,0,0,0)
a.hash_generate()