height = float(input("Enter your height in m: "));
weight = int(input("Enter your weight in kg: "));

bmi = weight/(height**2);

print("Your MBI is: ", round(bmi, 2));

# print("Your BMI is: ", (bmi // 2))