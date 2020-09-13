"""Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list 
and even numbers from the second list.
"""

a=[1,3,6,9,8]
b=[2,4,7,9]
# Print the lists
print("First List ", a)
print("Second List ", b)
 
# Declare a third list that will contain the result
c=[]
for i in a:
    if(i%2!=0):
        c.append(i)
for j in b:
    if(j%2==0):
        c.append(j)        

# Print result
print("result List is:")
print(c)