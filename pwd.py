import tkinter as tk
import re

def check_password_strength(*args):
    password = entry.get()
    strength, feedback = assess_strength(password)
    feedback_label.config(text="\n".join(feedback), fg="white")

    if strength == "Very Strong":
        entry.config(fg="lime")
        strength_label.config(text="Very Strong", fg="lime")
    elif strength == "Strong":
        entry.config(fg="cyan")
        strength_label.config(text="Strong", fg="cyan")
    elif strength == "Medium":
        entry.config(fg="yellow")
        strength_label.config(text="Medium", fg="yellow")
    elif strength == "Weak":
        entry.config(fg="orange")
        strength_label.config(text="Weak", fg="orange")
    else:
        entry.config(fg="red")
        strength_label.config(text="Very Weak", fg="red")

def assess_strength(password):
    strength_score = 0
    feedback = []
    
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    if strength_score == 5:
        return "Very Strong", feedback
    elif strength_score == 4:
        return "Strong", feedback
    elif strength_score == 3:
        return "Medium", feedback
    elif strength_score == 2:
        return "Weak", feedback
    else:
        return "Very Weak", feedback

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Set the window size and dark background
root.geometry("400x300")
root.configure(bg="#1c1c1c")

# Create a label and entry for password input
tk.Label(root, text="Enter Password:", font=("Helvetica", 12), fg="cyan", bg="#1c1c1c").pack(pady=10)
entry = tk.Entry(root, show='*', font=("Helvetica", 12), width=25, bg="#333333", fg="white", insertbackground="white")
entry.pack(pady=10)

# Trace the input to check password strength as the user types
entry_var = tk.StringVar()
entry.config(textvariable=entry_var)
entry_var.trace_add("write", check_password_strength)

# Create a button to check password strength
tk.Button(root, text="Check Strength", font=("Helvetica", 12), bg="cyan", fg="black", command=check_password_strength).pack(pady=10)

# Label to display the strength result
strength_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#1c1c1c")
strength_label.pack(pady=10)

# Label to display feedback messages
feedback_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#1c1c1c", wraplength=350, justify="left")
feedback_label.pack(pady=10)

# Run the application
root.mainloop()
