import math
print("----------------------Reference your equation sheet and use it as an index to find what you need----------------------")
EquationType = input("Pick an equation type to see more equations:\n 1. Mechanics\n 2. Geometry\n")

if EquationType == "1":
    MechanicsEquations = input("Pick an equation to solve for:\n 1. Vf = Vi + at\n 2. ΔX = ((Vf + Vi)/2)t\n 3. Vit + 1/2at^2\n 4. V^2 = Vi^2 + 2aΔX\n")
    if MechanicsEquations == "1":
        Vi = int(input("Ok, what is the initial Velocity?\n"))
        a = int(input("Ok, what is acceleration?\n"))
        t = int(input("Ok, what is time?\n"))
        Vf = Vi + (a*t)
        print("Ok, the final velocity is " + str(Vf) + "m/s")
    elif MechanicsEquations == "2":
        Vf = int(input("Ok, what is the final Velocity?\n"))
        Vi = int(input("Ok, what is the initial Velocity?\n"))
        t = int(input("Ok, what is the time?\n"))
        ΔX = ((Vf + Vi)/2)*t
        print("Ok, the displacement is " + str(ΔX) + "m")
    elif MechanicsEquations == "3":
        Vi = int(input("Ok, what is the initial Velocity?\n"))
        a = int(input("Ok, what is the acceleration?\n"))
        t = int(input("Ok, what is the time?\n"))
        temp = ((a/2)*t)
        ΔX = Vi*t + temp*temp
        print("Ok, the displacement is " + str(ΔX) + "m")
    elif MechanicsEquations == "4":
        Vi = int(input("Ok, what is the initial Velocity?\n"))
        a = int(input("Ok, what is the acceleration?\n"))
        ΔX = int(input("Ok, what is the displacement?\n"))
        Vf = math.sqrt((Vi*Vi + ((2*(a*ΔX)))))
        print("Ok, the final velocity is " + str(Vf) + "m/s")
    elif MechanicsEquations != "1" or "2" or "3" or "4":
        print("Pick the right number loser")
elif EquationType == "2":
    GeoShapes = input("Pick a Shape to solve for to solve for:\n 1. Rectangle\n 2. Triangle\n 3. Circle\n 4. Rectangular Solid\n 5. Cylinder\n 6. Sphere\n 7. Right Triangle\n")
    pi = 3.1415926535898
    if GeoShapes == "1":
        RectangleEquations = input("Pick an equation to solve for to solve for:\n 1. Area\n")
        if RectangleEquations == "1":
            b = int(input("What is the base?\n"))
            h = int(input("What is the height?\n"))
            a = b*h
            print("The area is " + str(a) + "u^2")
    elif GeoShapes == "2":
         TriEquations = input("Pick an equation to solve for to solve for:\n 1. Area\n")
         if TriEquations == "1":
            b = int(input("What is the base?\n"))
            h = int(input("What is the height?\n"))
            a = (b*h)/2
            print("The area is " + str(a) + "u^2")
    elif GeoShapes == "3":
        CircleEquations = input("Pick an equation to solve for to solve for:\n 1. Area\n 2. Circumference\n")
        if CircleEquations == "1":
            r = int(input("What is the radius?\n"))
            a = (pi)*(r*r)
            print("The area is " + str(a) + "u^2")
        elif CircleEquations == "2":
            r = int(input("What is the radius?\n"))
            c = 2*pi*r
            print("The Circumference is " + str(c) + "u")
    elif GeoShapes == "4":
        RSEquations = input("Pick an equation to solve for to solve for:\n 1. Volume\n")
        if RSEquations == "1":
            l = int(input("What is the length?\n"))
            w = int(input("What is the width?\n"))
            h = int(input("What is the height?\n"))
            v = l*w*h
            print("The Volume is " + str(v) + "u^3")
    elif GeoShapes == "5":
        Cylinderquations = input("Pick an equation to solve for to solve for:\n 1. Volume\n 2. Surface Area\n")
        if Cylinderquations == "1":
            h = int(input("What is the height?\n"))
            r = int(input("What is the radius?\n"))
            v = pi*(r*r)*h
            print("The Volume is " + str(v) + "u^3")
        elif Cylinderquations == "2":
            h = int(input("What is the height?\n"))
            r = int(input("What is the radius?\n"))
            s = 2*(pi*r*h) + 2*(pi*(r*r))
            print("The Surface Area is " + str(s) + "u^2")
    elif GeoShapes == "6":
        SphereEquations = input("Pick an equation to solve for to solve for:\n 1. Volume\n 2. Surface Area\n")
        if SphereEquations == "1":
            r = int(input("What is the radius?\n"))
            v = (4/3)*pi*(r*r*r)
            print("The Volume is " + str(v) + "u^3")
        if SphereEquations == "2":
            r = int(input("What is the radius?\n"))
            s = 4*pi*(r*r)
            print("The Surface Area is " + str(s) + "u^2")
    elif GeoShapes == "7":
        RightTEquations = input("Pick an equation to solve for to solve for:\n 1. C^2\n sinθ, cosθ, tanθ is too much work so screw off\n")
        if RightTEquations == "1":
            a = int(input("What is the length of side a?\n"))
            b = int(input("What is the length of side b?\n"))
            c = math.sqrt((a*a)+(b*b))
            print("The third side has a length of " + str(c) + "u")
    elif GeoShapes != "1" or "2" or "3" or "4" or "5" or "6" or "7":
        print("You're Weird")
elif EquationType != "1" or "2":
    print("I hate you")