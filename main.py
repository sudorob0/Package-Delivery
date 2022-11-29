import csv
from hash_table import ChainingHashTable
from pprint import pprint

with open("./WGUPS Distance Table.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    distance_read = [row for row in reader]

pprint(distance_read)

with open("./WGUPS Address File.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    address_read = [row for row in reader]

pprint(address_read)

with open("./WGUPS Package File.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    address_read = [row for row in reader]

pprint(address_read)

hash_map = ChainingHashTable()


def load_package_data(filename, package_hash_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline_time = package[5]
            pWeight = package[6]
            pStatus = "At Hub"

            # Package object
            p = Package(
                pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus
            )

            # Insert data into hash table
            package_hash_table.insert(pID, p)


def distance_in_between(x_value, y_value):
    """Find the distance between two addresses"""
    distance = distance_read[x_value][y_value]
    if distance == "":
        distance = distance_read[y_value][x_value]

    return float(distance)
