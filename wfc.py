from tile import Tile
from block import Block
import heapq
import random
#import maya.cmds as cmds

# Tile refers to general tile types
# Block refers to an individual block in the x by y by z board. Each block may be untiled or tiled.
# Coordinate for tileable block located at (x, y, z) is board[z][y][x]

# Directions
# West: -x
# East: +x
# North: -z
# South: +z
# Up: +y
# Down: -y

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
                tile_row = map(Block.get_tile, row)
                name_row = map(Tile.getTileName, tile_row)
                print(*name_row)
    
    def print_board_possibility(self):
        for slice in self.board:
            for row in slice:
                poss_row = map(Block.get_possible_tiles, row)
                count_row = map(len, poss_row)
                print(*count_row)

    def print_board_coord(self):
        for slice in self.board:
            for row in slice:
                coord_row = map(Block.get_coord, row)
                print(*coord_row)


    def push_tile(self, tile, x, y, z):
        self.render_stack.append((tile, x, y, z))

    def place_tile(self, tile, x, y, z):
        if tile.maya_name == 'Empty' or tile.maya_name == 'Path_Branch_Air' or tile.maya_name == 'Path_Corner_Air' or tile.maya_name == 'Path_Straight_Air': return
        pass
        #cmds.duplicate(f"{tile.maya_name}", n=f"{tile.maya_name}_{x}{y}{z}_{tile.rotation}")
        #cmds.select(f"{tile.maya_name}_{x}{y}{z}_{tile.rotation}")
        #cmds.rotate(0, tile.rotation*90, 0)
        #cmds.move(x+1, y+1, z+1)
    
    def render_tiles(self):
        while self.render_stack:
            obj = self.render_stack.pop()
            self.place_tile(obj[0], obj[1], obj[2], obj[3])

    def is_block_inbounds(self, x, y, z):
        return x < len(self.board[0][0]) and y < len(self.board[0]) and z < len(self.board) and x > -1 and y > -1 and z > -1

    direction_offsets = [
        ("west", (-1, 0, 0)),
        ("east", (1, 0, 0)),
        ("north", (0, 0, -1)),
        ("south", (0, 0, 1)),
        ("down", (0, -1, 0)),
        ("up", (0, 1, 0)),
    ]

    def collapse(self, x, y, z, seed):
        #print("{}, {}, {}".format(x, y, z))
        block = self.board[z][y][x]

        if block.is_tiled():
            pass
        
        # Assumes possible set of tiles for block is valid
        # Pick a tile from the set
        #print(list(map(Tile.getTileName, block.get_possible_tiles())))
        if len(block.get_possible_tiles()) == 0:
            return 1
        
        # For now just pick tile at index 0, TODO: add probability distribution for pick
        tile_placed = random.choice(list(block.get_possible_tiles()))
        if (seed):
            tile_placed = seed
            #print(tile_placed.getTileName())
        block.set_tile(tile_placed)
        self.push_tile(tile_placed, x, y, z)
        print("Placed tile " + tile_placed.getTileName() + " at block " + str((x, y, z)))

        # Update neighbors' possible tiles
        for dir, (dx, dy, dz) in Board.direction_offsets:
            # bounds check
            if not self.is_block_inbounds(x + dx, y + dy, z + dz): continue
            neighbor = self.board[z + dz][y + dy][x + dx]
            # we dont care if neighbor already locked in
            if neighbor.is_tiled(): continue
            neighbor.set_possible_tiles((neighbor.get_possible_tiles()).intersection(block.get_tile().get_set(dir)))
        
        return 0
    

def main():
    # TODO: Board is a 3d array of Block objects. Block objects are initialized with tile type None and with possible tile set of all tiles
    # Tile(name, [up, down, west, east, north, south])

    # tiles on https://docs.google.com/spreadsheets/d/126zAezKKaoGMzls38S5Fy72Ctz77F2zn7gWG4wSsJe0/edit?usp=sharing
    Building_Any = Tile("Building_Any", 0, ["vert_building","vert_building","interior","interior","interior","interior"])
    Building_Wall = Tile("Building_Wall", 0, ["vert_building","vert_building","wall","wall","interior","air"])
    Building_TopFloor = Tile("Building_TopFloor", 0, ["top_air","vert_building","top","top","top","top"])
    Building_Corner = Tile("Building_Corner", 0, ["vert_building","vert_building","wall","air","wall","air"])
    Building_Door = Tile("Building_Door", 0, ["vert_building","vert_building","interior","interior","interior","pack"])
    Path_Straight = Tile("Path_Straight", 0, ["pack_s","vert_building","ground","ground","path","path"])
    Path_Straight_Air = Tile("Path_Straight_Air", 0, ["air","pack_s","air","air","pack","pack"])
    Path_Corner = Tile("Path_Corner", 0, ["pack_c","vert_building","path","ground","ground","path"])   
    Path_Corner_Air = Tile("Path_Corner_Air", 0, ["air","pack_c","pack","air","air","pack"])
    Path_Branch = Tile("Path_Branch", 0, ["pack_b","vert_building","path","path","ground","path"])
    Path_Branch_Air = Tile("Path_Branch_Air", 0, ["air","pack_b","pack","pack","air","pack"])
    Stairs = Tile("Stairs", 0, ["stack","vert_building","air","air","path","pack"])
    Stair_Hack = Tile("Stair_Hack", 0, ["stack","vert_building","air","air","pack","air"])
    Ground = Tile("Ground", 0, ["vert_building","vert_building","ground","ground","ground","ground"])
    Empty = Tile("Empty", 0, ["air","air","air","air","air","air"])         

    # tiles = [tile_1, tile_2, tile_3, tile_4, tile_5, tile_6, tile_7, tile_8, tile_9, tile_10]
    tiles_norot = [Ground, Building_Any, Building_Wall, Building_TopFloor, Building_Corner, Building_Door, Path_Straight, Path_Straight_Air, Path_Corner, Path_Corner_Air, Path_Branch, Path_Branch_Air, Stairs, Stair_Hack, Empty]
    tiles = []
    rotmap = {}
    for tile in tiles_norot:
        rot = Tile.create_rotations(tile)
        tiles.extend(rot)
        rotmap[tile.maya_name] = rot
    #print(list(map(Tile.getTileName, tiles)))
    for i in range (len(tiles)):
        for j in range(len(tiles)):
            Tile.generate_sets(tiles[i], tiles[j])

    for tile in tiles:
        if tile.maya_name == 'Ground':
            upset = []
            upset.extend(rotmap['Ground'])
            upset.extend(rotmap['Building_Any'])
            upset.extend(rotmap['Building_Wall'])
            upset.extend(rotmap['Building_Corner'])
            upset.extend(rotmap['Building_Door'])
            upset.extend(rotmap["Path_Corner"])
            upset.extend(rotmap["Path_Straight"])
            upset.extend(rotmap["Path_Branch"])
            upset.extend(rotmap["Stairs"])
            upset.extend(rotmap["Empty"])
            tile.add_to_set("up", upset)
            tile.add_to_set("down", rotmap['Ground'])
        elif tile.maya_name == 'Stairs':
            rotation = tile.rotation
            tile.add_to_set("down", rotmap['Ground'])
            tile.add_to_set("up", [rotmap['Stair_Hack'][rotation]])
        elif tile.maya_name == 'Stair_Hack':
            rotation = tile.rotation
            tile.add_to_set("down", [rotmap['Stairs'][rotation]])
            tile.add_to_set("up", rotmap['Empty'])
        elif tile.maya_name == 'Path_Straight':
            rotation = tile.rotation
            tile.add_to_set("down", rotmap['Ground'])
            tile.add_to_set("up", [rotmap['Path_Straight_Air'][rotation]])
        elif tile.maya_name == 'Path_Straight_Air':
            rotation = tile.rotation
            tile.add_to_set("down", [rotmap['Path_Straight'][rotation]])
            tile.add_to_set("up", rotmap['Empty'])
        elif tile.maya_name == 'Path_Corner':
            rotation = tile.rotation
            tile.add_to_set("down", rotmap['Ground'])
            tile.add_to_set("up", [rotmap['Path_Corner_Air'][rotation]])
        elif tile.maya_name == 'Path_Corner_Air':
            rotation = tile.rotation
            tile.add_to_set("down", [rotmap['Path_Corner'][rotation]])
            tile.add_to_set("up", rotmap['Empty'])
        elif tile.maya_name == 'Path_Branch':
            rotation = tile.rotation
            tile.add_to_set("down", rotmap['Ground'])
            tile.add_to_set("up", [rotmap['Path_Branch_Air'][rotation]])
        elif tile.maya_name == 'Path_Branch_Air':
            rotation = tile.rotation
            tile.add_to_set("down", [rotmap['Path_Branch'][rotation]])
            tile.add_to_set("up", rotmap['Empty'])
        elif tile.maya_name == 'Building_Any':
            downset = []
            downset.extend(rotmap['Ground'])
            downset.extend(rotmap['Building_Any'])
            upset = []
            upset.extend(rotmap['Building_TopFloor'])
            upset.extend(rotmap['Building_Any'])
            #upset.extend(rotmap['Building_Corner'))
            #upset.extend(rotmap['Building_Wall'))
            tile.add_to_set("down", downset)
            tile.add_to_set("up", upset)
        elif tile.maya_name == 'Building_Wall':
            rotation = tile.rotation
            downset = []
            downset.extend(rotmap['Ground'])
            downset.append(rotmap['Building_Wall'][rotation])
            upset = []
            upset.append(rotmap['Building_Wall'][rotation])
            upset.extend(rotmap['Building_TopFloor'])
            tile.add_to_set("down", downset)
            tile.add_to_set("up", upset)
        elif tile.maya_name == 'Building_Door':
            rotation = tile.rotation
            downset = []
            downset.extend(rotmap['Ground'])
            upset = []
            upset.append(rotmap['Building_Wall'][rotation])
            upset.extend(rotmap['Building_TopFloor'])
            tile.add_to_set("down", downset)
            tile.add_to_set("up", upset)
        elif tile.maya_name == 'Building_Corner':
            rotation = tile.rotation
            downset = []
            downset.extend(rotmap['Ground'])
            downset.append(rotmap['Building_Corner'][rotation])
            upset = []
            upset.append(rotmap['Building_Corner'][rotation])
            upset.extend(rotmap['Building_TopFloor'])
            tile.add_to_set("down", downset)
            tile.add_to_set("up", upset)
        elif tile.maya_name == 'Building_TopFloor':
            rotation = tile.rotation
            downset = []
            downset.extend(rotmap['Building_Wall'])
            downset.extend(rotmap['Building_Corner'])
            downset.extend(rotmap['Building_Any'])
            upset = []
            upset.extend(rotmap['Empty'])
            tile.add_to_set("down", downset)
            tile.add_to_set("up", upset)
        elif tile.maya_name == 'Empty':
            rotation = tile.rotation
            downset = []
            downset.extend(rotmap['Ground'])
            downset.extend(rotmap['Building_TopFloor'])
            downset.extend(rotmap['Path_Straight_Air'])
            downset.extend(rotmap['Path_Corner_Air'])
            downset.extend(rotmap['Path_Branch_Air'])
            downset.extend(rotmap['Stair_Hack'])
            upset = []
            upset.extend(rotmap['Empty'])
            tile.add_to_set("down", downset)
            tile.add_to_set("up", upset)
        

    #for tile in tiles:
    #    tile.print_sets()
    
    board = Board(11, 4, 11, set(tiles))
    seed_block = heapq.heappop(board.block_heap)
    board.collapse(seed_block[1][2], seed_block[1][1], seed_block[1][0], Ground)
    while len(board.block_heap) != 0:
        next_block = heapq.heappop(board.block_heap)
        if board.collapse(next_block[1][2], next_block[1][1], next_block[1][0], None):
            board = Board(11, 4, 11, set(tiles))
            seed_block = heapq.heappop(board.block_heap)
            board.collapse(seed_block[1][2], seed_block[1][1], seed_block[1][0], Ground)
            print("New Generation\n")
    
    board.print_board()
    board.render_tiles()
    

if __name__ == "__main__":
    main()
