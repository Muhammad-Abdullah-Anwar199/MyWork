import json

data = ["pf" , "oop" , "DSA"]

with open("data.json" , "w") as file:
    json.dump(data , file , indent=4)

with open("data.json" , "r") as file:
    json.load(file)

data.append("python")

with open("data.json" , "w") as file:
    json.dump(data , file , indent=4)

with open("data.json" , "r") as f:
    me = json.load(f)

result = [s for s in me if s == "python1"]
print(result)