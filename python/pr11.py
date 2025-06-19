class Degree:
    def get_Degree(self):
        print("i got a degree")

class UnderGraduate(Degree):
    def print1(self):
        print("I am under graduate")

class PostGraduate(Degree):
    def print2(self):
        print("I am Post graduate")

d = Degree()
u = UnderGraduate()
p = PostGraduate()

d.get_Degree()
u.get_Degree()
p.get_Degree()

u.print1()
p.print2()

