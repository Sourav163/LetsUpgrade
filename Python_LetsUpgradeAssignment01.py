# Question :

# Write a Program to calculate the Simple Interest for Bank Customer for Fixed Deposit :
# a) If customer is Female & Senior Citizen, Rate - 8%
# b) If customer is Female & Non Senior Citizen, Rate - 6%
# c) If customer is Male & Senior Citizen, Rate - 7%
# d) If customer is Male & Non Senior Citizen, Rate - 5%

# Answer :

import math

# User Input :
# p = int(input("Enter The Principal Amount :  "))
# t = int(input("Enter The TimePeriod :  "))
# gender = input("Enter Your Gender (Male / Female) :  ")
# seniorCitizen = bool(input("Are you a Senior Citizen (True / False)? :  "))

# Sample :
p = 10000
t = 2
gender = 'Male'
seniorCitizen = True

if (gender == "Female" and seniorCitizen):
    i = 8
elif (gender == "Female" and not seniorCitizen):
    i = 6
elif (gender == "Male" and seniorCitizen):
    i = 7
elif (gender == "Male" and not seniorCitizen):
    i = 5
else:
    print("Invalid Gender or, Senior Citizen Status...")
    exit(0)

si = p*t*i/100
rounded_si = math.ceil(si*100)/100
print("Simple Interest is :  ", rounded_si)
