def import_data(filename):
    with open(filename) as file:
        lines=file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def split_data(lines):
    s = lines[0]
    collum_data = lines[1]
    row_data = lines[2]
    box_data = lines[3:]
    return s, row_data, collum_data, box_data

def format_1d_array(lst, var_name):
    result = var_name + " = [ "
    for i in lst:
        #result = result + str(i) + ", "
        result += i.replace(" ",",") 
    result +=  "];\n"
    return result

def format_2d_array(lst, var_name):
    result =  var_name + " = ["
    for elem in lst:
        result += "|"+elem.replace(" ",",") + "\n"
    result = result[:-1] + "|];\n"
    return result

def format_data(s,row_data,collum_data,box_data):
    s = "s = " + s + ";\n"
    row_data = format_1d_array(row_data, "row_data")
    collum_data = format_1d_array(collum_data, "collum_data")
    box_data = format_2d_array(box_data, "box_data")
    return [s, row_data,collum_data,box_data]

def write_to_file(data, filename):
    with open(filename, "w") as file:
        for string in data:
            file.write(string)

def main():
    for i in range(6):
        in_file= "data/instance." + str(i) + ".in"
        out_file = "test" + str(i) + ".dzn"
        raw_data = import_data(in_file)
        s, row_data, collum_data, box_data = split_data(raw_data)
        final_data = format_data(s,row_data,collum_data,box_data)

        write_to_file(final_data, out_file)
main()
