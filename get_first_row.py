import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   data = csv.reader(data)
   x = []
   for i in data:
        x.append(i[0])
   return x

# Read the csv file
f = open("data.csv")
print(get_first_row(f))