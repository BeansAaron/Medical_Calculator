import tkinter as tk
from tkinter import Entry, Button, messagebox
from Back_end.database import save_account

def load_create_account_ui(root, canvas, on_return_click):
    canvas.delete("all")

    # --- Header ---
    canvas.create_rectangle(0.0, 0.0, 772.0, 67.0, fill="#5F1C1C", outline="")
    canvas.create_text(25.0, 33.0, anchor="w", text="Create Account", fill="#FFFFFF", font=("Arial", 30 * -1))

    # --- Username Section ---
    canvas.create_text(29.0, 85.0, anchor="nw", text="Username:", font=("Arial", 20 * -1))
    entry_user = Entry(root, bd=0, bg="#D9D9D9", font=("Arial", 14))
    entry_user.place(x=40.0, y=110.0, width=692.0, height=35.0)

    # --- Password Section ---
    canvas.create_text(29.0, 160.0, anchor="nw", text="Password:", font=("Arial", 20 * -1))
    entry_pass = Entry(root, bd=0, bg="#D9D9D9", show="*", font=("Arial", 14))
    entry_pass.place(x=40.0, y=185.0, width=692.0, height=35.0)

    # --- Confirm Password Section ---
    canvas.create_text(29.0, 235.0, anchor="nw", text="Confirm Password:", font=("Arial", 20 * -1))
    entry_confirm = Entry(root, bd=0, bg="#D9D9D9", show="*", font=("Arial", 14))
    entry_confirm.place(x=40.0, y=260.0, width=692.0, height=35.0)

    # --- Create Account Logic ---
    def handle_create():
        user = entry_user.get()
        pw = entry_pass.get()
        cpw = entry_confirm.get()
        
        if not user or not pw:
            messagebox.showwarning("Warning", "Fields cannot be empty!")
            return

        if pw != cpw:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        success, message = save_account(user, pw)
        
        if success:
            messagebox.showinfo("Success", message)
            on_return_click() # Go back to Login screen
        else:
            messagebox.showerror("Error", message)

    # --- Buttons ---
    Button(root, text="Return", font=("Arial", 14), bg="#D9D9D9", command=on_return_click).place(x=40.0, y=320.0, width=200.0, height=40.0)
    
    Button(root, text="Create Account", font=("Arial", 14), bg="#D9D9D9", command=handle_create).place(x=532.0, y=320.0, width=200.0, height=40.0)