
import json
from Patient import Patient

class PatientManagement:

    def __init__(self):
        self.patients = {}

    def loadPatients(self):

        try:
            with open('patients.json', 'r') as file:
                self.patients = json.load(file)
                print("Patients loaded successfully!")
                return
        
        except FileNotFoundError:
            print("File not found!")
            return

    def savePatients(self):

        patients_data = [Patient(**p) for p in self.patients]
        patients = [p.to_json() for p in patients_data]

        with open('patients.json', 'w') as file:
                json.dump(patients, file, indent=4)

        print("Patients saved successfully!")

    def displayMenu(self):
        print("\n*** Patient Management List ***")
        print("1. Load Patients Data")
        print("2. Add new patient")
        print("3. Update patient info")
        print("4. Search for patient")
        print("5. View patient info")
        print("6. Exit")
        print("*******************************")

    def pManagementStart(self):
        
        while True:

            self.displayMenu()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # load patients data
                self.loadPatients()

            elif choice == 2:
                # add new patient
                self.addPatient()
                self.savePatients()

            elif choice == 3:
                # update patient
                self.updatePatient()
                self.savePatients()

            elif choice == 4:
                # search for patient
                self.searchForPatient()

            elif choice == 5:
                # view patients info
                self.viewPatients()

            elif choice == 6:
                # exit program
                return
            
            else:
                print("Invalid choice!")

    def addPatient(self):
        print("*** Adding new patient ***")
        new_patient = Patient(None, None, None, None)
        new_patient.readPatient()

        patients = [Patient(**p) for p in self.patients]

        for p in patients:
            if p.patientID == new_patient.patientID:
                print("Patient already exists!")
                return
        
        patients.append(new_patient)
        self.patients = [p.to_json() for p in patients]

    def updatePatient(self):
        print("*** Updating patient info ***")
        id = int(input("\nEnter Patient ID: "))

        patients = [Patient(**p) for p in self.patients]

        for p in patients:
            if p.patientID == id:
                p.readPatient()
                print("Patient updated successfully!")
        
        self.patients = [p.to_json() for p in patients]
    
    def searchForPatient(self):
        id = int(input("Enter Patient_ID: "))

        patients = [ Patient(**p) for p in self.patients]

        for p in patients :
            if p.patientID == id:
                print("Patient found!")
                print(p.displayPerson())
                return
        print(f"Patient with Patient_ID {id} not found!")

    def viewPatients(self):
        return [Patient(**p) for p in self.patients]

    def viewPatients2(self):
        patients = [Patient(**p) for p in self.patients]
        if patients:
            print("*** View Patients Info ***")
        for p in patients:
            print(p.displayPerson())

