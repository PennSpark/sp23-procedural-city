class Block:
    def __init__(self, possible_tiles, coord, tile = None):
        self._coord = coord
        self._tile = tile
        # TODO: initialize this to the set of all tiles once that is implemented
        self._possible_tiles = possible_tiles

    # Check if block is tiled
    def is_tiled(self):
        return self._tile != None

    # Returns number of possible tiles in current block
    def num_possible_tiles(self):
        return len(self._possible_tiles)

    # Getters and setters
    def get_tile(self):
        return self._tile

    def set_tile(self, tile):
        self._tile = tile

    def get_coord(self):
        return self._coord

    def get_possible_tiles(self):
        return self._possible_tiles

    def set_possible_tiles(self, possible_tiles):
        # TODO: recursion here!! otherwise possible tiles will not be valid
        self._possible_tiles = possible_tiles
