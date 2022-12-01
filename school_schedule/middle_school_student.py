from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, 
                 grade, classes, gets_transportation=False):
        super().__init__(name,grade,classes)

        self.gets_transportation = gets_transportation

    def summary(self):
        std_summary = super().summary() +"\n"
        gets_trans = "gets" if self.gets_transportation else "doesn't get"
        return std_summary + f"{self.name} " + gets_trans + " transportation"