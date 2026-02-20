with open("names.txt" , 'r') as file:
    for line in sorted(file ,key= lambda x : 5,reverse=True):
        print(line.strip())
