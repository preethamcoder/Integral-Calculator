import sys
def return_column_vals_from_csv_file(fname, input_column):
    f = open(fname, "r")
    column_list = f.readline()
    data = f.readlines()
    columns = column_list.split(",")
    h = "a"
    line1 = []
    output_list = []
    for col_name in columns:
        line1.append(col_name.lstrip())
    if input_column in line1:
        h = line1.index(input_column)
    elif input_column+'\n' in line1:
        h = line1.index(input_column+'\n')
    else:
        print("The element is invalid, try entering a different one.")
        return("")
    for elem in data:
        ind_data = elem.split(",")
        #print((ind_data[h].replace("\n", "")).lstrip())
        output_list.append((ind_data[h].replace("\n", "")).lstrip())
    return(output_list)
if __name__ == "__main__":
    inp_col = input("Enter the column name: ")
    resultant = return_column_vals_from_csv_file(sys.argv[1], inp_col)
    print(resultant)