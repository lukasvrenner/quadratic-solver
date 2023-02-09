#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import math

def program():

    #assign values to a, b, and c
    print ("ax^2 + bx + c")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    #sets a, b, and c to integers if they are whole
    if a % 2 == 1 or a % 2 == 0:
        a = int(a)
    if b % 2 == 1 or b % 2 == 0:
        b = int(b)
    if c % 2 == 1 or c % 2 == 0:
        c = int(c)

    #define variables
    AOS = -(b)/(2 * a)
    if AOS % 2 == 1 or AOS % 2 == 0:
        AOS = int(AOS)
    Y = a*AOS**2 + b*AOS + c
    L = 1/(4*a)
    F = str(AOS) + ", " + str(Y + L)
    dscrm = b**2 - 4*a*c
    drctx = " y = " + str(Y - L)
    prdct = c * a
    #functions
    def graph(formula, xrange):
        x = np.array(xrange)
        y = formula(x)
        plt.plot(x, y)
        plt.axis([-6, 6, -6, 6])
        plt.grid()
        plt.show()
        
    def my_formula(x):
        return a * x ** 2 + b * x + c

    def manual():
        print ("""
vertex                aos
y intercept         zeros
focus               graph
manual              reset
exit              discrim
directix      vertex form
factor""")
    #manual
    print ("""
Here is a list of commands that can be used in the program""")
    def ifs ():

        #enter command
        print("")
        cmnd = input()
        print("")

        #output of command
        if cmnd == "vertex":
            print ('(' + str(AOS) + ',', str(Y) + ')')
            ifs()

        if cmnd == "aos":
            print ("x =", AOS)
            ifs()
            
        if cmnd == "y intercept":
            print (c)
            ifs()
            
        if cmnd == "zeros":
            if dscrm >= 0 and math.sqrt(dscrm) % 2 == 1 or dscrm >=0 and  math.sqrt(dscrm) % 2 == 0:
                print ("(" + str(-b) + " ± " + str(int(math.sqrt(dscrm))) + ")" + " / " + str(2*a))
                zero1 = (-b + int(math.sqrt(dscrm))) / (2*a)
                zero2 = (-b - int(math.sqrt(dscrm))) / (2*a)
                print (zero1, "and", zero2)

            else:
                print ("(" + str(-b) + " ± √" + str(dscrm) + ")" + " / " + str(2*a))
                if dscrm >= 0:
                    zero1 = (-b - math.sqrt(dscrm))/(2*a)
                    zero2 = (-b + math.sqrt(dscrm))/(2*a)
                    print (str(zero1) + " and "  + str(zero2))
            ifs()

        if cmnd == "focus":
            print ("(" + F + ")")
            ifs()

        if cmnd == "graph":
            graph(my_formula, np.linspace(-100, 100, 100000))
            ifs()
        
        if cmnd == "discrim":
            print (dscrm)
            ifs()
        
        if cmnd == "vertex form":
            if AOS >= 0:
                print ("y = (x -", AOS + ")^2 +", Y)
            else:
                print ("y = (x + " + str(abs(AOS)) + ")^2 +", Y)

            ifs()

        if cmnd == "factor":
            prime = True
            #determines what the middle number splits into
            for factor in range (-abs(prdct), abs(prdct)):
                if factor != 0:
                    f = prdct//factor
                    if prdct % factor == 0 and factor + f == b:
                        prime = False
                        #determines greatest common factor
                        for factrd in range (abs(a), -abs(a), -1):
                            if factrd != 0:
                                if a % factrd == 0 and f % factrd == 0:
                                    w = factrd
                                    break
                            else:
                                pass
                        #determines greatest common factor
                        for fctrd in range (abs(factor), -abs(factor), -1):
                            if factrd != 0:
                                if factor % fctrd == 0 and c % fctrd == 0:
                                    z = fctrd
                                    break
                            else:
                                pass
                        #eliminates +- errors
                        if c < 0 and a > 0 or a > 0 and c >= 0 and b < 0 or a < 0 and c < 0 and b > 0:
                            z = -z
                        
                        if w == 1:
                            x = ""
                        elif w == -1:
                            x = "-"
                        else:
                            x = str(w)

                        if a//factrd == 1:
                            y = ""
                        elif a//factrd == -1:
                            y = "-"
                        else: 
                            y = str(a//factrd)

                        if z < 0:
                            z = -z
                            plus = " - "
                        else:
                            plus = " + "
                        if f//factrd < 0:
                            f = -f
                            plus2 = " - "
                        else:
                            plus2 = " + "
                        print ("(" + x +"x" + plus + str(z) + ") (" + y + "x" + plus2 + str(f//factrd) + ")")
                        break
                else:
                    pass
            if prime == True:
                print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is prime")
            ifs()
        
        if cmnd == "manual":
            manual()
            ifs()

        if cmnd == "directix":
            print (drctx)
            ifs()
        

        if cmnd == "reset":
            program()
        
        if cmnd == "exit":
            exit()

        else:
            print ("not a command")
            ifs()
    
    manual()
    ifs()
    
program()
