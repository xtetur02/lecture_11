import os
import json
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
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]


def linear_search(sequence, number):
    slovnik = {"positions": [], "count": 0} #zadefinovani prazdneho slovniku s klicema
    for index, num in enumerate(sequence):
        if number == num:
            slovnik["positions"].append(index)
            slovnik["count"] = slovnik["count"] + 1
    return slovnik


def pattern_search(sequence, vzor):
    mnozina_idx = set()
    index = 0
    while index < len(sequence) - len(vzor):
        idx = 0
        for letter in sequence[index:index+len(vzor)]:
            if letter != vzor[idx]:
                break
            else:
                idx += 1
        if idx == len(vzor):
            mnozina_idx.add(index)
        index += 1

    return mnozina_idx


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    hledane_cislo = 5
    results = linear_search(sequential_data, hledane_cislo)
    print(results)
    sequence = read_data("sequential.json", "dna_sequence")
    vzor = "ATA"
    dna_search = pattern_search(sequence, vzor)
    print(dna_search)

if __name__ == '__main__':
    main()