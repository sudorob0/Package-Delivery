class Truck:
    def __init__(
        self,
        depart_time: float,
        packages: list,
        capacity=16,
        speed=18,
        load=None,
        mileage=0.0,
        address="4001 South 700 East",
    ):
        """Creates a truck object"""
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.capacity,
            self.speed,
            self.load,
            self.packages,
            self.mileage,
            self.address,
            self.depart_time,
        )
