class Menu: 

	grid = []
	rows = 0 
	cols = 0
	current_page = 0
	num_pages = 0
	def __init__(self, num_pages, width, height) -> None:
		self.num_pages = num_pages - 1  # 0 indexed
		self.rows = height
		self.cols = width

		# Initialize grid
		self.grid = [ ["X"] * self.cols for i in range(self.rows)]
	
	def setPage(self, page: int) -> None:
		if (page >= 0 and page <= self.num_pages): 
			self.current_page = page
		self._displayGrid()

	def _displayGrid(self):
		print('Displaying Grid:')
		#TODO: Hook up display
		for row in range(self.rows):
			for col in range(self.cols):
				print(self.grid[row][col], end=',')
			print()