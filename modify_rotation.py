import json
import sys

if (len(sys.argv) != 2):
    print("")
    print("this script need to be given the name of the json file as an argument")
    print("")
    exit()

try:
    with open(sys.argv[1], "r") as snow:
        snow_data = json.load(snow)
except:
    print("unable to import json")
    exit()
try:
    output = []
    for rack in snow_data:
        u_z_unit_start = 0.10
        rotation = rack["u_rotation"]
        # customize this part 
        if (rack["u_rack_name"].startswith('TEST-1-0-1-0-A')):
            rotation = 2
        if (rack["u_rack_name"].startswith('TEST-1-0-1-0-B')):
            rotation = 0
        if (rack["u_rack_name"].startswith('TEST-1-0-1-0-C')):
            rotation = 2
        if (rack["u_rack_name"].startswith('TEST-1-0-1-0-D')):
            rotation = 0
        if (rack["u_rack_name"].startswith('TEST-1-0-1-0-E')):
            rotation = 2
        if (rack["u_rack_name"].startswith('TEST-1-0-1-0-F')):
            rotation = 0
        ######
        output.append({
            "u_room_name": rack["u_room_name"],
            "u_rack_name": rack["u_rack_name"],
            "u_rotation": rotation,
            "u_x_center": rack["u_x_center"],
            "u_x_size": rack["u_x_size"],
            "u_y_center": rack["u_y_center"],
            "u_y_size": rack["u_y_size"],
            "u_z_center": rack["u_z_center"],
            "u_z_size": rack["u_z_size"],
            "u_z_unit_start": u_z_unit_start
        })
    print(json.dumps(output, indent=4, sort_keys=True))
except Exception as e:
    print(e)
    exit()
