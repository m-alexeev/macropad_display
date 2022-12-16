import busio
import displayio
from adafruit_st7789 import ST7789
import board


class Display:
	cs_pin = None
	dc_pin = None
	rst_pin = None
	spi_pins = None
	spi = None
	display = None
	WIDTH = 240 
	HEIGHT = 240
	def __init__(
		self,
		cs_pin=board.D5,
		dc_pin=board.D6,
		rst_pin=board.D9,
		spi_pins=(board.SCK, board.MOSI),
		width=240,
		height=240,
	) -> None:
		self.cs_pin = cs_pin
		self.dc_pin = dc_pin
		self.rst_pin = rst_pin
		self.spi_pins = spi_pins
		self.WIDTH = width
		self.HEIGHT = height
		
		self._configure_spi()
		self._create_display()
		self._create_bitmap()

	def _configure_spi(self):
		displayio.release_displays()

		if not self.spi:
			self.spi = busio.SPI(self.spi_pins[0], self.spi_pins[1])

		while not self.spi.try_lock():
			pass

		self.spi.configure(baudrate=24000000)
		self.spi.unlock()

	def _create_display(self):
		display_bus = displayio.FourWire(
			self.spi, command=self.dc_pin, chip_select=self.cs_pin, reset=self.rst_pin
		)
		self.display = ST7789(display_bus, width=self.WIDTH, height=self.HEIGHT, rowstart=80, auto_refresh=False, rotation=180)


	def _create_bitmap(self):
		self.bitmap = displayio.Bitmap(self.display.width, self.display.height, 2)
		self.palette = displayio.Palette(2)
		self.palette[0] = 0x000000
		self.palette[1] = 0xFFFFFF

		self.tile_grid = displayio.TileGrid(bitmap=self.bitmap, pixel_shader=self.palette)

		self.group = displayio.Group()
		self.group.append(self.tile_grid)
		self.display.show(self.group)


	def create_grid(self, num_rows, num_cols):
		grid_width = self.WIDTH // num_cols
		grid_height = self.HEIGHT // num_rows
		# Draw Grid
		for x in range(0, num_cols + 1):
			_x = 0 if x == 0 else (x * grid_width) - 1
			for y in range(0, num_rows * grid_height):
				self.bitmap[_x,y] = 1		

		for y in range(0, num_rows + 1):
			_y = 0 if y == 0 else (y * grid_height) - 1
			for x in range(0, num_cols * grid_width):
				self.bitmap[x,_y] = 1

		self.display.refresh()


	def create_tile_grid(self, page_data): 
		pass

	def draw(self, page_data): 
		for a in range(3):
			for b in range(3):
				offset_x = a * 80
				offset_y = b * 80
				for x, i in enumerate(page_data):
					for y, j in enumerate(page_data[x]):
						if page_data[x][y] == '1':
							self.bitmap[y+ 5 + offset_x,x+ 5 + offset_y] = 1
		self.display.refresh()