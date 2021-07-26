import csv

 #list of elements to calculate mean
with open("HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#remove the title list from the data
file_data.pop(0)

#create an empty list
new_data = []

#sorting data  to get the height of people.
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(n_num)

#length of the list
n = len(new_data)

#sorts the data in ascending order
new_data.sort()

#If the length is an even number then there will be 2 values as medians and we'll have to find the mean of those two values.
if(n % 2 == 0):
    #getting the first number
	median1 = float(new_data[n//2])
    #getting the second number
	median2 = float(new_data[n//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2

#If the length is an odd number then we don't need to find the mean
else:
    median = new_data[n//2]

print("Median is: " + str(median))

