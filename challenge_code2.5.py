# The following code is the course's solution

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?: "));
tip = int(input("How much tip would you like to give?:\n10\n12\15"));
people = int(input("How many people to split the bill?: "))

tip_as_percent = tip/100;
total_tip_amount = bill * tip_as_percent;
total_bill = bill + total_tip_amount;
bill_per_person = total_bill / people;
final_amount = round(bill_per_person, 2)

# this format makes the integer into a string
final_amount = "{:.2f}".format(bill_per_person);

print(f"Each person should pay: {final_amount}$")

