def fortune():
    import random
    lucky   =   random.randint(1,9)
    if      lucky   ==  1:
        print("Don't pursue happiness, create it.")
    elif    lucky   ==  2:
        print("All things are difficult before they are easy.")
    elif    lucky   ==  3:
        print("The early bird gets the worm, but the second mouse gets the cheese.")
    elif    lucky   ==  4:
        print("If you eat something and nobody sees you eat it, it has no calories.")
    elif    lucky   ==  5:
        print("Someone in your life needs a letter from you.")
    elif    lucky   ==  6:
        print("Don't just think. Act!")
    elif    lucky   ==  7:
        print("Your heart will skip a beat.")
    elif    lucky   ==  8:
        print("The fortune you search for is in another cookie.")
    else:
        print("Help! I'm being held prisoner in a Chinese bakery!")
    
fortune()