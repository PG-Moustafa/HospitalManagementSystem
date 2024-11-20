

class Person:
    
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def to_json(self):
        return {
            'fname' : self.fname,
            'lname' : self.lname,
            'age' : self.age,
        }



