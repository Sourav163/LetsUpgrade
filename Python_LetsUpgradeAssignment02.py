# Write a Python to count number of odd and even number from the series of the list:
# [2, 3, 4, 55, 56, 78, 75, 69, 66, 101, 100]

# Initializing :
li = [2, 3, 4, 55, 56, 78, 75, 69, 66, 101, 100]
co, ce = 0, 0

# Counting the number of evens and odds in li :
for i in li:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1

# Displaying :
print(li)
print(f"{ce} even numbers & {co} odd numbers are there in the above given list")
