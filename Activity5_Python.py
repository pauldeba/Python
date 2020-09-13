# Write a Python program to create the multiplication table (from 1 to 10) of a number.
num = int(input('Enter a number:    '))
	
# use for loop to iterate 10 times
for i in range(1,11):
    print(num,"  X   ",i,"  =   ",i*num)
