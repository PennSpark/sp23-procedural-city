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
        board.choice(next_block[1][2], next_block[1][1], next_block[1][0])
    
    board.print_board()

if __name__ == '__main__':
  print(test_is_tiled())
  print(test_num_possible_tiles())
  # TODO: something funky is happening here
  print(test_2x2_board())
