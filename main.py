from Block import Block

class Profile:
	

	def adress_generate(self):
		self.arr = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z, '
		self.arr = self.arr + self.arr.upper() + '1,2,3,4,5,6,7,8,9,0'
		self.arr = self.arr.split(',')

		self.res = []

		for i in range(34):
			self.res.append(random.choice(self.arr))

		self.res = "".join(self.res).replace(" ", "")

		return self.res



a = Block(0,0,0,0,0,0)
print(a.hash_generate())