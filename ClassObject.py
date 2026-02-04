class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum= sum+val
        print("Hi", self.name , "your average score is", sum/3) 


s2 = Student("Karan",[99,98,97])
s2.get_avg()
