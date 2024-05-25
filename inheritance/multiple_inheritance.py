class stud:
    def __init__(self,sid,sname):
        self.sid=sid
        self.sname=sname

    def displaystud(self):
        print("sid=",sid)
        print("sname=",sname)

sid=int(input("Enter sid="))
sname=input("Enter name=")
class emp:
    def __init__(self,eid,ename):
        self.eid=eid
        self.ename=ename
        stud.__init__(self,sid,sname)

    def displayemp(self):
        print("eid=",eid)
        print("ename=",ename)

eid=int(input("Enter eid="))
ename=input("Enter eame=")
class hr(stud,emp):
    def __init__(self,hid,hname):
        self.hid=hid
        self.hname=hname
        emp.__init__(self,eid,ename)
        stud.__init__(self, sid, sname)

    def displayhr(self):
        print("hid=",hid)
        print("hname=",hname)

hid=int(input("Enter hid="))
hname=input("Enter hame=")
h=hr(eid,hname)
h.displayhr()
h.displayemp()
h.displaystud()

