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
    def __init__(self, tile):
        self.tile = tile
        self.possible_tiles = set()

    def is_tiled(self):
        return self.tile != None

    def num_possible_tiles(self):
        return len(self.possible_tiles)


def choice():
    pass
    # logic assumes this is an open tile, otherwise just pass (shouldn't have to deal with this case)
    # start with list of every tile (can be a set)
    # intersect it corresponding set of neighbors (for example, intersect with right_set of left neighbor)
    # if the remaining set is empty, then WFC again from scratch
    # otherwise, choose a random tile from the set and place it in the position
    # too tired to write this rn, we can talk about it at meeting



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

