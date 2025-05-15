import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')  # 24-hour format
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1 second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Customize the label
label = tk.Label(root, font=('Arial', 50), bg='black', fg='lime')
label.pack(padx=20, pady=20)

# Start the clock
update_time()

# Run the window loop
root.mainloop()
