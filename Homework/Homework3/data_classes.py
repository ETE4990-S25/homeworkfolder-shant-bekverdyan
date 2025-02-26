import json

class person(object):
   def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email

    def to_dict(self):
       return {"Name": self.name, "Age": self.age, "Email": self.email}
    

class student(person):
    def __init__(self, name, age, email, student_id):
       super().__init__(name, age, email)
       self.student_id = student_id

