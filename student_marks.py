students = {
    "Anas": 85,
    "Rahul": 72,
    "Aman": 90,
    "Priya": 65,
    "Sara": 95
}

print("STUDENT MARKS ANALYSIS")
print("----------------------")

for name, marks in students.items():
    print(name, ":", marks)

# Calculate total and average

total = sum(students.values())
average = total / len(students)

print("\nTotal Marks:", total)
print("Average Marks:", average)

# Find highest and lowest marks

highest = max(students.values())
lowest = min(students.values())

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Check pass or fail

print("\nSTUDENT RESULTS")
print("----------------")

for name, marks in students.items():
    if marks >= 40:
        print(name, ":", "PASS")
    else:
        print(name, ":", "FAIL")
