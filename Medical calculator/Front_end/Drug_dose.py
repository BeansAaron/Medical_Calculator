import tkinter as tk
from tkinter import messagebox

def load_drug_dose_ui(root, canvas, on_return):
    """
    root: The main Tk window
    canvas: The shared canvas
    on_return: Function to go back to the Selection Menu
    """
    canvas.delete("all")

    # --- Calculation Logic ---
    def calculate_dose():
        try:
            # Fetch values from entry boxes
            d_pk = entry_dose.get()
            w = entry_weight.get()
            s_mg = entry_stock_mg.get()
            s_ml = entry_stock_ml.get()

            if not all([d_pk, w, s_mg, s_ml]):
                messagebox.showwarning("Input Error", "Please fill in all fields.")
                return

            dose_per_kg = float(d_pk)
            weight = float(w)
            stock_mg = float(s_mg)
            stock_ml = float(s_ml)
            
            if stock_mg == 0:
                messagebox.showerror("Error", "Stock mg cannot be zero!")
                return
            
            # Formula: (Dose * Weight) = Total Dose; (Total Dose / Stock mg) * Stock mL = Volume
            total_dose = dose_per_kg * weight
            volume_to_give = (total_dose / stock_mg) * stock_ml
            
            # Update result labels
            label_total_dose.config(text=f"{total_dose:.2f} mg", fg="black")
            label_volume.config(text=f"{volume_to_give:.2f} mL", fg="black")
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")

    # --- Header ---
    canvas.create_rectangle(0.0, 0.0, 450.0, 60.0, fill="#5F1C1C", outline="")
    canvas.create_text(
        20.0, 30.0, 
        anchor="w", 
        text="Drug Dose", 
        fill="#FFFFFF", 
        font=("Arial", 24 * -1)
    )

    # --- Input Section ---
    # Ordered Dose
    canvas.create_text(25.0, 80.0, anchor="nw", text="Ordered Dose (mg/kg):", font=("Arial", 14 * -1))
    entry_dose = tk.Entry(root, bd=0, bg="#D9D9D9", font=("Arial", 12))
    entry_dose.place(x=25.0, y=105.0, width=180.0, height=30.0)

    # Weight
    canvas.create_text(25.0, 150.0, anchor="nw", text="Weight (kg):", font=("Arial", 14 * -1))
    entry_weight = tk.Entry(root, bd=0, bg="#D9D9D9", font=("Arial", 12))
    entry_weight.place(x=25.0, y=175.0, width=180.0, height=30.0)

    # Stock mg
    canvas.create_text(25.0, 220.0, anchor="nw", text="Stock (mg):", font=("Arial", 14 * -1))
    entry_stock_mg = tk.Entry(root, bd=0, bg="#D9D9D9", font=("Arial", 12))
    entry_stock_mg.place(x=25.0, y=245.0, width=180.0, height=30.0)

    # Stock mL
    canvas.create_text(25.0, 290.0, anchor="nw", text="Stock Volume (mL):", font=("Arial", 14 * -1))
    entry_stock_ml = tk.Entry(root, bd=0, bg="#D9D9D9", font=("Arial", 12))
    entry_stock_ml.place(x=25.0, y=315.0, width=180.0, height=30.0)

    # --- Calculate Button ---
    btn_calc = tk.Button(
        root,
        text="Calculate", 
        bg="#5F1C1C", 
        fg="white", 
        font=("Arial", 12, "bold"), 
        command=calculate_dose,
        borderwidth=0
    )
    btn_calc.place(x=260.0, y=190.0, width=130.0, height=50.0)

    # --- Divider ---
    canvas.create_rectangle(0.0, 360.0, 450.0, 368.0, fill="#5F1C1C", outline="")

    # --- Results Section ---
    canvas.create_text(25.0, 390.0, anchor="nw", text="Result:", font=("Arial", 20 * -1))

    # Total Dose Result
    canvas.create_text(110.0, 440.0, anchor="center", text="Total Dose:", font=("Arial", 16 * -1))
    label_total_dose = tk.Label(root, text="0.00 mg", bg="#D9D9D9", font=("Arial", 14), anchor="center")
    label_total_dose.place(x=25.0, y=465.0, width=170.0, height=45.0)

    # Volume to Give Result
    canvas.create_text(340.0, 440.0, anchor="center", text="Give (mL):", font=("Arial", 16 * -1))
    label_volume = tk.Label(root, text="0.00 mL", bg="#D9D9D9", font=("Arial", 14), anchor="center")
    label_volume.place(x=255.0, y=465.0, width=170.0, height=45.0)

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