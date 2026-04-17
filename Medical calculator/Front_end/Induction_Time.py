import tkinter as tk
from tkinter import messagebox

def load_infusion_time_ui(root, canvas, on_return):
    """
    root: The main Tk window
    canvas: The shared canvas
    on_return: Function to go back to the Selection Menu
    """
    # 1. Clear the canvas
    canvas.delete("all")

    # --- Calculation Logic ---
    def calculate_time():
        try:
            volume_str = entry_volume.get()
            rate_str = entry_rate.get()
            
            if not volume_str or not rate_str:
                messagebox.showwarning("Input Error", "Please fill in all fields.")
                return

            volume = float(volume_str)
            rate = float(rate_str)
            
            if rate == 0:
                messagebox.showerror("Error", "Rate cannot be zero!")
                return
            
            # Formula: Time = Volume / Rate
            time_result = volume / rate
            
            # Update result label
            label_result.config(text=f"{time_result:.2f} hours", fg="black")
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")

    # --- Header ---
    canvas.create_rectangle(0.0, 0.0, 450.0, 60.0, fill="#5F1C1C", outline="")
    canvas.create_text(
        20.0, 30.0, 
        anchor="w", 
        text="Infusion Time", 
        fill="#FFFFFF", 
        font=("Arial", 24 * -1)
    )

    # --- Input Section ---
    canvas.create_text(25.0, 100.0, anchor="nw", text="Volume (mL):", font=("Arial", 18 * -1))
    entry_volume = tk.Entry(root, bd=0, bg="#D9D9D9", justify="left", font=("Arial", 14))
    entry_volume.place(x=25.0, y=130.0, width=200.0, height=35.0)

    canvas.create_text(25.0, 200.0, anchor="nw", text="Rate (mL/hr):", font=("Arial", 18 * -1))
    entry_rate = tk.Entry(root, bd=0, bg="#D9D9D9", justify="left", font=("Arial", 14))
    entry_rate.place(x=25.0, y=230.0, width=200.0, height=35.0)

    # --- Calculate Button ---
    btn_calc = tk.Button(
        root,
        text="Calculate", 
        bg="#5F1C1C", 
        fg="white", 
        font=("Arial", 12, "bold"), 
        command=calculate_time,
        borderwidth=0,
        activebackground="#3e1212",
        activeforeground="white"
    )
    btn_calc.place(x=260.0, y=180.0, width=130.0, height=45.0)

    # --- Divider Line ---
    canvas.create_rectangle(0.0, 320.0, 450.0, 328.0, fill="#5F1C1C", outline="")

    # --- Results Section ---
    canvas.create_text(25.0, 360.0, anchor="nw", text="Result:", font=("Arial", 20 * -1))
    canvas.create_text(225.0, 420.0, anchor="center", text="Time:", font=("Arial", 18 * -1))
    
    label_result = tk.Label(root, text="0.00 hours", bg="#D9D9D9", font=("Arial", 14), anchor="center")
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