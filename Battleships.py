grid = []

def createGrid():
	for x in range (10):
		grid.append([])
		for y in range (10):
			grid[x].append('O')


def drawGrid():
	for y in range (10):
		row = ""
		for x in range (10):
			row = row + grid[x][y] + " "
		print row
	print " "




createGrid()
drawGrid()
grid[2][1] = 'j'
drawGrid()
