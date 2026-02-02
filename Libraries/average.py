import statistics

list = statistics.mean([100,200,300,50,50,70,60])
print(f"{list:.2f}")

#the first i is that going to be added in the list
evens = [i*i for i in range(10) if i%2 == 0]
print(evens)

i = input("Input: ")
print(i.lower())

new = input("Input: ")
print(new.replace(" ","..."))

def faces(str):
    str = str.replace(":)" , "😔")
    str = str.replace("(:", "😊")
    return str
        
f = faces("HEllo :)")
print(f)