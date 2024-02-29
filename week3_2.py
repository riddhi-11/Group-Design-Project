import tkinter as tk
from tkinter import messagebox

# Mock data for user profiles (you can replace this with your storage mechanism)
user_profiles = {}

# Function that checks entered username & pswd against stored to accept/deny
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

# Create an interface for profile setup
def setup_profile_gui(username):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("Profile Setup")

    def submit_profile():
        user_profiles[username]['name'] = name_entry.get()
        user_profiles[username]['pronouns'] = pronouns_entry.get()
        user_profiles[username]['age'] = age_entry.get()
        user_profiles[username]['country'] = country_entry.get()
        user_profiles[username]['title'] = title_entry.get()
        user_profiles[username]['interest'] = interest_entry.get()
        user_profiles[username]['lookingfor'] = looking_for_entry.get()

        window.destroy()  # Close the window after submitting
        blank_page(username)

    # Tkinter labels and entry widgets for each question
    tk.Label(window, text="Name:").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text="Pronouns:").pack()
    pronouns_entry = tk.Entry(window)
    pronouns_entry.pack()

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

# Function to create a blank page (contents can be extended)
def blank_page(username):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("Blank Page")
    tk.Label(window, text=f"Welcome, {username}! This is your blank page.").pack()

# Create the main login/signup page
def login_signup_page():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Login / Sign up")

    def on_submit():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if login(entered_username, entered_password):
            messagebox.showinfo("Success", "Login successful!")
            blank_page(entered_username)
        else:
            messagebox.showerror("Error", "Invalid username or password.")
            signup_choice()

    def signup_choice():
        response = messagebox.askyesno("Sign Up", "User not found. Do you want to sign up?")
        if response:
            signup_page()

    def signup_page():
        signup_window = tk.Toplevel(root)
        signup_window.geometry("500x500")
        signup_window.title("Sign Up")

        def on_signup():
            new_username = new_username_entry.get()
            new_password = new_password_entry.get()

            if signup(new_username, new_password):
                messagebox.showinfo("Success", "Sign up successful!")
                setup_profile_gui(new_username)
            else:
                messagebox.showerror("Error", "Username already exists. Choose a different username.")

        tk.Label(signup_window, text="New Username:").pack()
        new_username_entry = tk.Entry(signup_window)
        new_username_entry.pack()

        tk.Label(signup_window, text="New Password:").pack()
        new_password_entry = tk.Entry(signup_window, show="*")
        new_password_entry.pack()

        signup_button = tk.Button(signup_window, text="Sign Up", command=on_signup)
        signup_button.pack()

    # Tkinter labels and entry widgets for username and password
    tk.Label(root, text="Username:").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Tkinter button to submit login details
    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack()

    # Start the Tkinter event loop
    root.mainloop()

# Run the login/signup page
login_signup_page()

#TO DO:
#Figure out how to give options for the profile setup window. 

