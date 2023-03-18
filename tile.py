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
    
    def getTileName(self):
        return self.name
    
    # Add list of tiles to a direction set
    def get_set(self, dir):
        match dir:
            case "west":
                return self.west_set
            case "east":
                return self.east_set
            case "north":
                return self.north_set
            case "south":
                return self.south_set
            case "up":
                return self.up_set
            case "down":
                return self.down_set
            case _:
                raise Exception("invalid direction")
            
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
            