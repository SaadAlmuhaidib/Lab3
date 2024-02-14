numbers = []

# Input 10 values into the list
for i in range(10):
    value = int(input(f"Enter value {i+1}: "))
    numbers.append(value)

# Find the largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

# Display the largest number
print("The largest number is:", largest)