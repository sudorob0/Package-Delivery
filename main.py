"""
Robert Uhl
010191437
NHP2 — NHP2 Task 1: WGUPS Routing Program
"""
import csv
import Truck
from HashTable import ChainingHashTable
from Package import Package
from pprint import pprint
import Distance


with open("./WGUPS Package File.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    package_read = [row for row in reader]


# Loads the package data
def load_package_data(filename):
    with open(filename) as package_list:
        package_data = csv.reader(package_list, delimiter=",")
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_deadline = package[5]
            package_weight = package[6]

            package = Package(
                package_id,
                package_address,
                package_city,
                package_state,
                package_zipcode,
                package_deadline,
                package_weight,
            )

            hash_table.insert(package_id, package)


# create truck instances
truck1 = Truck.Truck(
    packages=[1, 13, 14, 15, 16, 19, 20, 21, 30, 34, 40],
    depart_time=8
)

truck2 = Truck.Truck(
    packages=[3, 6, 18, 36, 37, 38],
    depart_time=8
                     )

truck3 = Truck.Truck(
    packages=[2, 4, 5, 25, 26, 28, 31, 32],
    depart_time=8
)


hash_table = ChainingHashTable()

load_package_data("WGUPS Package File.csv", hash_table)
