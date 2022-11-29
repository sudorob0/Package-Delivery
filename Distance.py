import csv
import datetime

class Distance:

    # pull distance addresses and names from csv file
    with open('WGUPS Address File.csv') as address_file:
        address_reader = list(csv.reader(address_file, delimiter=','))

    # pull distance data from csv file
    with open('WGUPS Distance Table.csv') as distance_file:
        distance_reader = list(csv.reader(distance_file, delimiter=','))

    print(distance_reader)
    # get distance between locations
    def check_distance(self, current_location, from_location):
        row = int(current_location)
        column = int(from_location)
        distance = self.distance_reader[row][column]
        if distance == None or distance == "":
            distance = self.distance_reader[column][row]
            return distance


    def check_current_distance(self, row, column):
        distance = distance_reader[row][column]
        if distance == "":
            break




