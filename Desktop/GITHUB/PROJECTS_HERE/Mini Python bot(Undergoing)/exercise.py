class Student():

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return (self.name)

    def remove_student(self):
        return ("last name removed is ",mynames.pop())

class Stu_marks(Student):

    def __init__(self,smarks):
        self.smarks = smarks 

    def __str__(self):
        return (self.smarks)

class Stu_number(Student):

    def __init__(self,snum):
        self.snum = snum 

    def __str__(self):
        return (self.snum)
       


data = []
mynames = []
mymarks = []
mynum = []
ques = input("Do you want to add data(type 'y' or 'n')")
while(ques == 'y'):
    ques = input("Do you want to add data(type 'y' or 'n')")
    nm = input("enter your name")        
    s = Student(nm)
    mk = input("enter your marks")
    m = Stu_marks(mk)
    nb = input("enter your phone number")
    n = Stu_number(nb)
    print(s.name)
    print(m.smarks)
    print(n.snum)
    mynames.append(s.name)
    mymarks.append(m.smarks)
    mynum.append(n.snum)
    data.append(mynames)
    data.append(mymarks)
    data.append(mynum)
print("Your names are listed as: ",mynames)
print("Your marks are listed as: ",mymarks)
print("Your phone numbers are listed as: ",mynum)


for x in range(len(mynames)): 
    print ((mynames[x],mymarks[x],mynum[x]))



