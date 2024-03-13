import tkinter as tk #working
from tkinter import messagebox
import json

# Load existing user details and login credentials from JSON files
try:
    with open("user_details.json", "r") as user_details_file:
        user_details = json.load(user_details_file)
except FileNotFoundError:
    user_details = {}

try:
    with open("login_credentials.json", "r") as login_credentials_file:
        login_credentials = json.load(login_credentials_file)
except FileNotFoundError:
    login_credentials = {}

def validate_length(userid, password):
    return len(userid) == len(password) == 8

def signup():
    signup_window = tk.Toplevel(parent)
    signup_window.title("Sign Up")
    signup_window.geometry("500x500")
    signup_window.configure(bg="white")

    # Add logo to the signup page
    logo_label = tk.Label(signup_window, image=resized_logo, bg="white")
    logo_label.pack()

    # Create and place the labels and entries for user details
    details_labels = ["User ID:", "Password:", "Name:", "Pronouns:", "Country:", "Interests:", "Looking for:"]
    entry_list = []

    for label_text in details_labels:
        label = tk.Label(signup_window, text=label_text, bg="white", fg="black", font=("Times New Roman", 12))
        label.pack()

        entry = tk.Entry(signup_window, font=("Times New Roman", 12))
        entry.pack()
        entry_list.append(entry)

    # Create and place the done button
    done_button = tk.Button(signup_window, text="Done", command=lambda: save_signup(entry_list), bg="#2962FF", fg="white", font=("Arial", 12))
    done_button.pack()

def save_signup(entries):
    user_id, password, name, pronouns, country, interests, looking_for = [entry.get() for entry in entries]

    if validate_length(user_id, password):
        user_details[user_id] = {
            "name": name,
            "pronouns": pronouns,
            "country": country,
            "interests": interests,
            "looking_for": looking_for
        }
        login_credentials[user_id] = password

        # Save user details and login credentials to JSON files
        with open("user_details.json", "w") as user_details_file:
            json.dump(user_details, user_details_file, indent=4)

        with open("login_credentials.json", "w") as login_credentials_file:
            json.dump(login_credentials, login_credentials_file, indent=4)

        messagebox.showinfo("Sign Up Successful", "Welcome to Stumble!")

        show_welcome_page(name)
    else:
        messagebox.showerror("Sign Up Failed", "User ID and password must be 8 characters long")

def login():
    login_window = tk.Toplevel(parent)
    login_window.title("Log In")
    login_window.geometry("500x500")
    login_window.configure(bg="white")

    # Add logo to the login page
    logo_label = tk.Label(login_window, image=resized_logo, bg="white")
    logo_label.pack()

    # Create and place the username label and entry
    username_label = tk.Label(login_window, text="User ID:", bg="white", fg="black", font=("Times New Roman", 12))
    username_label.pack()

    username_entry_login = tk.Entry(login_window, font=("Times New Roman", 12))
    username_entry_login.pack()

    # Create and place the password label and entry
    password_label = tk.Label(login_window, text="Password:", bg="white", fg="black", font=("Times New Roman", 12))
    password_label.pack()

    password_entry_login = tk.Entry(login_window, show="*", font=("Times New Roman", 12))
    password_entry_login.pack()

    # Create and place the login button
    login_button = tk.Button(login_window, text="Login", command=lambda: validate_login(username_entry_login.get(), password_entry_login.get()), bg="#ffc629", fg="white", font=("Arial", 12))
    login_button.pack()

def validate_login(userid, password):
    if userid in login_credentials and login_credentials[userid] == password:
        show_welcome_page(user_details[userid]["name"])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def show_welcome_page(name):
    welcome_window = tk.Toplevel(parent)
    welcome_window.title("Welcome to Stumble")
    welcome_window.geometry("500x500")
    welcome_window.configure(bg="white")

    # Add logo to the welcome page
    logo_label = tk.Label(welcome_window, image=resized_logo, bg="white")
    logo_label.pack()

    # Display welcome message
    welcome_label = tk.Label(welcome_window, text=f"Welcome back, {name}!", bg="white", fg="black", font=("Times New Roman", 16))
    welcome_label.pack()

# Create the main window with 500x500 geometry
parent = tk.Tk()
parent.title("Login Form")
parent.geometry("500x500")
parent.configure(bg="white")

# Add a logo on top
logo_image = tk.PhotoImage(file="C:/Users/riddhi/Downloads/S T U M B L E.png")
original_width = logo_image.width()
original_height = logo_image.height()
desired_width = 200
desired_height = 200
width_scale = desired_width / original_width
height_scale = desired_height / original_height
resized_logo = logo_image.subsample(int(1/width_scale), int(1/height_scale))

logo_label = tk.Label(parent, image=resized_logo, bg="white")
logo_label.pack()

# Create and place the signup and login buttons on the first page
signup_button = tk.Button(parent, text="Sign Up", command=signup, bg="#2962FF", fg="white", font=("Arial", 12))
signup_button.pack()

login_button = tk.Button(parent, text="Log In", command=login, bg="#ffc629", fg="white", font=("Arial", 12))
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()
