import csv

# Change these constants for your file locations
DIRECTORY_PATH = ""
DISTANCE_FILE = "WGUPS Distance Table.csv"
ADDRESS_FILE = "WGUPS Address File.csv"

def check_distance(x_address_id: int, y_address_id: int):
    """Find the distance between two addresses. Supply address id integer for arguments."""
    # Read distance data from CSV
    with open(f"{DIRECTORY_PATH}{DISTANCE_FILE}") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        distance_data = [row for row in reader]

    distance = distance_data[x_address_id][y_address_id]
    # if distance is blank reverse the ids
    if distance == "":
        distance = distance_data[y_address_id][x_address_id]
    return float(distance)

def get_address_id(address):
    """Get address id from supplied address string"""
    # Read address data from CSV
    with open(f"{DIRECTORY_PATH}{ADDRESS_FILE}") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        address_data = [row for row in reader]
    # Loop through lines in csv file, find the address and return the address id
    for row in address_data:
        if address in row[2]:
            return int(row[0])
