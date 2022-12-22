from displayio import TileGrid, Bitmap, Palette, Group
from display import Display
from adafruit_imageload import load
import gc

class Graphics:
    last_index = 0
    def __init__(
        self,
        display: Display,
        pad_size: tuple[int, int],
        sprite_sheet: str,
        tile_width,
        tile_height,
    ) -> None:
        self.display = display
        self.rows = pad_size[1]
        self.cols = pad_size[0]

        self._initialize_sprites(sprite_sheet, tile_width, tile_height)

    def _initialize_sprites(self, sprite_sheet, tile_width, tile_height):

        self.sprite_sheet, palette = load(
            sprite_sheet, bitmap=Bitmap, palette=Palette
        )
        gc.collect()
        self.icons = TileGrid(
            self.sprite_sheet,
            pixel_shader=palette,
            width=self.display.WIDTH,
            height=self.display.HEIGHT,
            tile_width=tile_width,
            tile_height=tile_height
        )
        self.group = Group(scale=2)
        self.group.append(self.icons)

        self.display.display.show(self.group)


    def draw_tiles(self, tiles):
        for index, icon in enumerate(tiles): 
            # Tiles use 1 based indexing
            x = index % self.cols
            y = index // self.cols
            if icon is not None: 
                self.icons[x, y] = icon
            else:
                # Set as empty tile 
                # TODO: Remove magic num
                self.icons[x, y] = 35

        # self.icons[0,0] = 6

    def _create_bitmap(self):
        self.bitmap = Bitmap(self.display.width, self.display.height, 2)
        self.palette = Palette(2)
        self.palette[0] = 0x000000
        self.palette[1] = 0xFFFFFF

        self.tile_grid = TileGrid(
            bitmap=self.bitmap, pixel_shader=self.palette
        )

        self.group = Group()
        self.group.append(self.tile_grid)
        self.display.show(self.group)

    def create_grid(self, pad_size: tuple[int, int]):
        self.grid_width = self.WIDTH // pad_size[1]
        self.grid_height = self.HEIGHT // pad_size[0]
        # Draw Grid
        for x in range(0, pad_size[0] + 1):
            _x = 0 if x == 0 else (x * self.grid_width) - 1
            for y in range(0, pad_size[1] * self.grid_height):
                self.bitmap[_x, y] = 1

        for y in range(0, pad_size[1] + 1):
            _y = 0 if y == 0 else (y * self.grid_height) - 1
            for x in range(0, pad_size[0] * self.grid_width):
                self.bitmap[x, _y] = 1

        self.display.refresh()

    def draw_manual(self, page_data):
        self._clear_screen()
        self.create_grid((3, 3))
        for row in range(len(page_data)):
            for col in range(len(page_data[0])):
                # Find size of icon
                icon_h = len(page_data[row][col])
                icon_w = len(page_data[row][col][0])

                # Offset icon to be in middle of square
                offset_y = row * self.grid_height + ((self.grid_height - icon_h) // 2)
                offset_x = col * self.grid_width + ((self.grid_width - icon_w) // 2)
                icon = page_data[row][col]

                for y in range(len(icon)):
                    for x, pixel in enumerate(icon[y]):
                        self.bitmap[x + offset_x, y + offset_y] = (
                            0 if pixel == "0" else 1
                        )
        self.display.refresh()
