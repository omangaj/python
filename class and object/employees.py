class employee:
    emp_id=0
    emp_name=""
    emp_sal=0

    def __init__(self,eid,ename,esal):
        self.emp_id=eid
        self.emp_name=ename
        self.emp_sal=esal

    def semp(self):
        s = int(input("Enter employee id to search:"))
        print("id   name    salary")
        for k in d:
            if k == s:
                for i in d[k]:
                    print(i, end="      ")

d={}
l=[]
n=int(input("How many employee add:"))
for i in range(n):
    emp=[]
    emp_id=int(input("Enter emp id="))
    emp_name=input("Enter emp name=")
    emp_sal=int(input("Enter salary="))
    emp.append(emp_id)
    emp.append(emp_name)
    emp.append(emp_sal)
    d[emp_id]=emp
    l.append(emp)

e=employee(emp_id,emp_name,emp_sal)
e.semp()

# d={}
# i=1
# n=int(input("How many employee add:"))
# for i in range(n):
#     emp=[]
#     emp_id=int(input("Enter emp id="))
#     emp_name=input("Enter emp name=")
#     emp_sal=int(input("Enter salary="))
#     emp.append(emp_id)
#     emp.append(emp_name)
#     emp.append(emp_sal)
#     d[emp_name]=emp
# s=input("Enter employee id to search:")
# print("id   name    salary")
# for k in d:
#     if k==s:
#         for i in d[k]:
#             print(i,end="      ")
# e=employee
# e.displaydata()
#
# d={}
# i=1
# n=int(input("How many employee add:"))
# for i in range(n):
#     emp=[]
#     emp_id=int(input("Enter emp id="))
#     emp_name=input("Enter emp name=")
#     emp_sal=int(input("Enter salary="))
#     emp.append(emp_id)
#     emp.append(emp_name)
#     emp.append(emp_sal)
#     d[emp_sal]=emp
# print(d)
#
# s=int(input("Enter employee id to search:"))
# print("id   name    salary")
# for k in d:
#     if k==s:
#         for i in d[k]:
#             print(i,end="      ")
# e=employee
# e.displaydata()