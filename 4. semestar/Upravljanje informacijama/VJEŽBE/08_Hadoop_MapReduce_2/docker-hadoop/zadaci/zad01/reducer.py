import sys

current_variable = ""
current_value = 0
total_measurements = 0
variable = 0

for line in sys.stdin:
    line = line.strip()
    variable, value, measurements = line.split('\t')
    try:
        value = float(value)
        measurements = int(measurements)
    except ValueError:
        continue
    if current_variable == variable:
        current_value += value
        total_measurements += measurements
    else:
        if current_variable:
            print('%s\t%s\t%s' % (current_variable, current_value/total_measurements, total_measurements))
        current_variable = variable
        current_value = value
        total_measurements = measurements

if current_variable == variable:
    print('%s\t%s\t%s' % (current_variable, current_value/total_measurements, total_measurements))


