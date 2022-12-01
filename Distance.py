import csv
import datetime

# Change these constants for your file locations
DIRECTORY_PATH = ""
DISTANCE_FILE = "WGUPS Distance Table.csv"
ADDRESS_FILE = "WGUPS Address File.csv"

# Read distance data from CSV
with open(f"{DIRECTORY_PATH}{DISTANCE_FILE}") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    distance_read = [row for row in reader]

# Read address data from CSV
with open(f"{DIRECTORY_PATH}{ADDRESS_FILE}") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    address_read = [row for row in reader]

def check_distance(distance_data, x_address_id: int, y_address_id: int):
    """Find the distance between two addresses. Supply address id integer for arguments."""
    distance = distance_data[x_address_id][y_address_id]
    # if distance is blank reverse the ids
    if distance == "":
        distance = distance_data[y_address_id][x_address_id]
    return float(distance)


def get_address_id(address_data, address):
    """Get address id from supplied address string"""
    for row in address_data:
        if address in row[2]:
            return int(row[0])
