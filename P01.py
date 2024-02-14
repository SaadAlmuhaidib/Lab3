employee_data = {}

while True:
    name = input("Enter the name of the employee (or 'no' to exit): ")
    if name.lower() == "no":
        break

    salary = float(input("Enter the salary of the employee: "))

    employee_data[name] = salary

print("\nEmployee data:")
for name, salary in employee_data.items():
    print(f"{name}: {salary}")