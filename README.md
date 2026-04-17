# Medical_Calculator
A robust, desktop-based clinical tool built with Python and Tkinter, designed to assist healthcare students in performing high-accuracy calculations for IV therapy and medication titration.

A comprehensive, modular desktop application built with Python and Tkinter. This suite provides medical professionals and students with essential calculation tools, including IV Flow Rates, Drug Dosages, and Titration calculations, all secured behind a custom user authentication system.

🚀 FeaturesUser Authentication: Secure Sign-In and Account Creation using a JSON-based local database.
IV Flow Rate: Calculate Macro (DF:20) and Micro (DF:60) drops per minute.
Titration: Specialized calculations for Dopamine and Dobutamine infusions.
Drug Dosage: Determine total dosage (mg) and exact volume (mL) to administer based on patient weight and stock availability.
Infusion Time: Calculate the duration of an infusion based on total volume and hourly rate.
Unit Conversion: Quick conversion between kg/lbs and mg/g.

📁 Project StructureThe project follows a Modular Architecture to keep the code clean and maintainable:main.py: The Controller. Manages window resizing and navigation between screens.database_logic.py: The Backend. Handles account storage and login verification.selection_menu.py: The Hub. Links all calculation modules.sign_in.py & create_account.py: Front-end for user access.iv_flow.py, titration.py, drug_dose.py, etc.: Individual modules for each specific calculator.

🛠️ Installation & SetupPrerequisites: Ensure you have Python 3.x installed.Clone/Download: Download all .py files into a single folder.Assets: Ensure your assets folder (containing images) is in the correct path as defined in the code.Run the App:Bashpython main.py

📊 Technical DetailsGUI Framework: TkinterData Storage: Flat-file JSON (accounts.json).Design: Custom UI utilizing Canvas drawings for a modern, medical-themed aesthetic ($5F1C1C$ deep red theme).📝 UsageLaunch the app and Create an Account.Log in with your credentials.Select a calculator from the Selection Menu.Input the required values and click Calculate to see instant results.Use the Return button to switch between different tools.
