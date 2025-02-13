students = {
    "John": {"math": 85, "science": 90, "english": 78},
    "Alice": {"math": 92, "science": 88, "english": 95},
}

# Calculate average marks for each student
for student, subjects in students.items():
    avg_marks = sum(subjects.values()) / len(subjects)
    print(f"{student}'s average marks: {avg_marks:.2f}")
