bill_thickness = 0.11 * 0.001
sears_height = 442
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)