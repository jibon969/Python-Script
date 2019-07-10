
# Find all files in a directory with extension

your_location = input("Enter your location : ")
your_extension = input (str('your extension file name : ', ))

import os, os.path
for root, dirs, files in os.walk(your_location):
    for file in files:
        full_path = os.path.join(root, file)
        if os.path.splitext(full_path)[1] == "." + your_extension:
            print("You wanted it : ", full_path)
            
print("Thank you")

 
        
    


