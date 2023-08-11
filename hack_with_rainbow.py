from hashlib import sha256
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    # Read the input CSV file
    with open(input_file_name) as f:
        reader = csv.reader(f)
        # Open the output CSV file for writing
        with open(output_file_name, 'w', newline='') as w:
            writer = csv.writer(w)
            # Create an ordered dictionary to store username-password pairs from the input
            fileinfo = OrderedDict()
            for i in reader:
                fileinfo.setdefault(i[0], '')   # Initialize the password field for each username
                fileinfo[i[0]] += i[1]   # Concatenate the password for each username

            # Create an ordered dictionary to store the reverse-hashed passwords
            hashing = OrderedDict()
            for num in range(1000, 10000):
                hashing.setdefault(num, '')
                # Hash the number and store the result as the password for the corresponding number
                hashing[num] += sha256(str(num).encode('utf-8')).hexdigest()

            # Create an ordered dictionary to store the reversed hashing (password to number mapping)
            reverse_hashing = OrderedDict()
            for k, v in hashing.items():
                reverse_hashing[v] = k

            # Create a final ordered dictionary to store the reversed passwords and usernames
            final_dict = OrderedDict()
            for key1, value1 in fileinfo.items():
                for key2, value2 in reverse_hashing.items():
                    if key2 == value1:
                        final_dict.setdefault(key1, '')
                        final_dict[key1] += str(reverse_hashing[key2])

            # Write the reversed passwords and usernames to the output CSV file
            for key in final_dict.keys():
                writer.writerow((key, final_dict[key]))
