# 🚨 Don't change the code below 👇
two_digit_number = int(input("Type a two digit number: "))
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

tens_digit, ones_digit = divmod(two_digit_number, 10)

"""Here's an alternative way without using Python's divmod function"""
# tens_digit = two_digit_number // 10;
# ones_digit = two_digit_number % 10;

digit_sum = tens_digit + ones_digit;

print("The sum of the two numbers is: ", digit_sum);
