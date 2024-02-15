#Week 2

#Here we are initializing our list of subjects as a list of numbers. 
sub = [0,1]
#0 = Math
#1 = History

#Dictionary implemeantion: 

def stumble(n): #n is number of users
    q = {} #Empty dictionary
    for i in range(4): #Our pilot is for 4 users. 
        a=input("Enter username:") #Unique username.
        b=int(input("Enter subject:")) #from sub
        q[a]=b #Adding the username and subject as a key-value pair to the dictionary.
    g= {} #Initializing an empty dictionary for the grouping. 
    for key, value in q.items():
    # If the value is not already a key in groups, add it with an empty list as the value
        if value not in g:
            g[value] = []
            # Append the key to the list corresponding to its value in the groups dictionary
        g[value].append(key)
    print(g)

stumble(4) #Our pilot is for 4 users. 

"""
Enter username:User1
Enter subject:1
Enter username:User2
Enter subject:1
Enter username:User3
Enter subject:0
Enter username:User4
Enter subject:0
{1: ['User1', 'User2'], 0: ['User3', 'User4']}
"""
