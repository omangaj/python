class employee:
    def __init__(self,eid,ename,esal):
        self.emp_id=eid
        self.emp_name=ename
        self.emp_sal=esal

    def displaydata(self):
        print("Emp Id:",self.emp_id)
        print("Emp name:",self.emp_name)
        print("Emp sal:",self.emp_sal)

    def semp(self):
        s = int(input("Enter employee id for search employee:"))
        print("id   name    salary")
        for k in d:
            if k == s:
                for i in d[k]:
                    print(i, end="       ")


d={}
n=int(input("how many employees:"))
for i in range(n):
    emp=[]
    emp_id=int(input("Enter id:"))
    emp_name=input("Enter name:")
    emp_sal=int(input("Enter salary:"))
    emp.append(emp_id)
    emp.append(emp_name)
    emp.append(emp_sal)
    d[emp_id]=emp
print(d)

e=employee
e.displaydata()