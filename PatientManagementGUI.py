import tkinter as tk
from tkinter import messagebox, simpledialog
import json
from PatientManagement import PatientManagement



class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("City Hospital Management System")
        self.root.geometry("500x400")

        self.patient_management = PatientManagement()

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="--- Welcome to City Hospital ---", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self.root, text="1. Patient Management", command=self.patient_management_menu, width=30).pack(pady=10)
        tk.Button(self.root, text="2. Exit", command=self.root.quit, width=30).pack(pady=10)

    def patient_management_menu(self):
        self.clear_window()

        tk.Label(self.root, text="*** Patient Management ***", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.root, text="1. Load Patients", command=self.load_patients, width=30).pack(pady=5)
        tk.Button(self.root, text="2. Add Patient", command=self.add_patient, width=30).pack(pady=5)
        tk.Button(self.root, text="3. Update Patient", command=self.update_patient, width=30).pack(pady=5)
        tk.Button(self.root, text="4. Search for Patient", command=self.search_patient, width=30).pack(pady=5)
        tk.Button(self.root, text="5. View Patients", command=self.view_patients, width=30).pack(pady=5)
        tk.Button(self.root, text="6. Back to Main Menu", command=self.create_main_menu, width=30).pack(pady=10)

    def load_patients(self):
        try:
            self.patient_management.loadPatients()
            messagebox.showinfo("Success", "Patients loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load patients: {e}")

    def add_patient(self):
        fname = simpledialog.askstring("Add Patient", "Enter First Name:")
        lname = simpledialog.askstring("Add Patient", "Enter Last Name:")
        age = simpledialog.askinteger("Add Patient", "Enter Age:")
        patientID = simpledialog.askinteger("Add Patient", "Enter Patient ID:")

        if fname and lname and age and patientID:
            new_patient = Patient(fname, lname, age, patientID)
            self.patient_management.addPatient()
            self.patient_management.savePatients()
            messagebox.showinfo("Success", "Patient added successfully!")
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def update_patient(self):
        patientID = simpledialog.askinteger("Update Patient", "Enter Patient ID:")
        if not patientID:
            messagebox.showwarning("Input Error", "Patient ID is required.")
            return

        updated_fname = simpledialog.askstring("Update Patient", "Enter New First Name:")
        updated_lname = simpledialog.askstring("Update Patient", "Enter New Last Name:")
        updated_age = simpledialog.askinteger("Update Patient", "Enter New Age:")

        if updated_fname and updated_lname and updated_age:
            updated_patient = Patient(updated_fname, updated_lname, updated_age, patientID)
            self.patient_management.updatePatient()
            self.patient_management.savePatients()
            messagebox.showinfo("Success", "Patient updated successfully!")
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def search_patient(self):
        patientID = simpledialog.askinteger("Search Patient", "Enter Patient ID:")
        if not patientID:
            messagebox.showwarning("Input Error", "Patient ID is required.")
            return

        patient = self.patient_management.searchForPatient()
        if patient:
            messagebox.showinfo("Patient Found", patient.displayPerson())
        else:
            messagebox.showerror("Not Found", f"Patient with ID {patientID} not found!")

    def view_patients(self):
        patients = self.patient_management.viewPatients()
        if patients:
            patients_info = "\n".join(p.displayPerson() for p in patients)
            messagebox.showinfo("Patients Info", patients_info)
        else:
            messagebox.showinfo("No Patients", "No patients found.")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Initialize GUI Application
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()
