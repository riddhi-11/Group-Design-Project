import tkinter as tk

profiles = []

def submit():
    name = name_entry.get()
    age = age_entry.get()
    subjects = subjects_entry.get("1.0", tk.END).strip()  # Remove leading/trailing whitespace
    looking_for = looking_for_entry.get("1.0", tk.END).strip()  # Remove leading/trailing whitespace
    
    current_profile = {
        "Name": name,
        "Age": age,
        "Subjects chosen": subjects,
        "Looking for": looking_for
    }
    
    profiles.append(current_profile)
    
    print("Enter 'right' to add the profile, 'left' to remove, or 'done' to finish:")
    right_left_done = input().strip()
    
    if right_left_done == "done":
        print("All profiles:")
        for p in profiles:
            print(p)
        root.destroy()
    else:
        # Clear entry fields for next profile input
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        subjects_entry.delete("1.0", tk.END)
        looking_for_entry.delete("1.0", tk.END)

root = tk.Tk()
root.title("Photo Insert Form")

# Create a frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create rectangular box
canvas = tk.Canvas(frame, width=300, height=300)
canvas.pack()

# Create a square within the rectangular box
canvas.create_rectangle(50, 50, 250, 250, outline="black", width=2)
canvas.create_text(150, 150, text="Insert Photo", font=("Arial", 12))

# Create labels and entry fields
labels = ["Name:", "Age:", "Subjects chosen:", "Looking for:"]

for label_text in labels:
    label = tk.Label(frame, text=label_text)
    label.pack()
    
    if label_text == "Subjects chosen:" or label_text == "Looking for:":
        entry = tk.Text(frame, height=4, width=30)
    else:
        entry = tk.Entry(frame, width=30)
        
    entry.pack()

    if label_text == "Name:":
        name_entry = entry
    elif label_text == "Age:":
        age_entry = entry
    elif label_text == "Subjects chosen:":
        subjects_entry = entry
    elif label_text == "Looking for:":
        looking_for_entry = entry

# Create submit button
submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.pack(pady=10)

root.mainloop()

