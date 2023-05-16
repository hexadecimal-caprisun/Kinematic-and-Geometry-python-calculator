import math
print("----------------------Reference your equation sheet and use it as an index to find what you need----------------------")
print("PLEASE PUT ALL VALUES IN THEIR RELEVANT UNITS, CONVERT UNITS BEFORE PLUGGING THEM IN")
EquationType = input("Pick an equation type to see more equations:\n 1. Mechanics\n 2. Electricity\n 3. Geometry\nUser: ")
if EquationType == "1":
    MechanicsEquationType = input("Pick a type of Mechanic Equation:\n 1. Kinematics\n 2. Test\n ")
    if MechanicsEquationType == "1":
        KinematicEquations = input("Pick an equation to solve for:\n 1. Vf = Vi + at\n 2. ΔX = ((Vf + Vi)/2)t\n 3. Vit + 1/2at^2\n 4. V^2 = Vi^2 + 2aΔX\nUser: ")
        if KinematicEquations == "1":
            Vi = float(input("Ok, what is the initial Velocity?\nUser: "))
            a = float(input("Ok, what is acceleration?\nUser: "))
            t = float(input("Ok, what is time?\nUser: "))
            Vf = Vi + (a*t)
            print(f"Ok, the final velocity is {round(Vf, 3)}m/s")
        elif KinematicEquations == "2":
            Vf = float(input("Ok, what is the final Velocity?\nUser: "))
            Vi = float(input("Ok, what is the initial Velocity?\nUser: "))
            t = float(input("Ok, what is the time?\nUser: "))
            ΔX = ((Vf + Vi)/2)*t
            print(f"Ok, the displacement is {round(ΔX,3)}m")
        elif KinematicEquations == "3":
            Vi = float(input("Ok, what is the initial Velocity?\nUser: "))
            a = float(input("Ok, what is the acceleration?\nUser: "))
            t = float(input("Ok, what is the time?\nUser: "))
            temp = a/2
            ΔX = Vi*t + temp*(t*t)
            print(f"Ok, the displacement is {round(ΔX, 3)}m")
        elif KinematicEquations == "4":
            Vi = float(input("Ok, what is the initial Velocity?\nUser: "))
            a = float(input("Ok, what is the acceleration?\nUser: "))
            ΔX = float(input("Ok, what is the displacement?\nUser: "))
            Vf = math.sqrt((Vi*Vi + ((2*(a*ΔX)))))
            print(f"Ok, the final velocity is {round(Vf,3)}m/s")
        elif KinematicEquations != "1" or "2" or "3" or "4":
            print("Pick the right number loser")
    elif MechanicsEquationType == "2":
        print("test")
elif EquationType == "2":
    ElectricEquationType = input("Pick a type of Electric Equation:\n 1. Coulomb's Law\n 2. Circuits\nUser: ")
    if ElectricEquationType == "1":
        k = 89875517923
        q1 = float(input("What is the value of charge 1?\nUser: "))
        q2 = float(input("What is the value of charge 2?\nUser: "))
        r = float(input("What is the distance between the two charges?\nUser: "))
        temp = (q1*q2)/(r*r)
        Fe = k*temp
        print(f"The electric Force is {round(Fe,3)}N")
    elif ElectricEquationType == "2":
        CircuitEquationType = input("Pick a circuits Equation: 1. ΔV = IR\n 2. R = ρl/A\n 3. I = Δq/Δt\n 4. P = IΔV\n 5. Rseries = R1 + R2...\n 6. Rparallel = 1/R1 + 1/R2...\nUser: ")
        if CircuitEquationType == "1":
            i = float(input("What is the current in the circuit?\nUser: "))
            r = float(input("What is the resistance in the circuit?\nUser: "))
            ΔV = i*r
            print(f"The voltage in the circuit is {round(ΔV,3)}V")
        elif CircuitEquationType == "2":
            ρ = float(input("What is the resitivity of the Material?\nUser: "))
            l = float(input("What is the length of the Material?\nUser: "))
            a = float(input("What is the area of the material?\nUser: "))
            r = (ρ*l)/a
            print(f"The resitance of the material is {round(r,3)}Ω")
        elif CircuitEquationType == "3":
            q = float(input("What is the charge?\nUser: "))
            t = float(input("How much time passes?\nUser: "))
            i = q/t
            print(f"The current is {round(i,3)}A")
        elif CircuitEquationType == "4":
            i = float(input("What is the Current in the circuit?\nUser: "))
            v = float(input("What is the Voltage in the circuit?\nUser: "))
            p = i*v
            print(f"The power in the circuit is {round(p,3)}W")
        elif CircuitEquationType == "5":
            n = float(input("How many resitors are there?\nUser: "))
            i = 0
            REQ = 0
            while i < n:
                Rtemp = float(input(f"What is the value of resistor {i + 1}?\nUser: "))
                i = i + 1
                REQ = REQ + Rtemp
            print(f"The Total Resistance of the circuit is {round(REQ, 3)}Ω")
        elif CircuitEquationType == "6":
            n = float(input("How many resitors are there?\nUser: "))
            i = 0
            REQ = 0
            while i < n:
                Rtemp = float(input(f"What is the value of resistor {i + 1}?\nUser: "))
                i = i + 1
                REQ = REQ + 1/Rtemp
            REQ = 1/REQ
            print(f"The Total Resistance of the circuit is {round(REQ, 3)}Ω")

elif EquationType == "3":
    GeoShapes = input("Pick a Shape to solve for to solve for:\n 1. Rectangle\n 2. Triangle\n 3. Circle\n 4. Rectangular Solid\n 5. Cylinder\n 6. Sphere\n 7. Right Triangle\nUser: ")
    PI = 3.1415926535898
    if GeoShapes == "1":
        RectangleEquations = input("Pick an equation to solve for to solve for:\n 1. Area\nUser: ")
        if RectangleEquations == "1":
            b = float(input("What is the base?\nUser: "))
            h = float(input("What is the height?\nUser: "))
            a = b*h
            print(f"The area is {round(a, 3)}u^2")
    elif GeoShapes == "2":
         TriEquations = input("Pick an equation to solve for to solve for:\n 1. Area\nUser: ")
         if TriEquations == "1":
            b = float(input("What is the base?\nUser: "))
            h = float(input("What is the height?\nUser: "))
            a = (b*h)/2
            print(f"The area is {round(a, 3)}u^2")
    elif GeoShapes == "3":
        CircleEquations = input("Pick an equation to solve for to solve for:\n 1. Area\n 2. Circumference\nUser: ")
        if CircleEquations == "1":
            r = float(input("What is the radius?\nUser: "))
            a = (PI)*(r*r)
            print(f"The area is {round(a, 3)}u^2")
        elif CircleEquations == "2":
            r = float(input("What is the radius?\nUser: "))
            c = 2*PI*r
            print(f"The Circumference is {round(c, 3)}u")
    elif GeoShapes == "4":
        RSEquations = input("Pick an equation to solve for to solve for:\n 1. Volume\nUser: ")
        if RSEquations == "1":
            l = float(input("What is the length?\nUser: "))
            w = float(input("What is the width?\nUser: "))
            h = float(input("What is the height?\nUser: "))
            v = l*w*h
            print(f"The Volume is {round(v, 3)}u^3")
    elif GeoShapes == "5":
        Cylinderquations = input("Pick an equation to solve for to solve for:\n 1. Volume\n 2. Surface Area\nUser: ")
        if Cylinderquations == "1":
            h = float(input("What is the height?\nUser: "))
            r = float(input("What is the radius?\nUser: "))
            v = PI*(r*r)*h
            print(f"The Volume is {round(v, 3)}u^3")
        elif Cylinderquations == "2":
            h = float(input("What is the height?\nUser: "))
            r = float(input("What is the radius?\nUser: "))
            s = 2*(PI*r*h) + 2*(PI*(r*r))
            print(f"The Surface Area is {round(s, 3)}u^2")
    elif GeoShapes == "6":
        SphereEquations = input("Pick an equation to solve for to solve for:\n 1. Volume\n 2. Surface Area\nUser: ")
        if SphereEquations == "1":
            r = float(input("What is the radius?\nUser: "))
            v = (4/3)*PI*(r*r*r)
            print(f"The Volume is {round(v, 3)}u^3")
        if SphereEquations == "2":
            r = float(input("What is the radius?\nUser: "))
            s = 4*PI*(r*r)
            print(f"The Surface Area is {round(s, 3)}u^2")
    elif GeoShapes == "7":
        RightTEquations = input("Pick an equation to solve for to solve for:\n 1. C^2\n sinθ, cosθ, tanθ is too much work so screw off\nUser: ")
        if RightTEquations == "1":
            a = float(input("What is the length of side a?\nUser: "))
            b = float(input("What is the length of side b?\nUser: "))
            c = math.sqrt((a*a)+(b*b))
            print(f"The third side has a length of {round(c, 3)}u")
    elif GeoShapes != "1" or "2" or "3" or "4" or "5" or "6" or "7":
        print("You're Weird")
elif EquationType != "1" or "2":
    print("I hate you")
