class student:
    sid=1
    sname="Atul"
    age=18

    @staticmethod
    def displayData(self):
        print("Sid=",self.sid)
        print("Name=",self.sname)
        print("Age=",self.age)

stud=student()
stud.displayData(self=stud)