class WidgetRepairs:
	def days(self, arrivals, numPerDay):
		curDay = 0
		accum = 0
		count = 0
		for a in arrivals:
			print(a, accum)
			a += accum
			accum = 0
			if a == 0:
				continue
			if a > numPerDay:
				accum = a - numPerDay
			count += 1

		if accum > 0:
			count += accum/numPerDay
			if accum%numPerDay != 0:
				count += 1

		return count


d = WidgetRepairs()

test =([10, 0, 0, 4, 20],8)

print( d.days(*test) )

