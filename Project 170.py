from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Project 170")
label1 = Label(root)
label2 = Label(root)
label3 = Label(root)

class grade_3() :
    def __init__(self, language_arts, mathematics) :
        self.language_arts = language_arts
        self.mathematics = mathematics
        
    def percentage(self) :
        total_marks = self.language_arts + self.mathematics
        total_100 = total_marks * 100
        grade3_percent = total_marks/200
        label1["text"] = str(grade3_percent)

class grade_5() :
    def __init__(self, language_arts, mathematics, social_studies) :
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        
    def percentage(self) :
        total_marks = self.mathematics + self.language_arts + self.social_studies
        total_100 = total_marks * 100
        grade5_percent = total_marks/300
        label2["text"] = str(grade5_percent)
        
class grade_10() :
    def __init__(self, language_arts, mathematics, social_studies, foreign_language) :
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.foreign_language = foreign_language
        
    def percentage(self) :
        total_marks = self.mathematics + self.language_arts + self.social_studies + self.foreign_language
        total_100 = total_marks * 100
        grade10_percent = total_marks/400
        label3["text"] = str(grade10_percent)

obj1 = grade_3(60, 100)
obj2 = grade_5(60, 100, 40)
obj3 = grade_10(60, 100, 40, 110)
btn1 = Button(root, text = "Grade 3", command = obj1.percentage)
btn2 = Button(root, text = "Grade 5", command = obj2.percentage)
btn3 = Button(root, text = "Grade 10", command = obj3.percentage)
btn1.pack()
label1.pack()
btn2.pack()
label2.pack()
btn3.pack()
label3.pack()
root.mainloop()