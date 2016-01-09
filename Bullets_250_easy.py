class Bullets:
	def match(self, guns, bullet):
		aux = []
		for a in guns:
			aux.append(a+a)

		for a in aux:
			if bullet in a:
				return aux.index(a)

		return -1

		#if (bullet in guns):
		#	return guns.index(bullet)
		#else :
		#	return -1

test = (["| | | |","|| || |"," |||| "], "|| || |")


d = Bullets()
print( d.match(*test))

