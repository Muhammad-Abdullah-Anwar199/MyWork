students = []
with open("names.csv" , "r") as file:
    for line in file:
        name , house = line.strip().split(",") #split gives back a list
        student = {"name": name , "house" : house}
        students.append(student)
for stu in sorted(students , key=lambda student:student['name']):
    print(stu['name'])

