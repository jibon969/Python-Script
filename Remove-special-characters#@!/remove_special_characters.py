
# Remove Special $#! characters using re
# Example : Special $#! characters   spaces 888323

import re
my_string = input("Please enter your text :  ")
cleanString = re.sub('\W+',' ', my_string)
print(cleanString)
print('\n')





                




