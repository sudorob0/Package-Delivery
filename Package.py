from HashTable import ChainingHashTable
import csv


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
            self.status = "Out for delivery"
        else:
            self.status = "Pending Pickup"
