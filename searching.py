import os
import json
from operator import index

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with  open(file_path, "r") as file_obj:
        data = json.load(file_obj)
    if field in data.keys():
        return data(field)
    else:
        print(f'Field {field} not exist')
        return None




def linear_search(list_of_numbers, number):
    list_of_idxs = []
    for idx, element in enumerate(list_of_numbers):
        if element == number:
            list_of_idxs.append(idx)
        else:
            pass
    distionary_of_found_numbers = {"position":list_of_idxs, "count": len(list_of_idxs)}
    return list_of_idxs

def main():
    sequential_data = read_data("sequential.json", "unorded.numbers")
    print(sequential_data)
    found_number_linear = linear_search(sequential_data, 0)
    print(found_number_linear)

if __name__ == '__main__':
    main()
    my_list = [1, 2, 5, 7]
    search_number = [5]
    found_number = linear_search(my_list, search_number)