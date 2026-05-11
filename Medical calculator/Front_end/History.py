import tkinter as tk

def load_history_ui(root, canvas, on_return, username, get_history_func):
    """
    get_history_func: This will be the function from database.py
    """
    canvas.delete("all")

    # --- Header ---
    canvas.create_rectangle(0.0, 0.0, 450.0, 60.0, fill="#5F1C1C", outline="")
    canvas.create_text(
        20.0, 30.0, 
        anchor="w", 
        text=f"History: {username}", 
        fill="#FFFFFF", 
        font=("Arial", 18 * -1)
    )

    # Fetch data
    logs = get_history_func(username)

    if not logs:
        canvas.create_text(225.0, 300.0, text="No calculations found.", font=("Arial", 14))
    else:
        # Display the last 5-8 entries (simple list)
        y_pos = 100
        for entry in logs[:7]: # Limit display to fit screen
            # Draw a small box for each log
            canvas.create_rectangle(20.0, y_pos, 430.0, y_pos + 60.0, fill="#D9D9D9", outline="")
            
            # Type of Calc (e.g., IV Flow)
            canvas.create_text(30.0, y_pos + 10, anchor="nw", text=entry['type'], font=("Arial", 12, "bold"))
            
            # Inputs used
            canvas.create_text(30.0, y_pos + 35, anchor="nw", text=entry['inputs'], font=("Arial", 10))
            
            # Result (Aligned Right)
            canvas.create_text(420.0, y_pos + 30, anchor="e", text=entry['result'], font=("Arial", 12, "bold"), fill="#5F1C1C")
            
            y_pos += 70

    # --- Return Button ---
    btn_return = tk.Button(
        root,
        text="Return to Menu", 
        bg="#5F1C1C", 
        fg="white", 
        font=("Arial", 12), 
        command=on_return,
        borderwidth=0
    )
    btn_return.place(x=150.0, y=600.0, width=150.0, height=40.0)