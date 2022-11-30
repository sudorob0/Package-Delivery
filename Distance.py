import csv
import datetime

with open("./WGUPS Distance Table.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    distance_read = [row for row in reader]

with open("./WGUPS Address File.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    address_read = [row for row in reader]

def check_distance(x_value, y_value):
    """Find the distance between two addresses"""
    distance = distance_read[x_value][y_value]
    if distance == "":
        distance = distance_read[y_value][x_value]
    return float(distance)

def load_address(address):
    for row in address_read:
        if address in row[2]:
            return int(row[0])




