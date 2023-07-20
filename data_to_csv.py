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
    record1 = ("Check Domain", "FCODE", "Additional Domain", {1, "test1"})
    record2 = ("Check Domain", "FCODE", "Additional Domain", {2, "test2"})
    record3 = ("Check Domain", "FTYP", "Additional Domain", {2, "test2"})
    array = [record1, record2, record3]
    output_dir = r"D:\project\python\github\python_examples"
    filename = os.path.join(output_dir, "result.csv")
    header = ["Check_Name", "Identifer", "Message", "Value"]
    array_to_csv(array, filename, header)