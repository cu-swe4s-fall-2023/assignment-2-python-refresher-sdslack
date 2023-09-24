def get_column(file_name, query_column, query_value, result_column = 1):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.rstrip().split(',')
            if line[query_column] == query_value:
                result.append(line[result_column])
    result_mod = [int(round(float(val))) for val in result]

    return result_mod