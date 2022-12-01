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
        deadline=None,
    ):
        """Creates a package object"""
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.package_id,
            self.address,
            self.city,
            self.state,
            self.zipcode,
            self.deadline,
            self.weight,
        )

    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        elif self.departure_time > convert_timedelta:
            self.status = "On it's way"
        else:
            self.status = "Pending Pickup"


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
            package_deadline = package[5]
            package_weight = package[6]

            # create package object
            package = Package(
                package_id,
                package_address,
                package_city,
                package_state,
                package_zipcode,
                package_deadline,
                package_weight,
            )

            # Add packages to the package_list
            # package_list.append(package)

            hash_table.insert(package_id, package)


