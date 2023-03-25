import heapq
from tile import Tile
from block import Block
import random
#import maya.cmds as cmds

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
        self.board = [[[Block(tiles.copy(), (x,y,z)) for x in range(X) ] for y in range(Y)] for z in range(Z)]
        self.block_heap = []
        self.render_stack = []
        for i in range(Z): 
            for j in range(Y):
                for k in range(X):
                    heapq.heappush(self.block_heap, (len(tiles), (i, j, k)))
        # print(self.block_heap)
    
    def print_board(self):
        for slice in self.board:
            for row in slice:
                tile_row = map(Block.get_tile,row)
                name_row = map(Tile.getTileName, tile_row)
                print(*name_row)
    
    def print_board_possibility(self):
        for slice in self.board:
            for row in slice:
                poss_row = map(Block.get_possible_tiles,row)
                count_row = map(len, poss_row)
                print(*count_row)

    def print_board_coord(self):
        for slice in self.board:
            for row in slice:
                coord_row = map(Block.get_coord,row)
                print(*coord_row)


    def push_tile(self, tile, x, y, z):
        self.render_stack.append((tile, x, y, z))

    def place_tile(self, tile, x, y, z):
        pass
        #cmds.duplicate(f"{tile.name}", n=f"{tile.name}_{x}{y}{z}")
        #cmds.select(f"{tile.name}_{x}{y}{z}")
        #cmds.move(x+1, y+1, z+1)
        #cmds.select("Tile1")
    
    def render_tiles(self):
        while self.render_stack:
            obj = self.render_stack.pop()
            self.place_tile(obj[0], obj[1], obj[2], obj[3])

    def is_block_inbounds(self, x, y, z):
        return x < len(self.board[0][0]) and y < len(self.board[0]) and z < len(self.board) and x > -1 and y > -1 and z > -1

    def choice(self, x, y, z):
        #print("{}, {}, {}".format(x, y, z))
        block = self.board[z][y][x]

        if block.is_tiled():
            pass
        
        # Assumes possible set of tiles for block is valid
        # Pick a tile from the set
        print(list(map(Tile.getTileName, block.get_possible_tiles())))
        if len(block.get_possible_tiles()) == 0:
            return 1
        
        # For now just pick tile at index 0, TODO: add probability distribution for pick
        tile_placed = random.choice(list(block.get_possible_tiles()))
        block.set_tile(tile_placed)
        self.push_tile(tile_placed, x, y, z)
        print("Placed tile " + tile_placed.getTileName() + " at block " + str((x, y, z)))

        # Update neighbors' possible tiles
            # x - 1 (West)
        if self.is_block_inbounds(x - 1, y, z) and not self.board[z][y][x - 1].is_tiled():
            self.board[z][y][x - 1].set_possible_tiles((self.board[z][y][x - 1].get_possible_tiles()).intersection(block.get_tile().get_set("west")))

        # x + 1 (East)
        if self.is_block_inbounds(x + 1, y, z) and not self.board[z][y][x + 1].is_tiled():
            self.board[z][y][x + 1].set_possible_tiles((self.board[z][y][x + 1].get_possible_tiles()).intersection(block.get_tile().get_set("east")))

        # y - 1 (Up)
        if self.is_block_inbounds(x, y - 1, z) and not self.board[z][y - 1][x].is_tiled():
            self.board[z][y - 1][x].set_possible_tiles((self.board[z][y - 1][x].get_possible_tiles()).intersection(block.get_tile().get_set("down")))

        # y + 1 (Down)
        if self.is_block_inbounds(x, y + 1, z) and not self.board[z][y + 1][x].is_tiled():
            print("south")
            print(self.board[z][y+1][x].get_coord())
            self.board[z][y + 1][x].set_possible_tiles((self.board[z][y + 1][x].get_possible_tiles()).intersection(block.get_tile().get_set("up")))

        # z - 1 (South)
        if self.is_block_inbounds(x, y, z - 1) and not self.board[z - 1][y][x].is_tiled():
            self.board[z+1][y][x].set_possible_tiles((self.board[z - 1][y][x].get_possible_tiles()).intersection(block.get_tile().get_set("south")))

        # z + 1 (North)
        if self.is_block_inbounds(x, y, z + 1) and not self.board[z + 1][y][x].is_tiled():
            self.board[z + 1][y][x].set_possible_tiles((self.board[z + 1][y][x].get_possible_tiles()).intersection(block.get_tile().get_set("north")))
        
        return 0
    

def main():
    # TODO: Board is a 3d array of Block objects. Block objects are initialized with tile type None and with possible tile set of all tiles
    tile_1 = Tile("Tile1", ['Circle','Circle','Circle','Circle','Circle','Circle'])
    tile_2 = Tile("Tile2", ['Square','Square','Square','Square','Square','Square'])
    tile_3 = Tile("Tile3", ['Octogon','Octogon','Octogon','Octogon','Octogon','Octogon'])
    tile_4 = Tile("Tile4", ['Circle','Octogon','Circle','Octogon','Square','Square'])
    tile_5 = Tile("Tile5", ['Octogon','Square','Circle','Square','Octogon','Circle'])
    tile_6 = Tile("Tile6", ['Octogon','Square','Octogon','Circle','Octogon','Circle'])
    tile_7 = Tile("Tile7", ['Circle','Octogon','Octogon','Circle','Square','Circle'])
    tile_8 = Tile("Tile8", ['Square','Octogon','Circle','Octogon','Octogon','Circle'])
    tile_9 = Tile("Tile9", ['Square','Circle','Square','Square','Circle','Octogon'])
    tile_10 = Tile("Tile10", ['Circle','Circle','Square','Square','Circle','Square'])
    tiles = [tile_1, tile_2, tile_3, tile_4, tile_5, tile_6, tile_7, tile_8, tile_9, tile_10]
    for i in range (10):
        for j in range(10):
            Tile.generate_sets(tiles[i], tiles[j])
    #for tile in tiles:
    #    tile.print_sets()
    board = Board(3, 1, 3, set(tiles))

    while len(board.block_heap) != 0:
        next_block = heapq.heappop(board.block_heap)
        if board.choice(next_block[1][2], next_block[1][1], next_block[1][0]):
            board = Board(3, 1, 3, set(tiles))
    
    board.print_board()
    board.render_tiles()
    
    print(list(map(Tile.getTileName, tile_5.get_set("up"))))
    print(list(map(Tile.getTileName, tile_9.get_set("down"))))

if __name__ == "__main__":
    main()

