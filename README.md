# Medical Calculator Suite

A robust, desktop-based clinical tool built with **Python** and **Tkinter**, designed to assist healthcare students and professionals in performing high-accuracy calculations for IV therapy and medication titration.

This suite provides essential calculation tools secured behind a custom user authentication system, organized with a clean, modular architecture.

---

## 🚀 Features

* **User Authentication**: Secure Sign-In and Account Creation using a JSON-based local database.
* **IV Flow Rate**: Calculate Macro (DF:20) and Micro (DF:60) drops per minute.
* **Titration**: Specialized calculations for Dopamine and Dobutamine infusions.
* **Drug Dosage**: Determine total dosage (mg) and exact volume (mL) to administer based on patient weight and stock availability.
* **Infusion Time**: Calculate the duration of an infusion based on total volume and hourly rate.
* **Unit Conversion**: Quick conversion between kg/lbs and mg/g.

---

## 📁 Project Structure

The project follows a **Modular Architecture** to keep the code clean and maintainable:

* **`Main.py`**: The Controller. Manages window resizing and navigation between screens.
* **`Back_end/`**:
    * `database.py`: The Backend. Handles account storage and login verification.
    * `accounts.json`: Local storage for user credentials.
* **`Front_end/`**:
    * `sign_in.py` & `Create.py`: Front-end for user access.
    * `Selection.py`: The Hub. Links all calculation modules.
    * `iv_flow.py`, `titration.py`, `drug_dose.py`, etc.: Individual modules for each specific calculator.
* **`assets/`**: Contains images and UI elements used by the Tkinter canvas.

---

## 🛠️ Installation & Setup

1.  **Prerequisites**: Ensure you have **Python 3.x** installed.
2.  **Clone/Download**: Download all project files and maintain the folder structure (Back_end, Front_end, assets).
3.  **Run the App**:
    Open your terminal in the root folder and run:
    ```bash
    python Main.py
    ```

---

## 📊 Technical Details

* **GUI Framework**: Tkinter
* **Data Storage**: Flat-file JSON (`accounts.json`).
* **Design**: Custom UI utilizing Canvas drawings for a modern, medical-themed aesthetic (Deep Red theme: `#5F1C1C`).

---

## 📝 Usage

1.  **Start**: Launch the app and select "Create Account" if you are a new user.
2.  **Access**: Log in with your registered credentials.
3.  **Calculate**: Select a calculator from the Selection Menu.
4.  **Process**: Input the required values and click **Calculate** to see instant results.
5.  **Navigate**: Use the **Return** button to switch between different tools or log out.
