import tkinter as tk
from tkinter import messagebox
import datetime

def get_updates():
    updates = text_box.get(1.0, tk.END) # Get the text from the text box
    now = datetime.datetime.now()
    update_str = "{}-{} : {}".format(now.hour, (now.hour + 1) % 24, updates) # Format the update string with current hour and next hour
    with open('updates.txt', 'a') as file: # Append the update string to a file
        file.write(update_str + "\n")
    messagebox.showinfo("Updates", "Updates received:\n{}".format(updates)) # Show a message box with the updates

root = tk.Tk()
root.title("Update Tracker")

# Create a text box
text_box = tk.Text(root, height=10, width=40)
text_box.pack(pady=10)

# Create a button to submit updates
submit_button = tk.Button(root, text="Submit Updates", command=get_updates)
submit_button.pack()

# Create a label for day of the week
day_label = tk.Label(root, text="-----------{}---------".format(datetime.datetime.now().strftime('%A')))
day_label.pack()

root.mainloop()
