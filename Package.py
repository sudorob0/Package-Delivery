class Package:
    # initializing package class
    def __init__(self, package_id, address, city, state, zipcode, deadline_time, weight, status):
        # defining attributes
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline_time = deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
    # defining a str method to return attributes in string format
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state, self.zipcode,
                                                       self.deadline_time, self.weight, self.delivery_time,
                                                       self.status)

    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        elif self.departure_time > convert_timedelta:
            self.status = "Out for delivery"
        else:
            self.status = "Pending Pickup"