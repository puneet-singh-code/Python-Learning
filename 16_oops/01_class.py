# class: class is a blueprint or a template. Eg. form for an exam that contains name, age, electives, father's name etc.

# Object: specific instance created from the template (class). Eg. Form which contains the data for john doe


class Employee:
    company = "HP"

    def get_salary(self): # self is important here because self is a way to reference the object of the class which is being created
        return 34000

e = Employee() #An object of class Employee is created here
print(e.get_salary()) # Employee's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)
