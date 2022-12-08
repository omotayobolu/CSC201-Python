class stud:
    def __init__(self, regno, score, grade):
        self.regno=regno
        self.score=score
        self.grade=grade
    def display(self):
        print("Reg no ",self.regno, ", Score: " ,self.score ," Grade: ", self.grade)

stud1 = stud("CSC/2014/020", 74, 'A')        
stud2 = stud("EEE/2013/007", 64, 'B')        
stud3 = stud("EDU/2014/102", 87, 'A')        

stud1.display()

# It prints out stud attributes for stud1 which are regno, score and grade.