class Tile:
    keys = [0, 1, 2, 3, 4, 5]
    vals = [1, 0, 3, 2, 5, 4]
    rotated_cw = [0, 1, 4, 5, 3, 2]
    names = ["up", "down", "west", "east", "north", "south"]
    dir_map = dict(zip(keys, vals))
    index_to_name = dict(zip(keys, names))
    name_to_index = dict(zip(names, keys))

    # Define tile name, initialize empty direction sets
    def __init__(self, name, rotation, faces = ["", "", "", "", "", ""]):
        self.name = name
        self.rotation = rotation;
        self.faces = faces
        self.sets = [set() for _ in range(6)]
    
    def getTileName(self):
        return self.name
    
    # Add list of tiles to a direction set
    def get_set(self, dir):
        index = Tile.name_to_index.get(dir)
        if index == None:
            raise Exception("invalid direction")
        return self.sets[index]
            
    def add_to_set(self, dir, list):
        set = self.get_set(dir)
        set.update(list)
    
    def print_sets(self):
        print(self.name)
        for idx, set in enumerate(self.sets):
            print(f"{Tile.index_to_name[idx]}: {list(map(Tile.getTileName, list(set)))}")

    def generate_sets(tile1, tile2):
        faces_1 = tile1.faces
        faces_2 = tile2.faces
        for i in range(6):
            j = Tile.dir_map[i]
            if faces_1[i] == faces_2[j]:
                #print(f"Tile 1 ({Tile.index_to_name[i]}): {faces_1[i]}")
                #print(f"Tile 2 ({Tile.index_to_name[j]}): {faces_2[j]}")
                tile1.add_to_set(Tile.index_to_name[i], [tile2])

    def create_rotations(tile):
        out_list = [tile]
        for _ in range(2):
            last_rot = out_list[-1]

            face_sets = []
            for f in range(6):
                # TODO: make sure this goes the right direction
                face_sets.append(last_rot.sets[Tile.rotated_cw[f]])
            
            out_list.append(Tile(tile.name, (last_rot.rotation + 1) % 4, face_sets))
            
        return (out_list[0], out_list[1], out_list[2], out_list[3])
                            
            
    def remove_from_set(self, dir, item):
        set = self.get_set(dir)
        set.remove(item)
