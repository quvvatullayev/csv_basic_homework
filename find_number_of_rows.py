import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    x = csv.reader(data)
    sum = 1
    for i in x:
        sum += 1

    return sum

# Read the csv file
f = open("data.csv")
print(find_number_of_rows(f))

# Read the csv file
