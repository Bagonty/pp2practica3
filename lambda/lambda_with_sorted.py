# Using lambda with sorted()

students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]
# Sort by second element (score)
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)
