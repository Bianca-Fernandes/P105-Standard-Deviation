import csv
import math

with open("C:/Users/91982/OneDrive/Desktop/Python/Project/P105 Standard Deviation/data.csv", newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for a in data:
        total += int(a)
    
    mean = total/n
    return mean

squared_list= []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum + i

result = sum/(len(data)-1)

std_d = math.sqrt(result)
print(std_d)
