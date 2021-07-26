import csv

# list of elements to calculate mean
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
    new_data.append(float(n_num))

#getting the mean
n = len(new_data) # finding number of values
total = 0
for x in  new_data: # finding sum of values
    total = total + x

mean = total/n

print("Mean / Average is: " + str(mean))

