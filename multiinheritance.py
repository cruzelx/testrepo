class SchoolMember:
    def __init__(self, firstname, lastname, age, sex):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def __str__(self):
        print('''firstname: %s
lastname: %s
age: %s
sex: %s
''' %(self.firstname,self.lastname,self.age,self.sex))
    def line(self):
            print("---------------------------------------------")

class teachers(SchoolMember):
    def __init__(self, firstname, lastname, age, sex, periods, faculty, salary):
        super().__init__(firstname,lastname,age,sex)
        self.periods = periods
        self.salary = salary
        self.faculty = faculty

    def TeachInfo(self):
        """self.display()"""
        print('''periods: %s
salary: %s
faculty: %s
''' %(self.periods, self.salary, self.faculty))
        self.line()

class Students(SchoolMember):
    def __init__(self, firstname, lastname, age, sex, fee, scholarship):
        super().__init__(firstname, lastname, age, sex)
        self.fee = fee
        self.scholarship = scholarship

    def StudInfo(self):
        """self.display()"""
        print('''fee: %s
scholarship: %s

''' %(self.fee, self.scholarship))
        self.line()



a = Students("alex","bhattarai","19","male","4000","40%")
b = teachers("ram","kumar","27","male","4","chemistry","20000")

a.StudInfo()
b.TeachInfo()
