

class Person(object):
    """Represents person"""

    def __init__(self, name, age, email):
        """Initializing person's attributes"""
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    """Represents student"""
    def __init__(self, student_id):
        """Initializing student's attributes"""
        self.student_id = student_id


    
    
        
