import re
#Const
calibration_value = 0
units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
#Read txt file
with open('calibrationValues.txt') as f:
    lines = f.readlines()
f.close()
#Analyse
for line in lines:
    
    list_number = re.findall(r'\d', line)
    firt_num = list_number[0]
    last_num = list_number[-1]
    first_num_index = [iter.start() for iter in re.finditer(firt_num, line)][0]
    last_num_index = [iter.start() for iter in re.finditer(last_num, line)][-1] #  !!!! si "11" alors donne 0
    print('line :', line)
    for unit in units:
        if unit in line:
            list_iteration = [iter.start() for iter in re.finditer(unit, line)]
            if (list_iteration[0] < first_num_index):
                firt_num = str(units.index(unit))
                first_num_index = list_iteration[0]
            if (list_iteration[-1] > last_num_index):
                last_num = str(units.index(unit))
                last_num_index = list_iteration[-1]

    line_result = int(firt_num + last_num)
    calibration_value = calibration_value + line_result
    print('Result of the line :', line_result)
print('Calibration value :', calibration_value)