import tkinter as tk
import sys
import os
from pathlib import Path

from Front_end.sign_in import load_sign_in_ui
from Front_end.Create import load_create_account_ui
from Front_end.Selection import load_selection_menu
from Front_end.IV_Flow_Rate import load_iv_flow_ui
from Front_end.Titration import load_titration_ui
from Front_end.Induction_Time import load_infusion_time_ui
from Front_end.Drug_dose import load_drug_dose_ui
from Front_end.Converter import load_conversion_ui


class AppManager:   
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Medical Calculator")
        
        # Start with Sign-in size
        self.root.geometry("772x398")
        self.root.configure(bg="#BABABA")

        self.canvas = tk.Canvas(self.root, bg="#BABABA", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.show_sign_in()
        self.root.mainloop()

    def clear_screen(self, width, height):
        # Destroy floating widgets (Entries, Buttons)
        for widget in self.root.winfo_children():
            if widget != self.canvas:
                widget.destroy()
        
        # Clear canvas drawings and resize
        self.canvas.delete("all")
        self.root.geometry(f"{width}x{height}")
        self.canvas.config(width=width, height=height)

    def show_sign_in(self):
        self.clear_screen(772, 398)
        load_sign_in_ui(self.root, self.canvas, self.show_create_account, self.show_menu)

    def show_create_account(self):
        self.clear_screen(772, 398)
        load_create_account_ui(self.root, self.canvas, self.show_sign_in)

    def show_menu(self):
        # Switch to tall portrait mode for the selection hub
        self.clear_screen(450, 700)
        load_selection_menu(self.root, self.canvas, self.handle_menu_navigation, self.show_sign_in)
    
    def show_iv_flow(self):
        self.clear_screen(450, 650)
        load_iv_flow_ui(self.root, self.canvas, self.show_menu)
    
    def show_titration(self):
        self.clear_screen(450, 650)
        load_titration_ui(self.root, self.canvas, self.show_menu)
    
    def show_infusion_time(self):
        self.clear_screen(450, 650)
        load_infusion_time_ui(self.root, self.canvas, self.show_menu)
    
    def show_drug_dose(self):
        self.clear_screen(450, 650)
        load_drug_dose_ui(self.root, self.canvas, self.show_menu)
    
    def show_conversion(self):
        self.clear_screen(450, 650)
        load_conversion_ui(self.root, self.canvas, self.show_menu)

    def handle_menu_navigation(self, choice):
        # Maps the text on the buttons to the functions above
        menu_map = {
            "IV Flow Rate": self.show_iv_flow,
            "Titration": self.show_titration,
            "Infusion Time": self.show_infusion_time,
            "Drug Dose": self.show_drug_dose,
            "Conversion": self.show_conversion
        }
        
        if choice in menu_map:
            menu_map[choice]()

if __name__ == "__main__":
    AppManager()