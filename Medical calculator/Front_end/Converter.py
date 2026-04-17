import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
from pathlib import Path

if getattr(sys, 'frozen', False):
    # This is where PyInstaller puts your assets in the EXE
    BASE_PATH = Path(sys._MEIPASS)
else:
    BASE_PATH = Path(__file__).parent

ASSETS_PATH = BASE_PATH / "assets"

def load_conversion_ui(root, canvas, on_return):
    """
    root: The main Tk window
    canvas: The shared canvas
    on_return: Function to go back to the Selection Menu
    """
    # 1. Clear previous drawings
    canvas.delete("all")

    # --- Calculation Logic ---
    def calculate_conversion():
        try:
            val_str = entry_input.get()
            if not val_str:
                messagebox.showwarning("Input Error", "Please enter a value.")
                return

            val = float(val_str)
            choice = conversion_var.get()
            result_text = ""
            
            # Logic for conversion
            if choice == "kg to lbs":
                result_text = f"{round(val * 2.2, 2)} lbs"
            elif choice == "lbs to kg":
                result_text = f"{round(val / 2.2, 2)} kg"
            elif choice == "mg to g":
                result_text = f"{val / 1000} g"
                
            label_result.config(text=result_text, fg="black")
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    # --- Header ---
    canvas.create_rectangle(0.0, 0.0, 450.0, 60.0, fill="#5F1C1C", outline="")
    canvas.create_text(
        20.0, 30.0, 
        anchor="w", 
        text="Conversions", 
        fill="#FFFFFF", 
        font=("Arial", 24 * -1)
    )

    # --- Input Section ---
    # Dropdown for Conversion Type
    canvas.create_text(25.0, 100.0, anchor="nw", text="Select Conversion:", font=("Arial", 16 * -1))
    options = ["kg to lbs", "lbs to kg", "mg to g"]
    conversion_var = tk.StringVar(root)
    conversion_var.set(options[0])

    dropdown = ttk.OptionMenu(root, conversion_var, options[0], *options)
    dropdown.place(x=25.0, y=130.0, width=200.0, height=35.0)

    # Value Input
    canvas.create_text(25.0, 200.0, anchor="nw", text="Enter Value:", font=("Arial", 16 * -1))
    entry_input = tk.Entry(root, bd=0, bg="#D9D9D9", font=("Arial", 14))
    entry_input.place(x=25.0, y=230.0, width=200.0, height=35.0)

    # --- Calculate Button ---
    btn_calc = tk.Button(
        root,
        text="Calculate", 
        bg="#5F1C1C", 
        fg="white", 
        font=("Arial", 12, "bold"), 
        command=calculate_conversion,
        borderwidth=0
    )
    btn_calc.place(x=260.0, y=180.0, width=130.0, height=45.0)

    # --- Divider Line ---
    canvas.create_rectangle(0.0, 320.0, 450.0, 328.0, fill="#5F1C1C", outline="")

    # --- Results Section ---
    canvas.create_text(25.0, 360.0, anchor="nw", text="Result:", font=("Arial", 20 * -1))
    canvas.create_text(225.0, 420.0, anchor="center", text="Converted Value:", font=("Arial", 18 * -1))
    
    label_result = tk.Label(root, text="---", bg="#D9D9D9", font=("Arial", 14), anchor="center")
    label_result.place(x=95.0, y=450.0, width=260.0, height=50.0)

    # --- Return Button ---
    btn_return = tk.Button(
        root,
        text="Return", 
        bg="#5F1C1C", 
        fg="white", 
        font=("Arial", 14), 
        command=on_return,
        borderwidth=0
    )
    btn_return.place(x=25.0, y=580.0, width=140.0, height=40.0)