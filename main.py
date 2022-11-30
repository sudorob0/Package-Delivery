import csv

import Truck
from hash_table import ChainingHashTable
from pprint import pprint
import Distance


with open("./WGUPS Package File.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    package_read = [row for row in reader]


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
            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline_time, pWeight, pStatus)

            # Insert data into hash table
            package_hash_table.insert(pID, p)


# create truck instances
truck1 = Truck.Truck(capacity=16, speed=18, load=None, packages=[1, 13, 14, 15, 16, 19, 20, 21, 30, 34, 40], mileage=.0, address='4001 South 700 East', depart_time=8)

truck2 = Truck.Truck(capacity=16, speed=18, load=None, packages=[3, 6, 18, 36, 37, 38], mileage=.0, address='4001 South 700 East', depart_time=8)

truck3 = Truck.Truck(capacity=16, speed=18, load=None, packages=[2, 4, 5, 25, 26, 28, 31, 32], mileage=.0, address='4001 South 700 East', depart_time=8)

# create hash map
hash_map = ChainingHashTable()
