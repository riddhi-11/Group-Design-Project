#Collecting user data and storing using dictionary. 


# Initialize an empty dictionary to store user details
user_dict = {}

# Loop to collect details from users(2)
for _ in range(2):
    # Prompting the user for details
    username = input("Enter Username: ")
    name = input("Enter Name: ")
    pronouns = input("Enter Preferred pronouns: ")
    age = int(input("Enter Age: "))
    country = input("Enter Country: ")
    title = input("Enter Current title (Student/Professor/Working professional/Freelancer/Other): ")
    interest = input("Enter Area of interest (Math/History/Biology): ")
    looking_for = input("Enter Looking for (Mentor/Mentee/Internship/Friend/Project): ")

    # Store user details in the dictionary
    user_dict[username] = [name, pronouns, age, country, title, interest, looking_for]

print(user_dict)
