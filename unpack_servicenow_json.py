import json
import sys

if (len(sys.argv) != 2):
    print("")
    print("this script extracts the useful data from json downloaded from servicenow")
    print("the name of the json file needs to be given as an argument")
    print("")
    exit()

try:
    with open(sys.argv[1], "r") as raw:
        json_data = json.load(raw)
        output = []
        for rack in json_data["records"]:
            output.append({
                "u_room_name": rack["u_room_name"],
                "u_rack_name": rack["u_rack_name"],
                "u_rotation": rack["u_rotation"],
                "u_x_center": rack["u_x_center"],
                "u_x_size": rack["u_x_size"],
                "u_y_center": rack["u_y_center"],
                "u_y_size": rack["u_y_size"],
                "u_z_center": rack["u_z_center"],
                "u_z_size": rack["u_z_size"],
                "u_z_unit_start": rack["u_z_unit_start"]
            })
        print(json.dumps(output, indent=4))
except:
    print("unable to import json")
