print("Welcome to the tip calculator!");

bill = float(input("What was the total bill? $:"))

people = int(input("In how many people you want to split?: "));

if people < 0:
    print("That was an invalid input");

tip = int(input("How much tip would you like to give?\n1) 10%\n2) 12%\n3) 15%\n"));

if (tip == 1):
    tip1 = (bill / people) * (10/100);
    total = tip1 + bill
    print(f"Your total amount of your meal plus the tip is: {total}")
    print(f"Your tip is: {tip1}")
elif (tip == 2):
    tip2 = (bill / people) * (12/100);
    total = tip2 + bill
    print(f"Your total amount of your meal plus the tip is: {total}")
    print(f"Your tip is: {tip2}")
elif (tip == 3):
    tip3 = (bill / people) * (15/100);
    total = tip3 + bill
    print(f"You total amount of your meal plus the tip is: {total}")
    print(f"Your tip is: {tip3}")
else:
    print("That was an invalid input");