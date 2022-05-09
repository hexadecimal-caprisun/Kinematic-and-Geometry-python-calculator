import math
print("----------------------Reference your equation sheet and use it as an index to find what you need----------------------")
print("PLEASE PUT ALL VALUES IN THEIR RELEVANT UNITS, CONVERT UNITS BEFORE PLUGGING THEM IN")
EquationType = input("Pick an equation type to see more equations:\n 1. Mechanics\n 2. Electricity\n 3. Geometry\n")
if EquationType == "1":
    MechanicsEquationType = input("Pick a type of Mechanic Equation:\n 1. Kinematics\n 2. Test\n ")
    if MechanicsEquationType == "1":
        KinematicEquations = input("Pick an equation to solve for:\n 1. Vf = Vi + at\n 2. ΔX = ((Vf + Vi)/2)t\n 3. Vit + 1/2at^2\n 4. V^2 = Vi^2 + 2aΔX\n")
        if KinematicEquations == "1":
            Vi = int(input("Ok, what is the initial Velocity?\n"))
            a = int(input("Ok, what is acceleration?\n"))
            t = int(input("Ok, what is time?\n"))
            Vf = Vi + (a*t)
            print(f"Ok, the final velocity is {Vf}m/s")
        elif KinematicEquations == "2":
            Vf = int(input("Ok, what is the final Velocity?\n"))
            Vi = int(input("Ok, what is the initial Velocity?\n"))
            t = int(input("Ok, what is the time?\n"))
            ΔX = ((Vf + Vi)/2)*t
            print(f"Ok, the displacement is {ΔX}m")
        elif KinematicEquations == "3":
            Vi = int(input("Ok, what is the initial Velocity?\n"))
            a = int(input("Ok, what is the acceleration?\n"))
            t = int(input("Ok, what is the time?\n"))
            temp = a/2
            ΔX = Vi*t + temp*(t*t)
            print(f"Ok, the displacement is {ΔX}m")
        elif KinematicEquations == "4":
            Vi = int(input("Ok, what is the initial Velocity?\n"))
            a = int(input("Ok, what is the acceleration?\n"))
            ΔX = int(input("Ok, what is the displacement?\n"))
            Vf = math.sqrt((Vi*Vi + ((2*(a*ΔX)))))
            print(f"Ok, the final velocity is {Vf}m/s")
        elif KinematicEquations != "1" or "2" or "3" or "4":
            print("Pick the right number loser")
    elif MechanicsEquationType == "2":
        print("test")
elif EquationType == "2":
    ElectricEquationType = input("Pick a type of Electric Equation:\n 1. Coulomb's Law\n 2. Circuits\n")
    if ElectricEquationType == "1":
        k = 89875517923
        q1 = int(input("What is the value of charge 1?\n"))
        q2 = int(input("What is the value of charge 2?\n"))
        r = int(input("What is the distance between the two charges?\n"))
        temp = (q1*q2)/(r*r)
        Fe = k*temp
        print(f"The electric Force is {Fe}N")
    elif ElectricEquationType == "2":
        CircuitEquationType = input("Pick a circuits Equation: 1. ΔV = IR\n 2. R = ρl/A\n 3. I = Δq/Δt\n 4. P = IΔV\n 5. Rseries = R1 + R2...\n 6. Rparallel = 1/R1 + 1/R2...\n")
        if CircuitEquationType == "1":
            i = int(input("What is the current in the circuit?\n"))
            r = int(input("What is the resistance in the circuit?\n"))
            ΔV = i*r
            print(f"The voltage in the circuit is {ΔV}V")
        elif CircuitEquationType == "2":
            ρ = int(input("What is the resitivity of the Material?\n"))
            l = int(input("What is the length of the Material?\n"))
            a = int(input("What is the area of the material?\n?"))
            r = (ρ*l)/a
            print(f"The resitance of the material is {r}Ω")
        elif CircuitEquationType == "3":
            q = int(input("What is the charge?\n"))
            t = int(input("How much time passes?\n"))
            i = q/t
            print(f"The current is {i}A")
        elif CircuitEquationType == "4":
            i = int(input("What is the Current in the circuit?\n"))
            v = int(input("What is the Voltage in the circuit?\n"))
            p = i*v
            print(f"The power in the circuit is {p}W")
        elif CircuitEquationType == "5":
            n = int(input("How many resitors are there?\n"))
            i = 0
            REQ = 0
            while i < n:
                Rtemp = int(input(f"What is the value of resistor {i + 1}?\n"))
                i = i + 1
                REQ = REQ + Rtemp
            print(f"The Total Resistance of the circuit is {REQ}Ω")
        elif CircuitEquationType == "6":
            n = int(input("How many resitors are there?\n"))
            i = 0
            REQ = 0
            while i < n:
                Rtemp = int(input(f"What is the value of resistor {i + 1}?\n"))
                i = i + 1
                REQ = REQ + 1/Rtemp
            REQ = 1/REQ
            print(f"The Total Resistance of the circuit is {REQ}Ω")

elif EquationType == "3":
    GeoShapes = input("Pick a Shape to solve for to solve for:\n 1. Rectangle\n 2. Triangle\n 3. Circle\n 4. Rectangular Solid\n 5. Cylinder\n 6. Sphere\n 7. Right Triangle\n")
    PI = 3.1415926535898
    if GeoShapes == "1":
        RectangleEquations = input("Pick an equation to solve for to solve for:\n 1. Area\n")
        if RectangleEquations == "1":
            b = int(input("What is the base?\n"))
            h = int(input("What is the height?\n"))
            a = b*h
            print(f"The area is {a}u^2")
    elif GeoShapes == "2":
         TriEquations = input("Pick an equation to solve for to solve for:\n 1. Area\n")
         if TriEquations == "1":
            b = int(input("What is the base?\n"))
            h = int(input("What is the height?\n"))
            a = (b*h)/2
            print(f"The area is {a}u^2")
    elif GeoShapes == "3":
        CircleEquations = input("Pick an equation to solve for to solve for:\n 1. Area\n 2. Circumference\n")
        if CircleEquations == "1":
            r = int(input("What is the radius?\n"))
            a = (PI)*(r*r)
            print(f"The area is {a}u^2")
        elif CircleEquations == "2":
            r = int(input("What is the radius?\n"))
            c = 2*PI*r
            print(f"The Circumference is {c}u")
    elif GeoShapes == "4":
        RSEquations = input("Pick an equation to solve for to solve for:\n 1. Volume\n")
        if RSEquations == "1":
            l = int(input("What is the length?\n"))
            w = int(input("What is the width?\n"))
            h = int(input("What is the height?\n"))
            v = l*w*h
            print(f"The Volume is {v}u^3")
    elif GeoShapes == "5":
        Cylinderquations = input("Pick an equation to solve for to solve for:\n 1. Volume\n 2. Surface Area\n")
        if Cylinderquations == "1":
            h = int(input("What is the height?\n"))
            r = int(input("What is the radius?\n"))
            v = PI*(r*r)*h
            print(f"The Volume is {v}u^3")
        elif Cylinderquations == "2":
            h = int(input("What is the height?\n"))
            r = int(input("What is the radius?\n"))
            s = 2*(PI*r*h) + 2*(PI*(r*r))
            print(f"The Surface Area is {s}u^2")
    elif GeoShapes == "6":
        SphereEquations = input("Pick an equation to solve for to solve for:\n 1. Volume\n 2. Surface Area\n")
        if SphereEquations == "1":
            r = int(input("What is the radius?\n"))
            v = (4/3)*PI*(r*r*r)
            print(f"The Volume is {v}u^3")
        if SphereEquations == "2":
            r = int(input("What is the radius?\n"))
            s = 4*PI*(r*r)
            print(f"The Surface Area is {s}u^2")
    elif GeoShapes == "7":
        RightTEquations = input("Pick an equation to solve for to solve for:\n 1. C^2\n sinθ, cosθ, tanθ is too much work so screw off\n")
        if RightTEquations == "1":
            a = int(input("What is the length of side a?\n"))
            b = int(input("What is the length of side b?\n"))
            c = math.sqrt((a*a)+(b*b))
            print(f"The third side has a length of {c}u")
    elif GeoShapes != "1" or "2" or "3" or "4" or "5" or "6" or "7":
        print("You're Weird")
elif EquationType != "1" or "2":
    print("I hate you")
