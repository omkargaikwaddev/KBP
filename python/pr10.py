class Employee:
    emp_name = "Omkar gaikwad"
    department = "Computer"
    salary = 60000
    def getEmp_Details(self,n,d,s):
        self.emp_name = n
        self.department = d
        self.salary = s

    def showEmp_Details(self):
        print("\nEmployee name is:",self.emp_name)
        print("Employee Department is:",self.department)
        print("Employee Salary is:",self.salary)
    
e = Employee()
e.showEmp_Details()
e.getEmp_Details("Atharv Gaikwad","Computer",50000)
e.showEmp_Details()

