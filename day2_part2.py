import re

valid_game = 0
error = 0
sum_of_all = 0

with open('cubeConundrum.txt') as f:
    lines = f.readlines()
f.close()

for line in lines:
    red_min = 0
    blue_min = 0
    green_min = 0
    list_number = [eval(i) for i in re.findall(r'\d+', line)]
    warning_list = re.findall(r'\d\d+ [A-Za-z_]+', line)
    for warning in warning_list:
        if int(re.findall(r'\d+', warning)[0]) > 12 and re.findall(r'red', warning):
            print('red :',line)
            error = 1
        elif int(re.findall(r'\d+', warning)[0]) > 13 and re.findall(r'green', warning):
            print('green', line)
            error = 1
        elif int(re.findall(r'\d+', warning)[0]) > 14 and re.findall(r'blue', warning):
            print('blue', line)
            error = 1
    if error == 0 :
        valid_game = valid_game + int(list_number[0])
    error = 0
    part_of_line_list = re.findall(r'\d+ [A-Za-z_]+', line)
    for part in part_of_line_list:
        if 'red' in part and red_min < int(re.findall(r'\d+', part)[0]):
            red_min = int(re.findall(r'\d+', part)[0])
            print(red_min)
        elif 'green' in part and green_min < int(re.findall(r'\d+', part)[0]):
            green_min = int(re.findall(r'\d+', part)[0])
            print(green_min)
        elif 'blue' in part and blue_min < int(re.findall(r'\d+', part)[0]):
            blue_min = int(re.findall(r'\d+', part)[0])
            print(blue_min)
    line_value = blue_min * red_min * green_min
    sum_of_all = sum_of_all + line_value

print(valid_game)
print(sum_of_all)