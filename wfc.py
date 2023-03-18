import heapq
from tile import Tile
from block import Block

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

class Board:
    def __init__(self, X, Y, Z, tiles):
        self.board = [[[Block(tiles.copy()) for i in range(X) ] for i in range(Y)] for i in range(Z)]
        self.block_heap = []
        for i in range(X): 
            for j in range(Y):
                for k in range(Z):
                    heapq.heappush(self.block_heap, (len(tiles), (i, j, k)))
        # print(self.block_heap)

    def choice(self, x, y, z):
        block = self.board[z][y][x]

        if block.is_tiled():
            pass
        
        # Assumes possible set of tiles for block is valid
        # Pick a tile from the set
        if len(block.get_possible_tiles()) == 0:
            # print(block.get_possible_tiles())
            return
        
        # For now just pick tile at index 0, TODO: add probability distribution for pick
        tile_placed = block.get_possible_tiles().pop()
        block.set_tile(tile_placed)
        print("Placed tile " + tile_placed.getTileName() + " at block " + str((x, y, z)))

        # Update neighbors' possible tiles
            # x - 1 (West)
        if self.is_block_inbounds(x - 1, y, z) and not self.board[z][y][x - 1].is_tiled():
            self.board[z][y][x - 1].set_possible_tiles((self.board[z][y][x - 1].get_possible_tiles()).intersection(block.get_tile().get_set("west")))

        # x + 1 (East)
        if self.is_block_inbounds(x + 1, y, z) and not self.board[z][y][x + 1].is_tiled():
            self.board[z][y][x + 1].set_possible_tiles((self.board[z][y][x + 1].get_possible_tiles()).intersection(block.get_tile().get_set("east")))

        # y - 1 (North)
        if self.is_block_inbounds(x, y - 1, z) and not self.board[z][y - 1][x].is_tiled():
            self.board[z][y - 1][x].set_possible_tiles((self.board[z][y - 1][x].get_possible_tiles()).intersection(block.get_tile().get_set("north")))

        # y + 1 (South)
        if self.is_block_inbounds(x, y + 1, z) and not self.board[z][y + 1][x].is_tiled():
            self.board[z][y + 1][x].set_possible_tiles((self.board[z][y + 1][x].get_possible_tiles()).intersection(block.get_tile().get_set("south")))

        # z - 1 (Down)
        if self.is_block_inbounds(x, y, z - 1) and not self.board[z - 1][y][x].is_tiled():
            self.board[z - 1][y][x].set_possible_tiles((self.board[z - 1][y][x].get_possible_tiles()).intersection(block.get_tile().get_set("down")))

        # z + 1 (Up)
        if self.is_block_inbounds(x, y, z + 1) and not self.board[z + 1][y][x].is_tiled():
            self.board[z + 1][y][x].set_possible_tiles((self.board[z + 1][y][x].get_possible_tiles()).intersection(block.get_tile().get_set("up")))

    def is_block_inbounds(self, x, y, z):
        return x < len(self.board) and y < len(self.board[0]) and z < len(self.board[0][0])
    

def main():
    # TODO: Board is a 3d array of Block objects. Block objects are initialized with tile type None and with possible tile set of all tiles
    tile_1 = Tile("tile_type_1")
    tile_2 = Tile("tile_type_2")
    tile_1.add_to_set("west", [tile_1, tile_2])
    board = Board(3, 3, 3, set([tile_1, tile_2]))

    while len(board.block_heap) != 0:
        next_block = heapq.heappop(board.block_heap)
        board.choice(next_block[1][2], next_block[1][1], next_block[1][0])

if __name__ == "__main__":
    main()

