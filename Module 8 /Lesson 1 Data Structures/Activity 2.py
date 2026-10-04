classmates = ["Aarav", "Aanya", "Aditya", "Anaya", "Arjun"]
print("Class List:", classmates)

print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three students:", classmates[:3])

classmates.append("Roy")
print("\nAfter adding Roy:", classmates)
classmates.remove("Aanya")
print("After removing Aanya:", classmates)
classmates.sort()
print("Sorted Alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)

teachers = {"name": "Mr. Sharma", "subject": "Python", "experience": 5}
print("\nTeacher Profile:", teachers)

print("Subject:", teachers["subject"])
print("Experience:", teachers.get("experience", "Not found"))

teachers["experience"] = 6
teachers["email"] = "sharma@school.com"
print("Updated Teacher Profile:", teachers)

roll_numbers = (1, 2, 3, 4, 5)
names = ("Aarav", "Aanya", "Aditya", "Anaya", "Arjun")
student_directory = dict(zip(roll_numbers, names))  
print("\nStudent Directory:", student_directory)
print("Student at roll number 3:", student_directory[3])