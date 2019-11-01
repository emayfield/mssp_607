
def build_districts_list(districts_filename):
    districts_list = []
    with open(districts_filename) as districts_file:
        districts_input = districts_file.readlines()
        row_number = 0
        header_row = []
        for row in districts_input:
            if row_number == 0:
                header_row = row.strip().split(",")
            else:
                district_row = row.split(",")
                district_facts = {}
                for column_number in range(len(district_row)):
                    column_name = header_row[column_number]
                    cell_value = district_row[column_number]
                    try:
                        cell_value = int(cell_value)
                    except ValueError:
                        pass
                    district_facts[column_name] = cell_value
                districts_list.append(district_facts)
            row_number += 1
    return districts_list

import csv

def build_districts_list_csv(districts_filename):
    districts_list = []
    with open(districts_filename) as districts_file:
        districts_input = csv.reader(districts_file)
        header_row = []
        for i, row in enumerate(districts_input):
            if i == 0:
                header_row = row
            else:
                district_facts = {}
                for column_number in range(len(row)):
                    column_name = header_row[column_number]
                    cell_value = row[column_number]
                    try:
                        cell_value = int(cell_value)
                    except ValueError:
                        pass
                    district_facts[column_name] = cell_value
                districts_list.append(district_facts)
    return districts_list

