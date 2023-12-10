import re

calibration_value = 0

with open('calibrationValues.txt') as f:
    lines = f.readlines()
f.close()
for line in lines:
    list_number = re.findall(r'\d', line)
    firt_num = list_number[0]
    last_num = list_number[-1]
    line_result = int(firt_num + last_num)
    calibration_value = calibration_value + line_result
    print('Result of the line :', line_result)
print('Calibration value :', calibration_value)