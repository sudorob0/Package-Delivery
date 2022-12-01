"""
Robert Uhl
010191437
NHP2 — NHP2 Task 1: WGUPS Routing Program
"""
# python libraries
import csv
import datetime
# project files
import Truck
import HashTable
from Package import load_package_data
from Distance import check_distance, get_address_id

# Change these constants for your file locations
PACKAGE_FILE = "WGUPS Package File.csv"

# Create hash table instance to store packages
package_hash_table = HashTable.ChainingHashTable()

# create truck instances, manually load packages and set departure times
truck1 = Truck.Truck(
    packages=[1, 13, 14, 15, 16, 19, 20, 21, 22, 30, 34, 40],
    depart_time=datetime.timedelta(hours=8, minutes=0)
)

truck2 = Truck.Truck(
    packages=[3, 6, 12, 17, 18, 23, 24, 26, 27, 35, 36, 37, 38, 39],
    depart_time=datetime.timedelta(hours=10, minutes=20)
                     )

truck3 = Truck.Truck(
    packages=[2, 4, 5, 7, 8, 9, 10, 11, 25, 26, 28, 31, 32],
    depart_time=datetime.timedelta(hours=9, minutes=5)
)

# Load packages objects into the hash table
load_package_data(PACKAGE_FILE, package_hash_table)


def deliver_packages(truck):
    """Method for ordering the packages in a truck using nearest neighbor algorithm"""
    # create empty list to hole packages not yet delivered
    not_delivered = []
    for packageID in truck.packages:
        package = package_hash_table.search(packageID)
        not_delivered.append(package)
    truck.packages.clear()

    while len(not_delivered) > 0:
        # set address to be longer than any address we will get, so it will be replaced
        next_address = 100000
        next_package = None
        for package in not_delivered:
            if check_distance(get_address_id(truck.address), get_address_id(package.address)) <= next_address:
                next_address = check_distance(get_address_id(truck.address), get_address_id(package.address))
                next_package = package
                # Adds next closest package to the truck package list
            truck.packages.append(next_package.ID)
            # Removes the same package from the not_delivered list
            not_delivered.remove(next_package)
            # Takes the mileage driven to this packaged into the truck.mileage attribute
            truck.mileage += next_address
            # Updates truck's current address attribute to the package it drove to
            truck.address = next_package.address
            # Updates the time it took for the truck to drive to the nearest package
            truck.time += datetime.timedelta(hours=next_address / 18)
            next_package.delivery_time = truck.time
            next_package.departure_time = truck.depart_time


deliver_packages(truck1)
deliver_packages(truck2)
# The below line of code ensures that truck 3 does not leave until either of the first two trucks are finished
# delivering their packages
truck3.depart_time = min(truck1.time, truck2.time)
deliver_packages(truck3)