class create_map(object):
	#taking in height and width to create an oject with map of said h and w
	def __init__(self, height, width):
		self.map = []
		for i in range(0, height):
			#creating a row
			self.map.append([])
			for j in range(0, width):
				#seting all coloums in that row to 0 to denote free space
				self.map[i].append(0)

	def add_obstacle(self, xinital, xfinal, yinital, yfinal):
		#checking to see if x or y start and end are same
		if xintial == xfinal:
			xfinal += 1
		if yinital == yfinal:
			yfinal += 1
		
		#setting the range taken as input to 1 to denote obstacles
		for i in range(xinital, xfinal):
			for j in range(yinital, yfinal):
				self.map[i][j] = 1