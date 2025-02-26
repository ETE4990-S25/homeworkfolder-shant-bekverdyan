import json

class Person(object):
   def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email

   def to_dict(self):
       return {"Name": self.name, "Age": self.age, "Email": self.email}
    
class Student(Person):
    def __init__(self, name, age, email, student_id):
       super().__init__(name, age, email)
       self.student_id = student_id
       
    def to_dict(self):
        data = super().to_dict()
        data["Student ID"] = self.student_id
        return data

def save_to_json(filename, people):
    data = [p.to_dict() for p in people]
    with open(filename, 'w') as file:
        json.dump(data, file, indent = 2)

person_random = Person("Jeremy Clarkson", 64, "jclarkson@cpp.edu")
student_random = Student("Shant Bekverdyan", 26, "sbekverdyan@cpp.edu", 12345)

people = [person_random, student_random]

def display_json(filename):
    with open(filename, 'r') as file:
        print(file.read())

save_to_json("homework3.json", people)
display_json("homework3.json")


