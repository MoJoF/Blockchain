import random

class Block:
	def __init__(self, adress_send, adress_get, count, time, hash_key, prev_hash_key):
		self.adress_send = adress_send
		self.adress_get = adress_get
		self.count = count
		self.time = time
		self.hash_key = hash_key
		self.prev_hash_key = prev_hash_key

	def hash_generate(self):
		self.arr = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z, '
		self.arr = self.arr + '1,2,3,4,5,6,7,8,9,0'
		self.arr = self.arr.split(',')

		self.res = []

		for i in range(64):
			self.res.append(random.choice(self.arr))

		self.res = "".join(self.res).replace(" ", "")

		return self.res