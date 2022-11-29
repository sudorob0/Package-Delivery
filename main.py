import csv
from hash_table import ChainingHashTable
from pprint import pprint

with open("./WGUPS Distance Table test.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    distance_read = [row for row in reader]

pprint(distance_read)

with open("./WGUPS Package File.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    package_read = [row for row in reader]

pprint(distance_read)

with open("./WGUPS Package File.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    address_read = [row for row in reader]

pprint(address_read)

hash_map = ChainingHashTable()

