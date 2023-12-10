import re

valid_game = 0
error = 0

with open('cubeConundrum.txt') as f:
    lines = f.readlines()
f.close()

for line in lines:
    list_number = [eval(i) for i in re.findall(r'\d+', line)]
    warning_list = re.findall(r'\d\d+ [A-Za-z_]+', line)
    for warning in warning_list:
        if int(re.findall(r'\d+', warning)[0])>12 and re.findall(r'red', warning):
            print('red :',line)
            error = 1
        elif int(re.findall(r'\d+', warning)[0])>13 and re.findall(r'green', warning):
            print('green', line)
            error = 1
        elif int(re.findall(r'\d+', warning)[0])>14 and re.findall(r'blue', warning):
            print('blue', line)
            error = 1
    if error == 0 :
        valid_game = valid_game + int(list_number[0])
    error = 0
#    if re.findall(r'\d\d+ \w+,', line):       
#        print(line)
#        print(list_number)
#    else:
#        valid_game = valid_game + int(list_number[0])

print(valid_game)