from pathlib import Path
from tkinter import Button

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_PATH = BASE_DIR / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def load_selection_menu(root, canvas, on_navigate, on_logout):
    canvas.delete("all")

    # --- 1. Background Base ---
    canvas.configure(bg="#BABABA") 

    # --- 2. Header Section ---
    canvas.create_rectangle(0.0, 0.0, 450.0, 90.0, fill="#5F1C1C", outline="")
    canvas.create_text(
        225.0, 45.0,
        anchor="center",
        text="MEDICAL CALCULATOR",
        fill="#FFFFFF",
        font=("Helvetica", 20, "bold")
    )

    # --- 3. THE "CARD" CONTAINER ---
    # This subtle rectangle groups the buttons so they don't look like they are floating
    canvas.create_rectangle(35.0, 115.0, 415.0, 600.0, fill="#CFCFCF", outline="#A0A0A0", width=1)
    
    # Selection Label - Moved slightly up and made smaller/cleaner
    canvas.create_text(
        225.0, 145.0,
        anchor="center",
        text="SELECT CALCULATION MODULE",
        fill="#444444",
        font=("Helvetica", 10, "bold")
    )

    # --- 4. Main Calculator Buttons ---
    button_options = [
        "IV Flow Rate",
        "Titration",
        "Drug Dose",
        "Infusion Time",
        "Conversion"
    ]

    y_pos = 180
    for option in button_options:
        # Drawing a small decorative red line next to each button to fill space
        canvas.create_rectangle(65.0, y_pos + 10, 70.0, y_pos + 40, fill="#5F1C1C", outline="")
        
        btn = Button(
            root,
            text=f"  {option}", # Added spaces to offset text from the red line
            anchor="w",         # Align text to the left for a professional menu look
            font=("Helvetica", 13, "bold"),
            bg="#C89696",
            fg="black",
            activebackground="#A37272",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            cursor="hand2",
            command=lambda o=option: on_navigate(o) 
        )
        btn.place(x=75.0, y=y_pos, width=300.0, height=50.0)
        y_pos += 75

    # --- 5. Footer Information ---
    # Fills the gap at the bottom of the card
    canvas.create_text(
        225.0, 580.0,
        text="v1.0 Standard Edition | Clinical Tools",
        fill="#777777",
        font=("Helvetica", 8, "italic")
    )

    # --- 6. Bottom Action Buttons ---
    
    # Logout Button
    btn_logout = Button(
        root,
        text="Logout",
        font=("Helvetica", 12, "bold"),
        bg="#5F1C1C",
        fg="white",
        activebackground="#4A1616",
        activeforeground="white",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2",
        command=on_logout
    )
    btn_logout.place(x=55.0, y=630.0, width=120.0, height=40.0)

    # History Button
    btn_history = Button(
        root,
        text="History",
        font=("Helvetica", 12, "bold"),
        bg="#5F1C1C",
        fg="white",
        activebackground="#4A1616",
        activeforeground="white",
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2",
        command=lambda: on_navigate("History") 
    )
    btn_history.place(x=275.0, y=630.0, width=120.0, height=40.0)