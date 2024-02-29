import tkinter as tk
from tkinter import messagebox

# Mock data for user profiles (you can replace this with your storage mechanism)
user_profiles = {'reba88': {'password': '678'}, 'riddhi78': {'password': '896'}}

#Function that checks entered username & pswd against stored to accept/deny 
def login(username, password):
    # Check if the username exists and if the password matches
    if username in user_profiles and user_profiles[username]['password'] == password:
        return True
    else:
        return False

def signup(username, password):
    # Check if the username already exists
    if username in user_profiles:
        return False
    else:
        user_profiles[username] = {'password': password}
        return True

#Create an interface for this as well.
#Add other questions. 

def setup_profile(username):
    # Create a Tkinter window
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Profile Setup")

    # Function to handle profile setup
    def submit_profile():
        user_profiles[username]['name'] = input("Enter your name: ")
        user_profiles[username]['pronouns'] = input("Enter your pronouns: ")
        user_profiles[username]['age'] = input("Enter your age: ")
        user_profiles[username]['country'] = input("Enter Country: ")
        user_profiles[username]['title'] = input("Enter Current title (Student/Professor/Working professional/Freelancer/Other): ")
        user_profiles[username]['interest'] = input("Enter Area of interest (Math/History/Biology): ")
        user_profiles[username]['lookingfor'] = input("Enter Looking for (Mentor/Mentee/Internship/Friend/Project): ")
        #Figure out how to give options for the above 3 cases 
        window.destroy()  # Close the window after submitting

    # Tkinter labels and entry widgets for each question
    tk.Label(window, text="Name:").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()
    
    tk.Label(window, text="Pronouns:").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="Age:").pack()
    age_entry = tk.Entry(window)
    age_entry.pack()

    tk.Label(window, text="Country:").pack()
    country_entry = tk.Entry(window)
    country_entry.pack()

    tk.Label(window, text="Current Title:").pack()
    title_entry = tk.Entry(window)
    title_entry.pack()

    tk.Label(window, text="Area of Interest:").pack()
    interest_entry = tk.Entry(window)
    interest_entry.pack()

    tk.Label(window, text="Looking For:").pack()
    looking_for_entry = tk.Entry(window)
    looking_for_entry.pack()

    # Button to submit the profile
    submit_button = tk.Button(window, text="Submit", command=submit_profile)
    submit_button.pack()

    # Run the Tkinter event loop
    window.mainloop()

def login_signup_page():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Login / Sign up")

    def on_submit():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if login(entered_username, entered_password):
            messagebox.showinfo("Success", "Login successful!")
            # Check if the user has already set up their profile
            if 'name' not in user_profiles[entered_username]:
                setup_profile(entered_username)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    # Create and pack widgets
    username_label = tk.Label(root, text="Username:")
    username_label.pack()

    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack()

    root.mainloop()

login_signup_page()


#Figure out how to go from sign in/log in to questionnaire
