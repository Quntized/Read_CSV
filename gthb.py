def Parse_header(header_line):
    return header_line.strip().split(',')
def parse_values(Data_line):
    values = []
    for item in Data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values
def Create_item_dict(values,headers):
    result = {}
    for value,header in zip(values , headers):
        result[header] = value
    return result

def read_csv(path):
    result = []
    with open(path,mode = 'r') as file:
        lines = file.readlines()
        header = Parse_header(lines[0])
        for data_line in lines[1:]:
            values = parse_values(data_line)
            item_dict = Create_item_dict(values, header)
            result.append(item_dict)
    