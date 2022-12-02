"""
Name: Robert Uhl
Student ID: 010191437
Task: NHP2 — NHP2 Task 1: WGUPS Routing Program
"""
# python libraries
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
    packages=[1, 6, 13, 14, 15, 16, 20, 21, 22, 29, 30, 34, 37, 40],
    depart_time = datetime.timedelta(hours=8, minutes=0)
)

truck2 = Truck.Truck(
    packages=[3, 12, 17, 18, 19, 23, 24, 26, 27, 35, 36, 38, 39],
    depart_time = datetime.timedelta(hours=10, minutes=20)
                     )

truck3 = Truck.Truck(
    packages=[2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 31, 32, 33],
    depart_time = datetime.timedelta(hours=9, minutes=5)
)

# Load packages objects into the hash table
load_package_data(PACKAGE_FILE, package_hash_table)

# varable to store total number of packages to be delivered
num_of_packages = (len(truck1.packages) + len(truck2.packages) + len(truck3.packages))

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
        next_address = 10000
        next_package = None
        for package in not_delivered:
            if check_distance(get_address_id(truck.address), get_address_id(package.address)) <= next_address:
                next_address = check_distance(get_address_id(truck.address), get_address_id(package.address))
                next_package = package
        # Adds next closest package to the truck package list
        truck.packages.append(next_package.id)
        # Removes the same package from the not_delivered list
        not_delivered.remove(next_package)
        # Takes the mileage driven to this packaged into the truck.mileage attribute
        truck.mileage += next_address
        # Updates truck's current address attribute to the package it drove to
        truck.address = next_package.address
        # Updates the time it took for the truck to drive to the nearest address
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time


deliver_packages(truck1)
deliver_packages(truck2)
# The below line of code ensures that truck 3 does not leave until either of the first two trucks are finished
# delivering their packages
truck3.depart_time = min(truck1.time, truck2.time)
deliver_packages(truck3)

def main():
    """"Function for the CLI"""
    # staticly set cuurent time
    current_time = datetime.timedelta(hours=7, minutes=0)

    # Print welcome message
    print("""Welcome to the WGUPS CLI.""")


    # Main loop.  Prompts user for actions until exit is chosen.
    while True:
        print(f''' 
        Current time is {current_time}
        1) Set time of day
        2) Print current package status
        3) Print truck status
        4) Print a single package info
        0) Exit ''')
        # user input
        selection = input('Please enter the number of your selection:\n').strip()

        # Conditional statement to allow user to give options
        if selection == "1":
            hour = input(
                "Please enter what hour it is (in military time):")
            minute  = input(
                "Please enter what minute it is:")
            current_time = datetime.timedelta(hours=int(hour), minutes=int(minute))
        elif selection == "2":
            # header
            print("ID\t| Deadline\t| Status\t\t\t| Address")
            for package_id in range(1, num_of_packages):
                package = package_hash_table.search(package_id)
                package.update_status(current_time)
                # conditional statement to add a tab to EOD so everything lines up
                format = ""
                if package.deadline == "EOD":
                    format = "\t"
                print(f"{package.id}\t| {package.deadline}{format}\t| {package.status}\t| {package.address}")
        elif selection == "4":
            user_package_id = input('Enter package ID:\n').strip()
            package = package_hash_table.search(int(user_package_id))
            print(f"address:{package.address},  current status:{package.status},  Departure:{package.departure_time},  ETA:{package.delivery_time}")
        elif selection == "0":
            "Your are now leaving the CLI. Goodbye."
            exit()
        else:
            print(f"{selection} is an invalid entry. Please try again.")

main()