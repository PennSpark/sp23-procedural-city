<<<<<<< Updated upstream
# Tile refers to general tile types
# Block refers to an individual block in the x by y by z board. Each block may be untiled or tiled.
# Coordinate for tileable block located at (x, y, z) is board[z][y][x]

# Directions
# West: -x
# East: +x
# North: -y
# South: +y
# Up: +z
# Down: -z

# Global variables for board dimensions
X, Y, Z = 3, 3, 3
=======
import heapq

class Board:
    def __init__(self, i, j, k, tiles):
        self.board = [[[""] * i ] * j ] * k
        self.block_heap = []
        for i, j, k in range(i), range(j), range(k):
            heapq.heappush(self.block_heap, ((i, j, k), tiles.size()))

>>>>>>> Stashed changes

class Tile:
    # Define tile name, initialize empty direction sets
    def __init__(self, name):
        self.name = name
        self.west_set = set()
        self.east_set = set()
        self.north_set = set()
        self.south_set = set()
        self.up_set = set()
        self.down_set = set()
<<<<<<< Updated upstream
=======
        self.front_set = set()
        self.back_set = set()

>>>>>>> Stashed changes
    
    # Add list of tiles to a direction set
    def add_to_set(self, dir, list):
        match dir:
            case "west":
                self.west_set.update(list)
            case "east":
                self.east_set.update(list)
            case "north":
                self.north_set.update(list)
            case "south":
                self.south_set.update(list)
            case "up":
                self.up_set.update(list)
            case "down":
                self.down_set.update(list)
            case _:
                raise Exception("invalid direction")
            
    def remove_from_set(self, dir, item):
        match dir:
            case "west":
                self.west_set.remove(item)
            case "east":
                self.east_set.remove(item)
            case "north":
                self.north_set.remove(item)
            case "south":
                self.south_set.remove(item)
            case "up":
                self.up_set.remove(item)
            case "down":
                self.down_set.remove(item)
            case _:
                raise Exception("invalid direction")

class Block:
    def __init__(self, tile = None):
        self._tile = tile
        # TODO: initialize this to the set of all tiles once that is implemented
        self._possible_tiles = [Tile("tile_1"), Tile("tile_2")]

<<<<<<< Updated upstream
    # Check if block is tiled
    def is_tiled(self):
        return self._tile != None
=======
def choice():

    pass
    #logic assumes this is an open tile, otherwise just pass (shouldn't have to deal with this case)
    #start with list of every tile (can be a set)
    #intersect it corresponding set of neighbors (for example, intersect with right_set of left neighbor)
    #if the remaining set is empty, then WFC again from scratch
    #otherwise, choose a random tile from the set and place it in the position
    #too tired to write this rn, we can talk about it at meeting
>>>>>>> Stashed changes

    # Returns number of possible tiles in current block
    def num_possible_tiles(self):
        return len(self._possible_tiles)

    # Getters and setters
    def get_tile(self):
        return self._tile

    def set_tile(self, tile):
        self._tile = tile

    def get_possible_tiles(self):
        return self._possible_tiles

    def set_possible_tiles(self, possible_tiles)
        self._possible_tiles = possible_tiles

def choice(x, y, z):
    block = board[z][y][x]

    if block.is_tiled():
        pass
    
    # Assumes possible set of tiles for block is valid
    # Pick a tile from the set
    # For now just pick tile at index 0, TODO: add probability distribution for pick
    block.set_tile(block.get_possible_tiles[0])

    # Update neighbors' possible tiles
        # x - 1 (West)
        if is_block_inbounds(x - 1, y, z) and not board[z][y][x - 1].is_tiled():
            board[z][y][x - 1].set_possible_tiles((board[z][y][x - 1].get_possible_tiles).intersection(block.get_tile().get_west_set()))

        # x + 1 (East)
        if is_block_inbounds(x + 1, y, z) and not board[z][y][x + 1].is_tiled():
            board[z][y][x + 1].set_possible_tiles((board[z][y][x + 1].get_possible_tiles).intersection(block.get_tile().get_east_set()))

        # y - 1 (North)
        if is_block_inbounds(x, y - 1, z) and not board[z][y - 1][x].is_tiled():
            board[z][y - 1][x].set_possible_tiles((board[z][y - 1][x].get_possible_tiles).intersection(block.get_tile().get_north_set()))

        # y + 1 (South)
        if is_block_inbounds(x, y + 1, z) and not board[z][y + 1][x].is_tiled():
            board[z][y + 1][x].set_possible_tiles((board[z][y + 1][x].get_possible_tiles).intersection(block.get_tile().get_south_set()))

        # z - 1 (Down)
        if is_block_inbounds(x, y, z - 1) and not board[z - 1][y][x].is_tiled():
            board[z - 1][y][x].set_possible_tiles((board[z - 1][y][x].get_possible_tiles).intersection(block.get_tile().get_down_set()))

        # z + 1 (Up)
        if is_block_inbounds(x, y, z + 1) and not board[z + 1][y][x].is_tiled():
            board[z + 1][y][x].set_possible_tiles((board[z + 1][y][x].get_possible_tiles).intersection(block.get_tile().get_up_set()))

def is_block_inbounds(x, y, z):
    return x < X and y < Y and z < Z

def main():
    # TODO: Board is a 3d array of Block objects. Block objects are initialized with tile type None and with possible tile set of all tiles
    board = [[Block()] * 3] * 3
    tile_1 = Tile("tile_1")
    tile_2 = Tile("tile_2")
    tile_1.add_to_set("west", ["tile_1, tile_2"])

    for row in board:
        print(*row)
    

if __name__ == "__main__":
    main()

