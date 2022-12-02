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
    depart_time=datetime.timedelta(hours=8, minutes=0),
)

truck2 = Truck.Truck(
    packages=[3, 12, 17, 18, 19, 23, 24, 26, 27, 35, 36, 38, 39],
    depart_time=datetime.timedelta(hours=9, minutes=10),
)

truck3 = Truck.Truck(
    packages=[2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 31, 32, 33],
    depart_time=datetime.timedelta(hours=11, minutes=5),
)

# Load packages objects into the hash table
load_package_data(PACKAGE_FILE, package_hash_table)

# variable to store total number of packages to be delivered
num_of_packages = len(truck1.packages) + len(truck2.packages) + len(truck3.packages)


def deliver_packages(truck):
    """Method for ordering the packages in a truck using nearest neighbor algorithm"""
    # create empty list to hole packages not yet delivered
    not_delivered = []
    # Loop through packages in a truck
    for package_id in truck.packages:
        # Find package in the hash table
        package = package_hash_table.search(package_id)
        # Add package to not_delivered list
        not_delivered.append(package)
    # Clear package list
    truck.packages.clear()
    # While loop to loop through all not_delivered packages
    while len(not_delivered) > 0:
        # set address to be longer than any address we will get, so it will be replaced
        next_address_distance = 10000
        next_package = None
        for package in not_delivered:
            """ 
                Conditional statement that gets the current truck address and the package address 
                and compares it to the distance of the next address
                The first loop will hit because the next address is set really high
            """
            if (
                check_distance(
                    get_address_id(truck.address), get_address_id(package.address)
                )
                <= next_address_distance
            ):
                # If the current address is a shorter distance then it will replace next_address value
                next_address_distance = check_distance(
                    get_address_id(truck.address), get_address_id(package.address)
                )
                next_package = package
        # Adds the package with the smallest distance from current address to the truck
        truck.packages.append(next_package.id)
        # Removes the delivered package from the not_delivered list
        not_delivered.remove(next_package)
        # Updates the trucks total mileage
        truck.mileage += next_address_distance
        # Updates truck's current address attribute to the package it drove to
        truck.address = next_package.address
        # Updates the trucks time with the time it took to deliver package
        truck.time += datetime.timedelta(hours=next_address_distance / 18)
        # Updates the package with the delivery and departure time of the truck
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time

# start delivering packages
deliver_packages(truck1)
deliver_packages(truck2)
# truck3's departure time will start once both truck1&2 are done
truck3.depart_time = min(truck1.time, truck2.time)
deliver_packages(truck3)


def main():
    """ "Function for the CLI"""
    # start with a 7am time for current time
    current_time = datetime.timedelta(hours=7, minutes=0)

    # Print welcome message
    print("""Welcome to the WGUPS CLI.""")

    # Main loop.  Prompts user for actions until exit is chosen.
    while True:
        print(
            f""" 
        Current time is {current_time}
        1) Set time of day
        2) Current package status
        3) Truck status
        4) Single package status
        0) Exit """
        )
        # user input
        selection = input("Please enter the number of your selection:\n").strip()

        # Conditional statement to allow user to give options
        if selection == "1":
            hour = input("Please enter what hour it is (in military time):")
            minute = input("Please enter what minute it is:")
            # Update current time with user input
            current_time = datetime.timedelta(hours=int(hour), minutes=int(minute))
        elif selection == "2":
            print(f"Current Time: {current_time}")
            # header
            print("ID\t| Deadline\t| Status\t\t| Departure\t\t| Delivery\t\t| Address")
            print("-" * 80)
            # Loop through all packages
            for package_id in range(1, num_of_packages + 1):
                # Find package in hash table
                package = package_hash_table.search(package_id)
                # Update package status
                package.update_status(current_time)
                # Update departure and delivery time if packages are on its way or delivered
                timestamp = "Pending\t\t| Pending"
                if "Delivered" in package.status:
                    timestamp = f"{package.departure_time}\t\t| {package.delivery_time}"
                elif package.status == "On it's way":
                    timestamp = f"{package.departure_time}\t\t| Pending"
                # conditional statement to add a tab to EOD so everything lines up
                format = ""
                if package.deadline == "EOD":
                    format = "\t"
                print(
                    f"{package.id}\t| {package.deadline}{format}\t| {package.status}\t| {timestamp}\t\t| {package.address}"
                )
        elif selection == "3":
            print("Truck #\t\t| Departure\t| Mileage\t| Location\t\t\t| Packages")
            print("-" * 80)
            print(
                f"Truck 1\t\t| {truck1.depart_time}\t| {truck1.mileage}\t\t| {truck1.address}\t| {truck1.packages}"
            )
            print(
                f"Truck 2\t\t| {truck2.depart_time}\t| {truck2.mileage}\t\t| {truck2.address}\t\t| {truck2.packages}"
            )
            print(
                f"Truck 3\t\t| {truck3.depart_time}\t| {truck3.mileage}\t\t| {truck3.address}\t\t| {truck3.packages}"
            )
            print(f"Total Mileage: {truck1.mileage + truck2.mileage + truck3.mileage}")
        elif selection == "4":
            user_package_id = input("Enter package ID:\n").strip()
            package = package_hash_table.search(int(user_package_id))
            # Update departure and delivery time if packages are on its way or delivered
            timestamp = (
                "Departure Time: Awaiting pickup\nDelivery Time: Pending delivery"
            )
            if "Delivered" in package.status:
                timestamp = f"Departure: {package.departure_time}\nDelivered: {package.delivery_time}"
            elif package.status == f"On it's way\t":
                "Departure:{package.departure_time},\nDelivered:Pending delivery"
            print(
                f"Current Time:{current_time}\nAddress: {package.address}\nCurrent Status: {package.status}\n{timestamp}"
            )
        elif selection == "0":
            # Exit out of CLI
            "Your are now leaving the CLI. Goodbye."
            exit()
        else:
            # Else for invalid entries
            print(f"{selection} is an invalid entry. Please try again.")


main()
