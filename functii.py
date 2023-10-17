from graph import *
from math import *
''' 
    Acest program deseneaza functiile
'''

class Grafic:
    def __init__(self, width):
        self.width = width 

 
    def drawWin(self): 
        self.win = GraphWin("Grafic", self.width, self.width)
        self.win.setBackground(color_rgb(0,0,0))


    def createAxa(self):	# Axa x y
        ln1 = Line(Point(self.width/2,0),Point(self.width/2,self.width))
        ln1.setOutline(color_rgb(255,255,255))
        ln1.draw(self.win)

        ln2 = Line(Point(0,self.width/2),Point(self.width,self.width/2))
        ln2.setOutline(color_rgb(255,255,255))
        ln2.draw(self.win)
        #liniile de ajutor
        xl = 20
        while xl < self.width:
            ln3 = Line(Point(xl,self.width/2-5),Point(xl,self.width/2+5))
            ln3.setOutline("white")
            ln3.draw(self.win)
            xl += 20

        yl = 20
        while yl < self.width:
            ln4 = Line(Point(self.width/2-5,yl),Point(self.width/2+5,yl))
            ln4.setOutline("white")
            ln4.draw(self.win)
            yl += 20


    def closeWin(self):
        self.win.getMouse()
        self.win.close()



class Functii(Grafic):

    def __init__(self, functia):
        self.functia = functia

    def result(self,n):
        # self.functia.replace("x", str(n))
        functia_a = self.functia.replace('x', str(n))
        functia_a = functia_a.split()
        try:
            for i in range(len(self.functia)):
                if functia_a[i] == '^':
                    functia_a = [str(pow(float(functia_a[i-1]), float(functia_a[i+1])))] + functia_a[i+1:]
            print(functia_a)
        except IndexError: 
            pass

        string = ''

        for s in functia_a:
            string += s
        
        
        # print(self.functia)

        return eval(string)

    def formula(self, n):
        p = Point(n + graph.width/2,(self.result(n)+graph.width/2)-2*self.result(n))
        p.setOutline("white")
        p.draw(graph.win)

        # print("x : ", n)
        # print("y : ", self.result(n))
        # print()

    def draw(self):

        self.np = -100 

        while self.np <= 100:
            self.formula(self.np)
            self.np += 0.1

        graph.closeWin();

print("Ca exemplu poti scri de genul 2*x*x + 4*x + 6 \n Sau poti folosi functia sin() si cos() daca ai nevoie\nGraficul are scale mic asa ca de dorit de pus valuori destul de mari")
while True:

    fun = input("Scrie functia!:")

    if fun == "exit": break

    try :
        graph = Grafic(600)
        graph.drawWin()
        graph.createAxa()
        f = Functii(fun)
        f.draw()
    except: 
        pass