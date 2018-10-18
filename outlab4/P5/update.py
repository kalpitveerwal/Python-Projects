import json
with open("infinity_stones.json","r") as jsonFile:
    data=json.load(jsonFile)

temp_data=data["Infinity Stones"]

for emp in temp_data:
    emp["Containment Unit"]="Infinity Gauntlet"

with open("update_stones.json","w") as jsonFile:
    json.dump(data, jsonFile)
