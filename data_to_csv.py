import os
import numpy as np
import csv


def array_to_csv(array, filename, header=None):
    """Converts an array to a NumPy array and then writes the NumPy array to a CSV file.

    Args:
        array: The array to be converted.
        filename: The filename of the CSV file to be written.
        header: The header to be written to the CSV file.
    """

    np_array = np.array(array)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if header:
            writer.writerow(header)
        writer.writerows(np_array)


if __name__ == '__main__':
    # record1 = ("Check Domain", "FCODE", "Additional Domain", {1, "test1"})
    # record2 = ("Check Domain", "FCODE", "Additional Domain", {2, "test2"})
    # record3 = ("Check Domain", "FTYP", "Additional Domain", {2, "test2"})
    # array = [record1, record2, record3]
    # output_dir = r"D:\project\python\github\python_examples"
    # filename = os.path.join(output_dir, "result.csv")
    # header = ["Check_Name", "Identifer", "Message", "Value"]
    # array_to_csv

    differences = []
    list1 = [[1, 2], [3, 4], [5, 6]]
    list2 = [[3, 4], [7, 9]]
    dict_arr_list1 = [{item[0], item[1]} for item in list1]
    dict_arr_list2 = [{item[0], item[1]} for item in list2]

    for item in list2:
        diff_items = [item for item_list1 in list1 if (item[0] == item_list1[0]) and (item[1] == item[2])]
        if len(diff_items) == 0:
            differences.append(diff_items)


    # differences = [(a, b) for a, b in zip(list1, list2) if a != b]

    # If one list is longer than the other, we need to account for the remaining elements
    # if len(list1) > len(list2):
    #     differences.extend(list1[len(list2):])
    # elif len(list2) > len(list1):
    #     differences.extend(list2[len(list1):])

    print(differences)