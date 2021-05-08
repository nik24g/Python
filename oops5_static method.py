class Students:
    university = "RGPV"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        pass

    @staticmethod
    # static methods used when we make simple method without using self and cls as parameter
    # staticmethod have no access of property of object and class
    def college():
        print("Shriram college of engineering and management")
    pass


shayna = Students("Shayna Chhari", "71")
print(shayna.name)
shayna.college()
Students.college()
