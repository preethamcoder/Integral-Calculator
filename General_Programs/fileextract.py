import sys
def return_column_vals_from_csv_file(fname, n):
    f = open(fname, "r")
    z = f.readline()
    data = f.readlines()
    a = z.split(",")
    h = "a"
    line1 = []
    for quan in a:
        line1.append(quan.lstrip())
    if n in line1:
        h = line1.index(n)
    elif n+'\n' in line1:
        h = line1.index(n+'\n')
    else:
        print("The element is invalid, try entering a different one.")
        return
    for elem in data:
        ind_data = elem.split(",")
        print((ind_data[h].replace("\n", "")).lstrip())
if __name__ == "__main__":
    n = input("Enter the column name: ")
    return_column_vals_from_csv_file(sys.argv[1], n)