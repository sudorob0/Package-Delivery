import csv
from pprint import pprint

with open("./WGUPS Distance Table test.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

pprint(data_read)





