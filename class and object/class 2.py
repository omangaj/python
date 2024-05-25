class employee:
    emp_id=0
    emp_name=""
    emp_sal=0

    def __init__(self,eid,ename,esal):
        self.emp_id=eid
        self.emp_name=ename
        self.emp_sal=esal

    def displaydata(self):
        print("Emp Id=",self.emp_id)
        print("Emp Name=",self.emp_name)
        print("Emp Salary=",self.emp_sal)

eid=int(input("Enter emp id="))
ename=input("Enter emp name=")
esal=int(input("Enter salary="))

emp=employee(eid,ename,esal)
emp.displaydata()
