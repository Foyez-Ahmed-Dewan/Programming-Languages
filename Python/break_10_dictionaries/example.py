# ### example - 1: Given a dictionary of student marks. Create a new dictionary called `students_grades` that contains the student names as keys and their grades as values. if the student got 90 or above, the grade is "A". if the student got 80 or above, the grade is "A-". if the student got 70 or above, the grade is "B". if the student got 60 or above, the grade is pass.
student_marks = {"Foyez": 90, "Ahmed": 80, "Dewan": 70, "Yoo": 60, "Mohammed": 71, "Ali": 62, "Ahad": 82, "yoo" : 76 }

student_grades = {}

for key in student_marks:
  if (student_marks[key] >= 90):
    student_grades[key] = "A"
  elif (student_marks[key] >= 80):
    student_grades[key] = "A-"
  elif (student_marks[key] >= 70):
    student_grades[key] = "B"
  else:
    student_grades[key] = "Pass"

print(student_grades)
#output: {'Foyez': 'A', 'Ahmed': 'A-', 'Dewan': 'B', 'Yoo': 'Pass', 'Mohammed': 'B', 'Ali': 'Pass', 'Ahad': 'A-', 'yoo': 'B'}

## break - 19####
#### Nesting Lists and Dictionaries #####
# # syntax : {
#   key : [list],
#   key : {dict}
# }

## Nested Dictionary
student = {
  "name" : "Foyez",
  "subjects" : {
    "chem" : 80.0,
    "math" : 100,
    "phy" : "one hundread",
    "bio" : False
  }
}

# print (student["name"])    #output: Foyez
# print (student["subjects"])  #output: `subjects` dictionary
# print (student["subjects"]["bio"]) #output: False
# print (student["subjects"]["phy"]) #output: one hundread