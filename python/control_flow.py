# control_flow.py

# Example 1: if/elif/else
num = 7
if num % 2 == 0:
    print(f"{num} is even")
elif num % 3 == 0:
    print(f"{num} is divisible by 3")
else:
    print(f"{num} is neither even nor divisible by 3")

# Example 2: for loop
for i in range(1, 6):
    print(f"Square of {i} is {i*i}")

# Example 3: while loop
count = 0
while count < 3:
    print("Counting:", count)
    count += 1
