#this is a internal class 
class family:
    father_name = "bouzid"
    mother_name = "houria"
    sister_name = "mira"
    brother_name = "samir"
    def __init__(self,father_name,mother_name,sister_name,brother_name):
        self.father_name = father_name
        self.mother_name = mother_name
        self.sister_name = sister_name
        self.brother_name = brother_name
    def __init__():
        pass
        
    def __str__(self):
        return f"{self.father_name}"

#instonciation of the family class
fam = family("lakhder","malika","oum hani","said")
fam1 = family()

#fam1.father_name = "said"
print("fam "+fam.father_name)
print("fam1 "+fam1.father_name)

print(fam)
