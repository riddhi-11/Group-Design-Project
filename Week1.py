#Week 1

#Here we are initializing our list of subjects as a list of numbers. 
sub = [0,1]
#0 = Math
#1 = History

#Need to figure out how to use dictionaries here. 

#Here, we are taking user input 
a = int(input("User 1 enter subject:"))
b = int(input("User 2 enter subject:"))
c = int(input("User 3 enter subject:"))
d = int(input("User 4 enter subject:"))

#Collecting the user input in a list 
l = [a,b,c,d] #User is defined by their choice

#Function that takes a pair of users and checks if they entered the same subject.
#Input : A pair of user's inputs
#Output: Tuple of their inputs in case of a match. -1 in case of mismatch. 
def match(a,b): #match(a,b)
    if a == b:
        return (a,b)
    else:
        return -1

#Looping through the list of inputs from users and calling match. 
for i in range (0,len(l)):
    for j in range(i,len(l)-1):
         print(match(l[i],l[j+1]))

"""
Test case
User 1 enter subject:1
User 2 enter subject:1
User 3 enter subject:0
User 4 enter subject:0
(1, 1)
-1
-1
-1
-1
(0, 0)
"""
    

        