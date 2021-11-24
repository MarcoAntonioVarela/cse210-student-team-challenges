#Marco Varela (step 1-5)
#Week 10

class Person:

    def __init__(self,fname,lname):
        #self._fullname = Fname + " "+ Lname
        self._f_name = fname
        self._l_name = lname
        fullname = fname + " "+ lname
        self._full_name = fullname

    
    def get_fname(self):
        return self._f_name

    def get_lname(self):
        return self._l_name

    def set_fname(self,fname):
        self._f_name = fname
    
    def set_lname(self,lname):
        self._l_name = lname
       
    def get_full_name(self):
        return self._f_name+" "+self._l_name


#I will add the student class in this file, but in other cases, I would place this class inside of its own file
class Student(Person):

    def __init__(self,fname,lname,gpa):
        #Calling my superclas(parent class) __init__
        super().__init__(fname,lname)
        self._gpa = gpa
        
        
    def get_gpa(self):
        return self._gpa

    def set_gpa(self,gpa):
        self._gpa = gpa


Bob = Student ("Marc0", "Varela", 4.00)
Marco = Student ("Scott", "Burton", 4.0)
Jeremy = Student ("Jeremy", "Bush", 3.7)
Jenny = Student ("Jenny", "Davis",2.7)

#Now I will change Jenny's last name using the set method
Jenny.set_lname("Smith")
#print(Jenny.get_full_name())

#Bob.Set_Name("Bob", "Robert")

people = [Bob, Marco, Jeremy,Jenny]
number = 0

for person in people:
    number += 1
    print(f"Person {number} = {person.get_full_name()}, GPA = {person.get_gpa()}")
    

       

