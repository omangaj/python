class stud:
    def __init__(self,sid,sname):
        self.sid=sid
        self.sname=sname

    def displaystud(self):
        print("sid=",sid)
        print("sname=",sname)

sid=int(input("Enter sid="))
sname=input("Enter name=")
class emp(stud):
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
        stud.__init__(self,sid,sname)

    def displayemp(self):
        print("eid=",eid)
        print("ename=",ename)

eid=int(input("Enter eid="))
ename=input("Enter eame=")

e=emp(eid,ename)
e.displaystud()
e.displayemp()
