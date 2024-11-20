from Person import Person

class Patient(Person):

    def __init__(self, fname, lname, age, patientID):
        super().__init__(fname, lname, age)
        self.patientID = patientID

    def to_json(self):
        data = super().to_json()
        data['patientID'] = self.patientID
        return data
    
    def displayPerson(self):
        return (
            f"\n*** Patient Info ***\n"
            f"First Name: {self.fname}\n"
            f"Last Name: {self.lname}\n"
            f"Age: {self.age}\n"
            f"ID: {self.patientID}"
        )

    def readPatient(self):
        print("\nEnter Patient details: ")
        fname = input("FName: ")
        lname = input("LName: ")
        age = int(input("Age: "))
        patientID = int(input("PatientID: "))   
        self.fname = fname
        self.lname = lname
        self.age = age
        self.patientID = patientID
        return self
    


