def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    list1 = []
    col = 0
    for i in data:
        list1.append(i.split(','))
    for e in list1[1]:
        col += 1



    return col

# Read the csv file
f = open("data.csv").read()
print(find_number_of_columns(f.split('\n')))