class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name1 = name                       #name1 is an attribute, name is the variable assigned to the attribute as passed in at the time of obejct instantiation
        self.major1 = major
        self.gpa1 = gpa
        self.is_on_probation1 = is_on_probation

    def is_on_honor_roll(self):
        if self.gpa1 >= 3.5:
            return True
        else:
            return False



