import json
from PatientManagement import PatientManagement

# This project aims to create a basic hospital management system that can
# manage patient records, doctor appointments, and billing information. We'll
# use Python and a suitable database JSON to store and retrieve data.

class Hospital:

    def __init__(self):
        self.doctors = {}
        self.patients = {}
        self.patient_management = PatientManagement()

    def MainMenu(self):
        print("---Welcome to City Hospital---\n")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Scheduling")
        print("4. Billing System")
        print("5. Exit")

    def start(self):
        

        while True:
            self.MainMenu()
            choice = int(input("\nChoose what to do: "))

            if choice == 1:
                # Patient Management
                self.patient_management.pManagementStart()

            elif choice == 2:
                # Doctor Management
                return
            
            elif choice == 3:
                # Appointment Scheduling
                return
            
            elif choice == 4:
                # Billing System
                return
            
            elif choice == 5:
                # exit system
                print("System Exited...")
                return

            else:
                print("Invalid choice!")



