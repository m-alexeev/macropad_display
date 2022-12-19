from busio import SPI
from displayio import release_displays, FourWire
from adafruit_st7789 import ST7789
from board import D5, D6, D9, SCK, MOSI

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
		cs_pin=D5,
		dc_pin=D6,
		rst_pin=D9,
		spi_pins=(SCK, MOSI),
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

	def _configure_spi(self):
		release_displays()

		if not self.spi:
			self.spi = SPI(self.spi_pins[0], self.spi_pins[1])

		while not self.spi.try_lock():
			pass

		self.spi.configure(baudrate=24000000)
		self.spi.unlock()

	def _create_display(self):
		display_bus = FourWire(
			self.spi, command=self.dc_pin, chip_select=self.cs_pin, reset=self.rst_pin
		)
		self.display = ST7789(display_bus, width=self.WIDTH, height=self.HEIGHT, rowstart=80, rotation=180)


