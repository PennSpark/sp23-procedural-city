import heapq

from block import Block
from tile import Tile
from wfc import Board

# Block
def test_is_tiled():
  b = Block([], "hello")
  return b.is_tiled()

def test_num_possible_tiles():
  b = Block([1, 2, 4])
  return b.num_possible_tiles() == 3

# Board
def test_2x2_board():
    tile_1 = Tile("Tile1")
    tile_2 = Tile("Tile2")
    dirs = ["north", "south", "east", "west", "up", "down"]
    for dir in dirs:
        tile_1.add_to_set(dir, [tile_1, tile_2])
        tile_2.add_to_set(dir, [tile_1, tile_2])
    board = Board(2, 2, 1, set([tile_1, tile_2]))

    while len(board.block_heap) != 0:
        next_block = heapq.heappop(board.block_heap)
        board.collapse(next_block[1][2], next_block[1][1], next_block[1][0])
    
    board.print_board()

def path_straight_rotation_test():
   Path_Straight = Tile("Path_Straight", 0, ["pack_s","vert_building","ground","ground","path","path"])
   path_rots = Tile.create_rotations(Path_Straight)
   for i in range (len(path_rots)):
      for j in range(len(path_rots)):
          Tile.generate_sets(path_rots[i], path_rots[j])
   for path in path_rots:
      path.print_sets()

def path_corner_to_straight_generation_test():
   Path_Straight = Tile("Path_Straight", 0, ["pack_s","vert_building","ground","ground","path","path"])
   Path_Corner = Tile("Path_Corner", 0, ["pack_c","vert_building","path","ground","path","ground"]) 
   tiles = [Path_Straight, Path_Corner]
   for i in range (len(tiles)):
      for j in range(len(tiles)):
          Tile.generate_sets(tiles[i], tiles[j])
   for path in tiles:
      path.print_sets()

if __name__ == '__main__':
  #print(test_is_tiled())
  #print(test_num_possible_tiles())
  # TODO: something funky is happening here
  #print(test_2x2_board())
  path_corner_to_straight_generation_test()
