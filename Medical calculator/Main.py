import tkinter as tk
import sys
import os
from pathlib import Path

# ... (All your existing imports remain the same)
from Front_end.sign_in import load_sign_in_ui
from Front_end.Create import load_create_account_ui
from Front_end.Selection import load_selection_menu
from Front_end.IV_Flow_Rate import load_iv_flow_ui
from Front_end.Titration import load_titration_ui
from Front_end.Induction_Time import load_infusion_time_ui
from Front_end.Drug_dose import load_drug_dose_ui
from Front_end.Converter import load_conversion_ui
from Front_end.History import load_history_ui 

class AppManager:   
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Medical Calculator")
        
        # Track the logged-in user
        self.current_user = None
        
        # 1. Start with Sign-in size
        self.root.geometry("772x398")
        
        # 2. DISABLE FULLSCREEN AND RESIZING
        # This locks the window so users can't stretch it or hit 'Maximize'
        self.root.resizable(False, False)
        
        self.root.configure(bg="#BABABA")

        self.canvas = tk.Canvas(self.root, bg="#BABABA", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.show_sign_in()
        self.root.mainloop()

    def clear_screen(self, width, height):
        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()
        
        self.canvas.delete("all")
        
        # We update the geometry here for different screen sizes, 
        # but since resizable is False, the user still can't change it themselves.
        self.root.geometry(f"{width}x{height}")
        self.canvas.config(width=width, height=height)

    # ... (Rest of your methods: show_sign_in, show_menu, etc. stay exactly the same)
    def show_sign_in(self):
        self.current_user = None 
        self.clear_screen(772, 398)
        load_sign_in_ui(self.root, self.canvas, self.show_create_account, self.show_menu)

    def show_create_account(self):
        self.clear_screen(772, 398)
        load_create_account_ui(self.root, self.canvas, self.show_sign_in)

    def show_menu(self, username=None):
        if username:
            self.current_user = username
        self.clear_screen(450, 700)
        load_selection_menu(self.root, self.canvas, self.handle_menu_navigation, self.show_sign_in)
    
    def show_history(self):
        from Back_end.database import get_history 
        self.clear_screen(450, 650)
        load_history_ui(self.root, self.canvas, self.show_menu, self.current_user, get_history)

    def show_iv_flow(self):
        self.clear_screen(450, 650)
        load_iv_flow_ui(self.root, self.canvas, self.show_menu, self.current_user)
    
    def show_titration(self):
        self.clear_screen(450, 650)
        load_titration_ui(self.root, self.canvas, self.show_menu, self.current_user)
    
    def show_infusion_time(self):
        self.clear_screen(450, 650)
        load_infusion_time_ui(self.root, self.canvas, self.show_menu, self.current_user)
    
    def show_drug_dose(self):
        self.clear_screen(450, 650)
        load_drug_dose_ui(self.root, self.canvas, self.show_menu, self.current_user)
    
    def show_conversion(self):
        self.clear_screen(450, 650)
        load_conversion_ui(self.root, self.canvas, self.show_menu, self.current_user)

    def handle_menu_navigation(self, choice):
        menu_map = {
            "IV Flow Rate": self.show_iv_flow,
            "Titration": self.show_titration,
            "Infusion Time": self.show_infusion_time,
            "Drug Dose": self.show_drug_dose,
            "Conversion": self.show_conversion,
            "History": self.show_history 
        }
        if choice in menu_map:
            menu_map[choice]()

if __name__ == "__main__":
    AppManager()