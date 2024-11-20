from Person import Person

class Doctor(Person):

    def __init__(self, fname, lname, age, doctorID):
        super().__init__(fname, lname, age)
        self.doctorID = doctorID

    def to_json(self):
        data = super().to_json()
        data['id'] = self.doctorID
        return data
    
    def displayPerson(self):
        return (
            f"*** Patient Info ***\n"
            f"First Name: {self.fname}\n"
            f"Last Name: {self.lname}\n"
            f"Age: {self.age}\n"
            f"ID: {self.doctorID}"
        )

    


    