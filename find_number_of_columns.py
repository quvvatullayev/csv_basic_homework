import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    list1 = []
    sum = 0
    for i in data:
        list1.append(i)

    for i in list1[1]:
        sum += 1

    return sum

# Read the csv file
f = open("data.csv")
print(find_number_of_columns(csv.reader(f)))