# Define the lists of students
allowed_students = ["Alice", "Bob", "Charlie", "David", "Eve"]
denied_students = ["Oliver", "Patricia", "Quinn", "Rachel", "Sam"]

# Define a dictionary to store student scores
student_scores = {}

# Define a function to check if a student is allowed to write the exam
def can_write_exam(student):
  if student in allowed_students:
    return True
  elif student in denied_students:
    return False
  else:
    return "Student not found"

# Define a function to administer the exam
def administer_exam(student):
  if can_write_exam(student):
    score = input(f"{student}, please enter your score: ")
    student_scores[student] = score
    print(f"Exam submitted successfully, {student}!")
  else:
    print(f"Sorry, {student}, you are not allowed to write the exam.")

# Define a function to view student scores
def view_scores():
  print("Student Scores:")
  for student, score in student_scores.items():
    print(f"{student}: {score}")

# Test the functions
students = ["Alice", "Oliver", "Bob", "Quinn", "Eve", "Sam", "John"]
for student in students:
  result = can_write_exam(student)
  print(f"{student} can write the exam: {result}")

administer_exam("Alice")
administer_exam("Oliver")
view_scores()