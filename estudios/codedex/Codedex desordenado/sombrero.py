
print("wich house do you belong to?: ")
print("🦁 Gryffindor")
print("🦅 Ravenclaw")
print("🦡 Hufflepuff")
print("🐍 Slytherin")

Gryffindor  =  0
Ravenclaw  =  0
Hufflepuff  =  0
Slytherin  =  0

print("A) do you like dawn or dusk?: ")
print("1 for dawn")
print ("2 for dusk")
A   =   int(input(""))
if A == 1:
    Gryffindor =    1
if A == 1:
    Ravenclaw =     1
elif A == 2:
    Hufflepuff =    1
elif A == 2:
    Slytherin =     1
else:
    print("wrong input.")

    

print("B) When Im dead, I want people to remember me as: ")
print("1 the good")
print("2 the great")
print("3 the wise")
print("4 the bold")
B   =   int(input(""))
if B == 1:
    Hufflepuff  +=  2
elif B  ==  2:
    Slytherin   +=   2
elif B  ==  3:
    Ravenclaw   +=   2
elif B  ==  4:
    Gryffindor  +=   2
else:
    print("wrong input.")


print("C) Which kind of instrument most pleases your ear?: ")
print("1 the violin")
print("2 the trumpet")
print("3 the piano")
print("4 the drum")
C   =   int(input(""))
if C == 1:
    Slytherin  +=  4
elif C  ==  2:
    Hufflepuff   +=   4
elif C  ==  3:
    Ravenclaw   +=   4
elif C  ==  4:
    Gryffindor  +=   4
else:
    print("wrong input.")

if      Gryffindor  >   Hufflepuff  and   Ravenclaw     <   Gryffindor  and     Gryffindor  >   Slytherin:
    print("your house is: 🦁 Gryffindor")
elif    Hufflepuff  >   Gryffindor  and   Hufflepuff    >   Ravenclaw   and     Hufflepuff  >   Slytherin:
    print("your house is: 🦡 Hufflepuff")
elif    Ravenclaw   >   Gryffindor  and   Hufflepuff    <   Ravenclaw   and     Ravenclaw   >   Slytherin:
    print("your house is: 🦅 Ravenclaw")
elif    Slytherin   >   Gryffindor  and   Ravenclaw     <   Slytherin   and     Slytherin   >   Hufflepuff:
    print("your house is: 🐍 Slytherin")
else:
    print(Gryffindor)
    print(Hufflepuff)
    print(Slytherin)
    print(Ravenclaw)

