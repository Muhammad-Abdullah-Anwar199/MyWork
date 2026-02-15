def saveToFile(name , roll):
    #write the student data in json
    student = [{name:roll}]
    with open ("student.json" ,"r") as file:
        if any(student[i][name] for i in student):
            print("Already Exist")
        else:
            