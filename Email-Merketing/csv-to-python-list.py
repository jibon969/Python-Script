# importing the module
import csv
 
# open the file in read mode
filename = open('first-1600.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
email = []

# values to empty list
for col in file:
    email.append(col['E-mail'])
   
# printing lists
print('E-mail:', email)