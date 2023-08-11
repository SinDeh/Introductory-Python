import csv
# For the average
from statistics import mean
from collections import OrderedDict
import numpy as np


def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w', newline='') as o:
            writer = csv.writer(o)
            result = OrderedDict()
            for k in reader:
                result.setdefault(k[0], 0)
                result[k[0]] += mean(np.float_(k[1:]))
            for key in result.keys():
                writer.writerow((key, result[key]))

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w', newline='') as o:
            writer = csv.writer(o)
            result = OrderedDict()
            for k in reader:
                result.setdefault(k[0], 0)
                result[k[0]] += mean(np.float_(k[1:]))
            sort_key = OrderedDict(sorted(result.items(), key=lambda x:x[0]))
            sort_value = OrderedDict(sorted(sort_key.items(), key=lambda x:x[1]))
            for key in sort_value.keys():
                writer.writerow((key, sort_value[key]))



def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w', newline='') as o:
            writer = csv.writer(o)
            result = OrderedDict()
            for k in reader:
                result.setdefault(k[0], 0)
                result[k[0]] += mean(np.float_(k[1:]))
            sort_key = OrderedDict(sorted(result.items(), key=lambda x:x[0]))
            sort_value = OrderedDict(sorted(sort_key.items(), key=lambda x:x[1]))
            a= []
            for j in sort_value.items():
                a.append(j)
            top3 = []
            for l in range(-1, -4, -1):
                top3.append(a[l])
            sorte = OrderedDict()
            for key, value in top3:
                sorte.setdefault(key, 0)
                sorte[key] += value
            sort_key = OrderedDict(sorted(sorte.items(), key=lambda x:x[0]))
            sort_value = OrderedDict(sorted(sort_key.items(), key=lambda x:x[1], reverse=True))
            for key in sort_value.keys():
                writer.writerow((key, sort_value[key]))


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w', newline='') as o:
            writer = csv.writer(o)
            result = OrderedDict()
            for k in reader:
                result.setdefault(k[0], 0)
                result[k[0]] += mean(np.float_(k[1:]))
            result1 = OrderedDict(sorted(result.items(), key=lambda x:x[1]))
            a= []
            for j in result1.items():
                a.append(j)
            down3 = []
            for l in range(0, 3, 1):
                down3.append(a[l])
            sorte = OrderedDict()
            for key, value in down3:
                sorte.setdefault(key, 0)
                sorte[key] += value
            sort_value = OrderedDict(sorted(sorte.items(), key=lambda x:x[1]))
            for value in sort_value.values():
                writer.writerow([value])
                


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        with open(output_file_name, 'w', newline='') as o:
            writer = csv.writer(o)
            result = OrderedDict()
            for k in reader:
                result.setdefault(k[0], 0)
                result[k[0]] += mean(np.float_(k[1:]))
            total_average = OrderedDict()
            total_average.setdefault('total_average', mean(result.values()))
            for value in total_average.values():
                writer.writerow([value])
