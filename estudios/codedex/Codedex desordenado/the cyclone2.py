
height=int(input("whats your height?: "))
credits=int(input("how many credits do you have?: "))
print("you with a tall person?: ")
tall_person=int(input("1 for yes, 2 for no "))

if  height >= 137 and credits >= 10:
    print("Enjoy your ride")
elif height < 137 > 100 and credits >= 10 and tall_person == 1:
    print("enjoy your ride")
elif height < 137 > 100 and credits >= 10 and tall_person == 2:
    print("You're not tall enough for this ride yet")
elif  height >137 and credits < 10:
    print("you dont have enough credits for this ride")
elif height < 137 and credits < 10:
    print("you dont have enough credits for this ride")
elif height <   137 and credits <   10:
    print("you dont have enough credits")
elif height > 137 and credits < 10:
    print ("you dont have enough credits")
else:
    print("somethink went wrong")