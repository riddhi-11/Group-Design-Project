import tkinter as tk

# Given user data stored in a dictionary
user_dict = {
    'John': ['John', 'he/him', 25, 'USA', 'Student', 'Math', 'Mentor'],
    'Alice': ['Alice', 'she/her', 30, 'Canada', 'Professor', 'History', 'Mentee'],
    'Bob': ['Bob', 'they/them', 22, 'UK', 'Freelancer', 'Math', 'Friend'],
    'Emma': ['Emma', 'she/her', 28, 'Australia', 'Working Professional', 'Biology', 'Internship'],
    'Michael': ['Michael', 'he/him', 35, 'USA', 'Professor', 'Math', 'Mentor'],
    'Sophia': ['Sophia', 'she/her', 29, 'Canada', 'Student', 'Math', 'Mentee'],
    'Daniel': ['Daniel', 'he/him', 27, 'UK', 'Working Professional', 'History', 'Friend'],
    'Emily': ['Emily', 'she/her', 26, 'Australia', 'Freelancer', 'Math', 'Project'],
    'William': ['William', 'he/him', 31, 'USA', 'Professor', 'Biology', 'Internship'],
    'Olivia': ['Olivia', 'she/her', 24, 'Canada', 'Student', 'Math', 'Mentor'],
    'James': ['James', 'he/him', 23, 'UK', 'Working Professional', 'History', 'Mentee'],
    'Ava': ['Ava', 'she/her', 27, 'Australia', 'Freelancer', 'Math', 'Friend'],
    'Alexander': ['Alexander', 'he/him', 33, 'USA', 'Professor', 'Biology', 'Internship'],
    'Isabella': ['Isabella', 'she/her', 28, 'Canada', 'Student', 'Math', 'Project'],
    'Ethan': ['Ethan', 'he/him', 29, 'UK', 'Working Professional', 'History', 'Mentor'],
    'Mia': ['Mia', 'she/her', 30, 'Australia', 'Freelancer', 'Math', 'Mentee'],
    # Add more users as needed
}

def display_users_with_same_interest(subject):
    matching_users = {user: details for user, details in user_dict.items() if details[5] == subject}
    return matching_users

def get_subject_of_interest():
    subject = subject_entry.get().strip()
    matching_users = display_users_with_same_interest(subject)
    result_text.set("\n".join([f"{user}: {details}" for user, details in matching_users.items()]))

# Create the main window
root = tk.Tk()
root.geometry("500x500")
root.title("User Search")

# Create and place the widgets
subject_label = tk.Label(root, text="Enter Subject of Interest:")
subject_label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

search_button = tk.Button(root, text="Search", command=get_subject_of_interest)
search_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
