import student

def showStudent(aStudent):
  print('')
  print("Student Name: " + aStudent.name)
  for category in aStudent.categories:
    print("Category: " + category.name + ' has Weight of: ' + str(category.weight) + '%')

studentName = input("Enter the Student's Name: ")
theStudent = student.Student(studentName)

print('')
keepGoing = True
while keepGoing:
  categoryName = input("Please Enter a Grade Category (DONE): ")
  if (categoryName.lower() == 'done'):
    keepGoing = False
  else:
    theStudent.addCategory(categoryName)
 
while not theStudent.categoriesAreValid():
  print('')
  print('Enter Weights for Categories (Must add up to 100)')
  for category in theStudent.categories:
    percentage = input('Please Enter the % Weight for ' + category.name + ' ')
    category.setWeight(percentage)
  
keepGoing = True
while keepGoing:
  print('')
  for index, category in enumerate(theStudent.categories):
    print(str(index + 1) + '. Enter: ' + category.name)
  print('R. See the Report Card')
  print('Q. Quit')
  option = input('Choose an Option: ')
  if option.lower() == 'q':
    keepGoing = False
  #else:
    # DO the option



showStudent(theStudent)

