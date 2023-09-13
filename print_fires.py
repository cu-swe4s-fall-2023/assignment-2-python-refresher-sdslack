import my_utils as utils
import sys

file_name = sys.argv[1]
country_column = int(sys.argv[2])
country = sys.argv[3]

if len(sys.argv) == 5:
    fires_column = int(sys.argv[4])
    fires = utils.get_column(file_name, country_column, country,
                         result_column = fires_column)
else:
    fires = utils.get_column(file_name, country_column, country)

print(fires)