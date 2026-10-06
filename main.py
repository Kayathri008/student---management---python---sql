students = []
def add_student(name, dept, marks):
    students.append({"name": name, "dept": dept, "marks": marks})
    print(f"Added {name}")

add_student("Arun", "CS", 85)
add_student("Priya", "CS", 92)
print("All Students:", students)
