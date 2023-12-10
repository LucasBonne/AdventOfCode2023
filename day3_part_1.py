import re
list_of_all_numbers = []

with open('day3.txt') as f:
    lines = f.readlines()
f.close()

for line in lines:
    list_number = [eval(i) for i in re.findall(r'\d+', line)]
    for idx, value in enumerate(list_number):
        if id
    list_of_all_numbers.append()