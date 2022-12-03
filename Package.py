from HashTable import ChainingHashTable
import csv
import HashTable


class Package:
    def __init__(
        self,
        package_id: int,
        address: str,
        city: str,
        state: str,
        zipcode: int,
        weight: float,
        deadline: str,
        notes: str
    ):
        """Creates a package object"""
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.weight = weight
        self.deadline = deadline
        self.departure_time = None
        self.delivery_time = None
        self.truck = None
        self.status = "At Hub"
        self.notes = notes

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, s% s%" % (
            self.id,
            self.address,
            self.city,
            self.state,
            self.zipcode,
            self.weight,
            self.deadline,
            self.status,
            self.truck,
            self.notes
        )

    def update_status(self, current_time):
        if self.delivery_time <= current_time:
            # tabs added to make it line up with the other text when it prints
            self.status = "Delivered\t"
        elif self.departure_time <= current_time:
            self.status = "On it's way"
        else:
            self.status = "At Hub\t"

    def update_truck(self, truck_name):
        self.truck = truck_name


def load_package_data(filename, hash_table):
    """read package data and return a package list"""
    # utf-8-sif encoding is needed to remove unnecessary characters that are read in
    with open(filename, encoding='utf-8-sig') as raw_packages:
        package_data = csv.reader(raw_packages, delimiter=",")
        # loop through the package data
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_weight = package[5]
            package_deadline = package[6]
            package_notes = package[7]

            # create package object
            package = Package(
                package_id,
                package_address,
                package_city,
                package_state,
                package_zipcode,
                package_deadline,
                package_weight,
                package_notes
            )

            # add package to hash table
            hash_table.insert(package_id, package)



