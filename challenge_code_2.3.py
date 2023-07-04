years_days_90 = 90 * 365
years_weeks_90 = 90 * 52
years_months_90 = 90 * 12

year_days = 365
year_weeks = 52
year_months = 12

age = int(input("What is your current age?: "));

days_so_far = (age * year_days);
weeks_so_far = (age * year_weeks);
months_so_far = age * year_months;

print(f"Based on your current age, you have lived so far:{days_so_far} days, {weeks_so_far} weeks and {months_so_far} months ");

last_days = years_days_90 - days_so_far
last_weeks = years_weeks_90 - weeks_so_far
last_months = years_months_90 - months_so_far

print(f"The days that have been left are: {last_days}, the weeks that have been left are: {last_weeks} and the months that have been left are: {last_months}");