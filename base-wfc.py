# Tile refers to general tile types
# Block refers to an individual block in the x by y by z board. Each block may be untiled or tiled.

class Tile:
    # Define tile name, initialize empty direction sets
    def __init__(self, name):
        self.name = name
        self.left_set = set()
        self.right_set = set()
        self.up_set = set()
        self.down_set = set()
        self.front_set = set()
        self.back_set = set()
    
    # Add list of tiles to a direction set
    def add_to_set(self, dir, list):
        match dir:
            case "left":
                self.left_set.update(list)
            case "right":
                self.right_set.update(list)
            case "up":
                self.up_set.update(list)
            case "down":
                self.down_set.update(list)
            case "front":
                self.front_set.update(list)
            case "back":
                self.back_set.update(list)
            case _:
                raise Exception("invalid direction")
            
    def remove_from_set(self, dir, item):
        match dir:
            case "left":
                self.left_set.remove(item)
            case "right":
                self.right_set.remove(item)
            case "up":
                self.up_set.remove(item)
            case "down":
                self.down_set.remove(item)
            case "front":
                self.front_set.remove(item)
            case "back":
                self.back_set.remove(item)
            case _:
                raise Exception("invalid direction")

class Block:
    def __init__(self, tile = None):
        self._tile = tile
        self._possible_tiles = set()

    # Check if block is tiled
    def is_tiled(self):
        return self._tile != None

    # Returns number of possible tiles in current block
    def num_possible_tiles(self):
        return len(self._possible_tiles)

    def get_tile(self):
        return self._tile

    def set_tile(self, tile):
        self._tile = tile

    def get_possible_tiles(self):
        return self._possible_tiles

    def set_possible_tiles(self, possible_tiles)
        self._possible_tiles = possible_tiles

def choice(block):
    if block.is_tiled():
        pass
    
    # Assume possible set of tiles for block is valid
    # Pick a tile from the set
    # For now just pick tile at index 0, TODO: add probability distribution for pick
    block.set_tile(block.get_possible_tiles[0])

    # Update neighbors' possible tiles
        # If neighbor inbounds:
            # If neighbor untiled:
                # Update neighbor's possible tile set to be the intersection of curr tile's direction set and neighbor's set



def main():
    board = [["X"] * 3] * 3
    # Coordinate for tileable block located at (x, y, z) is board[z][y][x]
    tile_1 = Tile("tile_1")
    tile_2 = Tile("tile_2")
    tile_1.add_to_set("left", ["tile_1, tile_2"])

    for row in board:
        print(*row)
    

if __name__ == "__main__":
    main()

