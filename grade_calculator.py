print("Grade Calculator")

grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))

average = (grade1 + grade2 + grade3) / 3

print(f"Average Grade: {average:.2f}")

if average >= 90:
    print("Letter Grade: A")
elif average >= 80:
    print("Letter Grade: B")
elif average >= 75:
    print("Letter Grade: C")
else:
    print("Letter Grade: F")
