import csv
#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    data = csv.reader(data)
    x = []
    s = []
    for i in data:
        x.append(i)
    for i in x[0]:
        s.append(i)


    return s
    
# Read the csv file
f = open("data.csv")
print(get_column_names(f))