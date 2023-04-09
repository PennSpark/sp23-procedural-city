import maya.cmds as cmds

output_string = """

Building_Corner 3 5 3 5
Empty 2 4 3 5
Empty 3 3 3 5
Empty 3 2 3 5
Empty 1 1 3 5
Empty 0 0 3 5
Building_Corner 3 5 2 5
Empty 1 4 2 5
Empty 1 3 2 5
Empty 3 2 2 5
Empty 0 1 2 5
Empty 1 0 2 5
Building_Corner 3 5 1 5
Path_Straight_Air 2 4 1 5
Path_Straight_Air 0 3 1 5
Empty 0 2 1 5
Path_Corner_Air 0 1 1 5
Path_Straight_Air 3 0 1 5
Ground 2 5 0 5
Path_Straight 2 4 0 5
Path_Straight 0 3 0 5
Ground 2 2 0 5
Path_Corner 0 1 0 5
Path_Straight 3 0 0 5
Building_Corner 2 5 3 4
Empty 1 4 3 4
Empty 0 3 3 4
Empty 3 2 3 4
Empty 2 1 3 4
Empty 3 0 3 4
Building_Corner 2 5 2 4
Empty 1 4 2 4
Empty 1 3 2 4
Empty 2 2 2 4
Empty 3 1 2 4
Empty 0 0 2 4
Building_Corner 2 5 1 4
Path_Corner_Air 0 4 1 4
Path_Branch_Air 0 3 1 4
Path_Branch_Air 2 2 1 4
Path_Straight_Air 3 1 1 4
Path_Straight_Air 1 0 1 4
Ground 0 5 0 4
Path_Corner 0 4 0 4
Path_Branch 0 3 0 4
Path_Branch 2 2 0 4
Path_Straight 3 1 0 4
Path_Straight 1 0 0 4
Empty 0 5 3 3
Empty 1 4 3 3
Empty 3 3 3 3
Empty 2 2 3 3
Empty 2 1 3 3
Empty 2 0 3 3
Empty 0 5 2 3
Empty 3 4 2 3
Empty 2 3 2 3
Empty 0 2 2 3
Empty 1 1 2 3
Empty 1 0 2 3
Path_Branch_Air 2 5 1 3
Path_Branch_Air 2 4 1 3
Path_Straight_Air 3 3 1 3
Path_Branch_Air 0 2 1 3
Path_Branch_Air 2 1 1 3
Path_Straight_Air 3 0 1 3
Path_Branch 2 5 0 3
Path_Branch 2 4 0 3
Path_Straight 3 3 0 3
Path_Branch 0 2 0 3
Path_Branch 2 1 0 3
Path_Straight 3 0 0 3
Empty 0 5 3 2
Empty 2 4 3 2
Building_Corner 0 3 3 2
Building_Corner 3 2 3 2
Empty 3 1 3 2
Empty 2 0 3 2
Empty 0 5 2 2
Empty 1 4 2 2
Building_Corner 0 3 2 2
Building_Corner 3 2 2 2
Empty 3 1 2 2
Empty 2 0 2 2
Path_Branch_Air 1 5 1 2
Path_Straight_Air 2 4 1 2
Building_Corner 0 3 1 2
Building_Corner 3 2 1 2
Path_Straight_Air 2 1 1 2
Empty 1 0 1 2
Path_Branch 1 5 0 2
Path_Straight 2 4 0 2
Ground 0 3 0 2
Ground 0 2 0 2
Path_Straight 2 1 0 2
Ground 2 0 0 2
Empty 2 5 3 1
Empty 2 4 3 1
Building_Wall 1 3 3 1
Building_Wall 3 2 3 1
Empty 3 1 3 1
Empty 2 0 3 1
Empty 3 5 2 1
Empty 0 4 2 1
Building_Wall 1 3 2 1
Building_Wall 3 2 2 1
Empty 3 1 2 1
Empty 2 0 2 1
Path_Branch_Air 1 5 1 1
Path_Straight_Air 2 4 1 1
Building_Wall 1 3 1 1
Building_Wall 3 2 1 1
Path_Branch_Air 3 1 1 1
Path_Straight_Air 3 0 1 1
Path_Branch 1 5 0 1
Path_Straight 2 4 0 1
Ground 3 3 0 1
Ground 1 2 0 1
Path_Branch 3 1 0 1
Path_Straight 3 0 0 1
Empty 3 5 3 0
Empty 2 4 3 0
Building_Wall 1 3 3 0
Building_Wall 3 2 3 0
Empty 3 1 3 0
Empty 1 0 3 0
Empty 1 5 2 0
Empty 0 4 2 0
Building_Wall 1 3 2 0
Building_Wall 3 2 2 0
Empty 3 1 2 0
Empty 2 0 2 0
Path_Branch_Air 1 5 1 0
Path_Straight_Air 0 4 1 0
Building_Wall 1 3 1 0
Building_Wall 3 2 1 0
Path_Straight_Air 0 1 1 0
Empty 1 0 1 0
Path_Branch 1 5 0 0
Path_Straight 0 4 0 0
Ground 1 3 0 0
Ground 2 2 0 0
Path_Straight 0 1 0 0
Ground 0 0 0 0


"""

def main():
    string_cmds = output_string.split('\n')
    print(string_cmds)
    for string_cmd in string_cmds:
        if string_cmd == "": 
            continue
        [maya_name, rotation, x, y, z] = string_cmd.split(' ')
        rotation, x, y, z = int(rotation), int(x), int(y), int(z)
        if maya_name == 'Empty' or maya_name == 'Path_Branch_Air' or maya_name == 'Path_Corner_Air' or maya_name == 'Path_Straight_Air': 
            continue
        else:
            cmds.duplicate(f"{maya_name}", n=f"{maya_name}_{x}{y}{z}_{rotation}")
            cmds.select(f"{maya_name}_{x}{y}{z}_{rotation}")
            cmds.rotate(0, rotation*90, 0)
            cmds.move(x+1, y+1, z+1)
    return

if __name__ == "__main__":
    main()

