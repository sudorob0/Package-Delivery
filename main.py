import csv
from hash_table import ChainingHashTable
from pprint import pprint


with open("./WGUPS Package File.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    address_read = [row for row in reader]

pprint(address_read)

hash_map = ChainingHashTable()


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

def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)