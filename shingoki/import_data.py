def import_data(filename):
    with open(filename) as file:
        lines=file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def split_data(lines):
    s_w_b = lines[0].split(" ")
    white = lines[1:int(s_w_b[1])+1]
    black = lines[int(s_w_b[1])+1:]
    return s_w_b, white, black

def format_1d_array(lst, var_name):
    result = var_name + " = [ "
    for i in lst:
        result += str(i) + ","
    result = result[:-1] +"];\n"
    return result
def format_size_data(data):
    s = "s = "+str(data[0])+ ";\n"
    w = "w = "+str(data[1])+ ";\n"
    b = "b = "+str(data[2])+ ";\n"
    return [s,w,b]
def format_circle(data, name):
    x = []
    y = []
    value = []
    for line in data: 
        split_l = line.split(' ')
        x.append(split_l[0])
        y.append(split_l[1])
        value.append(split_l[2])
    return [format_1d_array(x,'x_'+name), format_1d_array(y,'y_'+name),format_1d_array(value,'value_'+name)]

def write_to_file(data, filename):
    with open(filename, "w") as file:
        for string in data:
            file.write(string)

lines = import_data("data/instance.0.in")
s_w_b, white, black = split_data(lines)
white_data = format_circle(white, "white")
black_data = format_circle(black, "black")
size_data = format_size_data(s_w_b)
all_data = size_data + white_data + black_data

write_to_file(all_data, "test0.dzn")
