import tkinter as tk
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

# Declare profiles_list as a global variable
profiles_list = None

# Function to display users with the same interest
def display_users_with_same_interest(subject):
    matching_users = {user: details for user, details in user_details.items() if details.get("interests") == subject}
    return matching_users

# Function to get the subject of interest
def get_subject_of_interest():
    subject = subject_entry.get().strip()
    matching_users = display_users_with_same_interest(subject)
    if matching_users:
        display_profiles(matching_users)
    else:
        result_text.set("No profiles found for the given subject of interest.")

# Function to display profiles
def display_profiles(profiles):
    global profiles_list
    global current_profile_index
    current_profile_index = -1
    profiles_list = list(profiles.items())
    display_next_profile()

# Function to display the next profile
def display_next_profile():
    global current_profile_index
    current_profile_index += 1
    if current_profile_index < len(profiles_list):
        user, details = profiles_list[current_profile_index]
        formatted_profile = (
            f"Name: {details['name']}\n"
            f"Pronouns: {details['pronouns']}\n"
            f"Country: {details['country']}\n"
            f"Interests: {details['interests']}\n"
            f"Looking for: {details['looking_for']}"
        )
        result_text.set(formatted_profile)
    else:
        result_text.set("No more profiles to display.")

# Function to accept a profile
def accept_profile():
    global profiles_list
    if current_profile_index >= 0:
        user, details = profiles_list[current_profile_index]
        save_accepted_profile(user)
    display_next_profile()

# Function to save the accepted profile
def save_accepted_profile(user):
    with open("accepted_profiles.json", "a") as accepted_profiles_file:
        json.dump({user: user_details[user]}, accepted_profiles_file, indent=4)
        accepted_profiles_file.write("\n")

# Function to deny a profile
def deny_profile():
    display_next_profile()

# Create the main window
root = tk.Tk()
root.geometry("500x500")
root.title("STUMBLE 'Find Your Academic Match!'")
root.configure(bg="#ADD8E6")  # Light blue background

# Create and place the widgets
title_label = tk.Label(root, text="STUMBLE 'Find Your Academic Match!'", font=("Arial", 16, "bold"), fg="navy", bg="#ADD8E6")
title_label.pack(pady=(10, 0))

subject_label = tk.Label(root, text="Enter Subject of Interest:", font=("Arial", 14), bg="#ADD8E6", fg="white")
subject_label.pack(pady=(10, 0))

subject_entry = tk.Entry(root)
subject_entry.pack(pady=(0, 10))

search_button = tk.Button(root, text="Search", command=get_subject_of_interest, font=("Arial", 12))
search_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14), bg="#ADD8E6", fg="navy", justify="center")
result_label.pack(pady=(20, 10))

accept_button = tk.Button(root, text="Accept", command=accept_profile, bg="green", fg="black", font=("Arial", 12))
accept_button.place(relx=0.75, rely=0.9, anchor=tk.CENTER)

deny_button = tk.Button(root, text="Deny", command=deny_profile, bg="red", fg="black", font=("Arial", 12))
deny_button.place(relx=0.25, rely=0.9, anchor=tk.CENTER)

# Initialize current_profile_index
current_profile_index = -1

# Start the Tkinter event loop
root.mainloop()




