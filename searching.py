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

def linear_search(sequence, number):
    list_of_idxs = []
    for idx, element in enumerate(sequence):
        if element == number:
            list_of_idxs.append(idx)
        else:
            pass
    distionary_of_found_numbers = {"position":list_of_idxs, "count": len(list_of_idxs)}
    return list_of_idxs

def pattern_search(sequence, pattern):
    set_of_idxs = set()
    pattern_length = len(pattern)
    for idx in range(0, len(sequence) - pattern_length):
        pattern_similarity = 0
        for idx_pattern, patten_element in enumerate(pattern):
            if sequence[idx + idx_pattern] ==patten_element:
                pattern_similarity = pattern_similarity + 1
            else:
                break
        if pattern_similarity == pattern_length:
            set_of_idxs.add(idx + pattern_length // 2 - 1)
        else:
            pass
    return set_of_idxs


def main():
   file_name = "sequential.json"
   kay_of_sequence = "dna_sequence"
   search_sequence = "ATA"
   sequential_data = read_data(file_name, kay_of_sequence)
   print(sequential_data)
   found_set = pattern_search(sequential_data, search_sequence)
   print(found_set)

if __name__ == '__main__':
    main()
    my_list = [1, 2, 5, 7]
    search_number = [5]
    found_number = linear_search(my_list, search_number)