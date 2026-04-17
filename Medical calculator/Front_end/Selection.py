from pathlib import Path
from tkinter import Button

# --- Assets Setup ---
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vince\OneDrive\Desktop\Medical calculator\mga ui\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def load_selection_menu(root, canvas, on_navigate, on_logout):
    """
    root: The main Tk window
    canvas: The shared canvas
    on_navigate: Function to open calculators (takes the name as an argument)
    on_logout: Function to go back to Sign In
    """
    # 1. Clear previous screen
    canvas.delete("all")

    # --- Header Section ---
    canvas.create_rectangle(0.0, 0.0, 450.0, 80.0, fill="#5F1C1C", outline="")
    canvas.create_text(
        20.0, 40.0,
        anchor="w",
        text="Medical Calculator",
        fill="#FFFFFF",
        font=("Arial", 28 * -1)
    )

    # --- Sidebars ---
    canvas.create_rectangle(0.0, 120.0, 40.0, 650.0, fill="#5F1C1C", outline="", width=0)
    canvas.create_rectangle(410.0, 120.0, 450.0, 650.0, fill="#5F1C1C", outline="", width=0)

    # --- Selection Label ---
    canvas.create_text(
        225.0, 140.0,
        anchor="center",
        text="Selection:",
        fill="#000000",
        font=("Arial", 22 * -1)
    )

    # --- Menu Buttons ---
    button_options = [
        "IV Flow Rate",
        "Titration",
        "Drug Dose",
        "Infusion Time",
        "Conversion"
    ]

    y_pos = 200
    for option in button_options:
        # We use 'on_navigate' to tell main.py which screen was picked
        btn = Button(
            text=option,
            font=("Arial", 16),
            bg="#C89696",
            fg="black",
            activebackground="#A37272",
            borderwidth=2,
            relief="solid",
            command=lambda o=option: on_navigate(o) 
        )
        btn.place(x=100.0, y=y_pos, width=250.0, height=50.0)
        y_pos += 80

    # --- Bottom Buttons ---
    # Return Button (acting as Logout/Back to Sign In)
    btn_return = Button(
        text="Logout",
        font=("Arial", 14),
        bg="#C89696",
        borderwidth=0,
        command=on_logout
    )
    btn_return.place(x=55.0, y=630.0, width=120.0, height=40.0)

    # History Button
    btn_history = Button(
        text="History",
        font=("Arial", 14),
        bg="#C89696",
        borderwidth=0,
        command=lambda: print("History clicked")
    )
    btn_history.place(x=275.0, y=630.0, width=120.0, height=40.0)