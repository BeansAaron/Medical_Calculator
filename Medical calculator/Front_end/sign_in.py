from pathlib import Path
from tkinter import Entry, Button, PhotoImage, messagebox
from Back_end.database import check_login

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def load_sign_in_ui(root, canvas, on_create_click, on_signin_click):
    canvas.delete("all")
    global entry_image_1, entry_image_2, button_image_1, button_image_2

    # --- Header ---
    canvas.create_rectangle(0.0, 0.0, 772.0, 67.0, fill="#5F1C1C", outline="")
    canvas.create_text(40.0, 33.0, anchor="w", text="Medical calculator", fill="#FFFFFF", font=("Arial", 30 * -1))

    # --- Username ---
    canvas.create_text(29.0, 97.0, anchor="nw", text="Username:", font=("Arial", 25 * -1))
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(387.0, 158.0, image=entry_image_1)
    
    entry_user = Entry(bd=0, bg="#D9D9D9", font=("Arial", 16))
    entry_user.place(x=43.0, y=136.0, width=688.0, height=42.0)

    # --- Password ---
    canvas.create_text(29.0, 195.0, anchor="nw", text="Password:", font=("Arial", 25 * -1))
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(386.0, 256.0, image=entry_image_2)
    
    entry_pass = Entry(bd=0, bg="#D9D9D9", show="*", font=("Arial", 16))
    entry_pass.place(x=42.0, y=234.0, width=688.0, height=42.0)

    # --- Login Logic ---
    def handle_login():
        username = entry_user.get()
        password = entry_pass.get()
        
        if check_login(username, password):
            on_signin_click() # Moves to Menu
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    # --- Buttons ---
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, command=handle_login, relief="flat")
    button_1.place(x=590.0, y=318.0, width=141.0, height=42.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, command=on_create_click, relief="flat")
    button_2.place(x=42.0, y=325.0, width=229.0, height=35.0)