import math
from tkinter import Entry, Button, Label

def load_iv_flow_ui(root, canvas, on_return_click):
    """
    root: The main Tk window
    canvas: The shared canvas from main.py
    on_return_click: The function to go back to the selection menu
    """
    # 1. Clear previous screen
    canvas.delete("all")

    # --- Header ---
    canvas.create_rectangle(0.0, 0.0, 450.0, 60.0, fill="#5F1C1C", outline="")
    canvas.create_text(
        20.0, 30.0,
        anchor="w",
        text="IV Flow Rate",
        fill="#FFFFFF",
        font=("Arial", 24 * -1)
    )

    # --- Input Section ---
    canvas.create_text(25.0, 100.0, anchor="nw", text="Volume (ml):", font=("Arial", 18 * -1))
    entry_vol = Entry(root, bd=0, bg="#D9D9D9", justify="left", font=("Arial", 14))
    entry_vol.place(x=25.0, y=130.0, width=200.0, height=35.0)

    canvas.create_text(25.0, 200.0, anchor="nw", text="Time (Hours):", font=("Arial", 18 * -1))
    entry_time = Entry(root, bd=0, bg="#D9D9D9", justify="left", font=("Arial", 14))
    entry_time.place(x=25.0, y=230.0, width=200.0, height=35.0)

    # --- Result Labels (Created before the function so it can find them) ---
    result_df20 = Label(root, text="0.00", bg="#D9D9D9", font=("Arial", 14), anchor="center")
    result_df20.place(x=25.0, y=420.0, width=170.0, height=40.0)

    result_df60 = Label(root, text="0.00", bg="#D9D9D9", font=("Arial", 14), anchor="center")
    result_df60.place(x=255.0, y=420.0, width=170.0, height=40.0)

    # --- Calculation Logic ---
    def calculate_flow():
        try:
            vol = float(entry_vol.get())
            time = float(entry_time.get())
            
            # Formula: (Volume * Drop Factor) / (Time in minutes)
            res_20 = math.ceil((vol / time) / 3)
            res_60 = math.ceil((vol / time))
            
            result_df20.config(text=f"{res_20:.2f}")
            result_df60.config(text=f"{res_60:.2f}")
        except (ValueError, ZeroDivisionError):
            result_df20.config(text="Error")
            result_df60.config(text="Error")

    # --- Calculate Button ---
    btn_calc = Button(
        root,
        text="Calculate",
        bg="#5F1C1C",
        fg="white",
        font=("Arial", 12, "bold"),
        borderwidth=0,
        command=calculate_flow
    )
    btn_calc.place(x=280.0, y=170.0, width=120.0, height=45.0)

    # --- Decoration & Labels ---
    canvas.create_rectangle(0.0, 300.0, 450.0, 308.0, fill="#5F1C1C", outline="")
    canvas.create_text(25.0, 340.0, anchor="nw", text="Results:", font=("Arial", 20 * -1))
    canvas.create_text(110.0, 390.0, anchor="center", text="DF:20", font=("Arial", 18 * -1))
    canvas.create_text(340.0, 390.0, anchor="center", text="DF:60", font=("Arial", 18 * -1))

    # --- Return Button ---
    btn_return = Button(
        root,
        text="Return",
        bg="#5F1C1C",
        fg="white",
        font=("Arial", 14),
        command=on_return_click,
        borderwidth=0
    )
    btn_return.place(x=25.0, y=580.0, width=140.0, height=40.0)