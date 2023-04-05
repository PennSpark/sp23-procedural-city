class Tile:
    keys = [0, 1, 2, 3, 4, 5]
    vals = [1, 0, 3, 2, 5, 4]
    rotated_cw = [0, 1, 4, 5, 3, 2]
    names = ["up", "down", "west", "east", "north", "south"]
    opposite_dir = dict(zip(keys, vals))
    index_to_name = dict(zip(keys, names))
    name_to_index = dict(zip(names, keys))

    # Define tile name, initialize empty direction sets
    def __init__(self, name, rotation, faces, tags):
        self.maya_name = name
        self.name = f'{name}_{rotation}'
        self.rotation = rotation
        self.faces = faces
        self.tags = tags
        self.sets = [set() for _ in range(6)]
    
    def getTileName(self):
        return self.name
    
    def get_set(self, dir):
        """Get a tile set from direction string"""
        index = Tile.name_to_index.get(dir)
        if index == None:
            raise Exception("invalid direction")
        return self.sets[index]
    
    def add_to_set(self, dir, list):
        """Add list of tiles to a direction set"""
        set = self.get_set(dir)
        set.update(list)

    def print_sets(self):
        print(self.name)
        for idx, set in enumerate(self.sets):
            print(f"{Tile.index_to_name[idx]}: {list(map(Tile.getTileName, list(set)))}")

    # NOTE: We have to call this between all pairs AFTER generating rotations.
    def generate_sets(tile1, tile2):
        """Add all possible adjacency rules using tile2 to tile1 sets, with locked rotation"""
        faces_1 = tile1.faces
        faces_2 = tile2.tags
        for i in range(6):
            j = Tile.opposite_dir[i]
            if faces_1[i] in (faces_2[j]):
                if ((tile1.maya_name == "Building_Corner" and tile2.maya_name == "Building_Corner") or (tile1.maya_name == "Path_Corner" and tile2.maya_name == "Path_Corner") and (tile1.rotation != tile2.rotation)):
                    continue
                #print(f"Tile 1 ({Tile.name_map[i]}): {faces_1[i]}")
                #print(f"Tile 2 ({Tile.name_map[j]}): {faces_2[j]}")
                tile1.add_to_set(Tile.index_to_name[i], [tile2])

    def create_rotations(tile):
        """Generate 3 more rotations of a tile, and return a list with all 4"""
        out_list = [tile]
        for _ in range(3):
            last_rot = out_list[-1]

            faces = []
            tags = []
            for f in range(6):
                # TODO: make sure this goes the right direction
                faces.append(last_rot.faces[Tile.rotated_cw[f]])
                tags.append(last_rot.tags[Tile.rotated_cw[f]])
            
            out_list.append(Tile(tile.maya_name, (last_rot.rotation + 1) % 4, faces, tags))
            
        return out_list
                            
            
    def remove_from_set(self, dir, item):
        set = self.get_set(dir)
        set.remove(item)
