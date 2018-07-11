print("Lean body mass calculator\n")

weight = input("What is your weight in lbs? ")

print("""
    If you aren't sure about what your body
    fat percentage is, go online and search
    images of different bodyfat percentages
    and use the percentage that looks closest
    to the fat on your body. 
    If you want to be very accurate then buy a
    fat caliper, it's easy and cheap to use.
    """)

fat = input("What is your bodyfat percentage (Number only)? ")

# procedure to do the calculations
def calculate(weight, bodyfat):
    lean_per = 100 - int(bodyfat)
    lean_dec = lean_per/100
    lean_weight = int(weight)*lean_dec
    fat_weight = int(weight)*(int(bodyfat)/100)

    
    print("\nYour lean body mass is: {0} lbs.".format(lean_weight))
    
    x = input("\nDo you want to know how much lbs of bodyfat you have? Y or N? ")
    if x.lower() == 'y':
        print("\nYour fat body mass is: {0} lbs.".format(fat_weight))
    else:
        exit()

calculate(weight, fat)

