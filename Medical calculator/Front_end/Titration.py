import tkinter as tk
from tkinter import ttk
import math

def load_titration_ui(root, canvas, on_return):
    """
    root: The main Tk window from main.py
    canvas: The shared canvas
    on_return: Function to go back to the Selection Menu
    """
    canvas.delete("all")

    # --- Calculation Logic ---
    def calculate_titration():
        try:
            dose = float(entry_dose.get())
            weight = float(entry_weight.get())
            selection = titration_var.get().lower()
     
            result = 0.0

            if selection == "dopamine":
                # Formula: (Dose * Weight) / 13.3
                result = math.ceil((dose * weight) / 13.3)
            elif selection == "dobutamine":
                # Formula: (Dose * Weight) / 16.6
                result = math.ceil((dose * weight) / 16.6)
                
            result_label.config(text=f"{result} gtts/min", fg="black")
            
        except ValueError:
            result_label.config(text="Invalid Input", fg="red")

    # --- Header ---
    canvas.create_rectangle(0.0, 0.0, 450.0, 60.0, fill="#5F1C1C", outline="")
    canvas.create_text(
        20.0, 30.0, 
        anchor="w", 
        text="Titration", 
        fill="#FFFFFF", 
        font=("Arial", 24 * -1)
    )

    # --- Input Section ---
    canvas.create_text(50.0, 100.0, anchor="nw", text="Type of titration:", font=("Arial", 16 * -1))
    
    titration_options = ["Dopamine", "Dobutamine"]
    titration_var = tk.StringVar(root)
    titration_var.set(titration_options[0])

    dropdown = ttk.OptionMenu(root, titration_var, titration_options[0], *titration_options)
    dropdown.place(x=220.0, y=95.0, width=180.0, height=35.0)

    # Dose Input
    canvas.create_text(50.0, 160.0, anchor="nw", text="Dose:", font=("Arial", 16 * -1))
    entry_dose = tk.Entry(root, bd=0, bg="#D9D9D9", font=("Arial", 14))
    entry_dose.place(x=220.0, y=155.0, width=180.0, height=35.0)

    # Weight Input
    canvas.create_text(50.0, 220.0, anchor="nw", text="Weight (kg):", font=("Arial", 16 * -1))
    entry_weight = tk.Entry(root, bd=0, bg="#D9D9D9", font=("Arial", 14))
    entry_weight.place(x=220.0, y=215.0, width=180.0, height=35.0)

    # --- Divider ---
    canvas.create_rectangle(0.0, 340.0, 450.0, 335.0, fill="#5F1C1C", outline="")

    # --- Result Section ---
    canvas.create_text(25.0, 360.0, anchor="nw", text="Result:", font=("Arial", 20 * -1))
    canvas.create_text(
        225.0, 
        420.0, 
        anchor="center", 
        text="Infusion Rate:", 
        font=("Arial", 18 * -1)
    )

    result_label = tk.Label(root, text="0.00", bg="#D9D9D9", font=("Arial", 14, "bold"))
    result_label.place(x=95.0, y=450.0, width=260.0, height=50.0)

    # --- Buttons ---
    btn_calc = tk.Button(
        root,
        text="Calculate", 
        bg="#5F1C1C", 
        fg="white", 
        font=("Arial", 12, "bold"), 
        command=calculate_titration
    )
    btn_calc.place(x=175.0, y=285.0, width=100.0, height=30.0)

    btn_return = tk.Button(
        root,
        text="Return", 
        bg="#5F1C1C", 
        fg="white", 
        font=("Arial", 14), 
        command=on_return # This calls self.show_menu in main.py
    )
    btn_return.place(x=25.0, y=580.0, width=140.0, height=40.0)