import maya.cmds as cmds

def main():
    f = open("/Users/omgitsmonday/procedural-city/output.txt", "r")
    string_cmds =f.readlines()
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

