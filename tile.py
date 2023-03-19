class Tile:
    keys = [0, 1, 2, 3, 4, 5]
    vals = [1, 0, 3, 2, 5, 4]
    names = ["up", "down", "west", "east", "north", "south"]
    dir_map = dict(zip(keys, vals))
    name_map = dict(zip(keys, names))
    # Define tile name, initialize empty direction sets
    def __init__(self, name, faces = ["", "", "", "", "", ""]):
        self.name = name
        self.faces = faces
        self.west_set = set()
        self.east_set = set()
        self.north_set = set()
        self.south_set = set()
        self.up_set = set()
        self.down_set = set()
        self.sets = [self.up_set, self.down_set, self.west_set, self.east_set, self.north_set, self.south_set]
    
    def getTileName(self):
        return self.name
    
    # Add list of tiles to a direction set
    def get_set(self, dir):
        if dir == "west":
            return self.west_set
        elif dir == "east":
            return self.east_set
        elif dir == "north":
            return self.north_set
        elif dir == "south":
            return self.south_set
        elif dir == "up":
            return self.up_set
        elif dir == "down":
            return self.down_set
        else:
            raise Exception("invalid direction")
            
    def add_to_set(self, dir, list):
        if dir == "west":
            self.west_set.update(list)
        elif dir == "east":
            self.east_set.update(list)
        elif dir == "north":
            self.north_set.update(list)
        elif dir == "south":
            self.south_set.update(list)
        elif dir == "up":
            self.up_set.update(list)
        elif dir == "down":
            self.down_set.update(list)
        else:
            raise Exception("invalid direction")
    
    def print_sets(self):
        print(self.name)
        for idx, set in enumerate(self.sets):
            print(f"{Tile.name_map[idx]}: {list(map(Tile.getTileName, list(set)))}")

        
    
    def generate_sets(tile1, tile2):
        faces_1 = tile1.faces
        faces_2 = tile2.faces
        for i in range(6):
            j = Tile.dir_map[i]
            if faces_1[i] == faces_2[j]:
                print(f"Tile 1 ({Tile.name_map[i]}): {faces_1[i]}")
                print(f"Tile 2 ({Tile.name_map[j]}): {faces_2[j]}")
                tile1.add_to_set(Tile.name_map[i], [tile2])
            
    def remove_from_set(self, dir, item):
        if dir == "west":
            self.west_set.remove(item)
        elif dir == "east":
            self.east_set.remove(item)
        elif dir == "north":
            self.north_set.remove(item)
        elif dir == "south":
            self.south_set.remove(item)
        elif dir == "up":
            self.up_set.remove(item)
        elif dir == "down":
            self.down_set.remove(item)
        else:
            raise Exception("invalid direction")
            