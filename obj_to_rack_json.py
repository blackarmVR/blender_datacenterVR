import json
import requests
import sys

if (len(sys.argv) != 4):
    print("")
    print("this script needs three arguments")
    print(" - the obj file")
    print(" - the room name")
    print(" - the rotation")
    print("python3 input.obj upload_racks.py roomname 1")
    print("")
    exit()

blocklist = []
roomName = sys.argv[2]
with open(sys.argv[1]) as fp:
    line = fp.readline()
    while line:
        if (line.startswith('o ')):
            name = line.rstrip("\n").split(' ')[1]
            xmin = None
            xmax = None
            ymin = None
            ymax = None
            zmin = None
            zmax = None
            reading = True
            while reading:
                if (line.startswith('v ')):
                    xyz = line.rstrip("\n").split(' ')
                    #x = float(xyz[3]) * -1
                    #y = float(xyz[2])
                    #z = float(xyz[1])
                    x = float(xyz[1])
                    y = float(xyz[3]) * -1
                    z = float(xyz[2])
                    if (xmin == None):
                        xmin = x
                    if (xmax == None):
                        xmax = x
                    if (ymin == None):
                        ymin = y
                    if (ymax == None):
                        ymax = y
                    if (zmin == None):
                        zmin = z
                    if (zmax == None):
                        zmax = z
                    if (x < xmin):
                        xmin = x
                    if (x  > xmax):
                        xmax = x
                    if (y < ymin):
                        ymin = y
                    if (y > ymax):
                        ymax = y
                    if (z < zmin):
                        zmin = z
                    if (z > zmax):
                        zmax = z
                if (line.startswith('usemtl')):
                    reading = False
                    blocklist.append({
                        "u_room_name": roomName,
                        "u_rack_name": name,
                        "u_rotation": sys.argv[3],
                        "u_x_center": (xmin + xmax) * 0.5,
                        "u_x_size": xmax - xmin,
                        "u_y_center": (ymin + ymax) * 0.5,
                        "u_y_size": ymax - ymin,
                        "u_z_center": (zmin + zmax) * 0.5,
                        "u_z_size": zmax - zmin,
                        "u_z_unit_start": 0.1
                        })
                line = fp.readline()
        line = fp.readline()
print(json.dumps(blocklist, indent=4, sort_keys=True))