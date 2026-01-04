# ==============================================

# Task-1: Creating a Dictionary of Student Marks

#===============================================


student_marks = {"Bob":89,"Sneha":98,"Alice":94,"Don":82}
student_name = input("Enter the student's name:").strip().title()

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found")

print("\n=================================")

#===========================================

# Task-2 Demonstrate List Slicing

#===========================================

numbers = [1,2,3,4,5,6,7,8,9,10]
print(f"\nOriginal list: {numbers}")

extracted = numbers[:5]
print(f"Extracted first five elements: {extracted}")

reversed_extracted  = extracted[::-1]
print(f"Reversed extracted element: {reversed_extracted}")