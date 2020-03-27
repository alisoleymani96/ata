import hashlib
import csv


def ID_hash_converter(input_file_name, output_file_name):

    container = {}

    for four_digit_number in range(10000):

        four_digit_number_str = '{:04}'.format(four_digit_number)
        m = hashlib.sha256(four_digit_number_str.encode())
        container[m.hexdigest()] = four_digit_number

    with open(input_file_name, newline='') as f_input, open(output_file_name, 'w', newline='') as f_output:
        """
        If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correctly,
        and on platforms that use \r\n linendings on write an extra \r will be added.
        It should always be safe to specify newline='', since the csv module
        does its own (universal) newline handling.
        """

        csv_input = csv.reader(f_input)
        csv_output = csv.writer(f_output)

        for ID, encoded_ID in csv_input:
            csv_output.writerow([ID, container[encoded_ID]])


ID_hash_converter('input.csv', 'output.csv')
