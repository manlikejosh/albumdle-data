import json


f = open('blerp.json')

# returns JSON object as a dictionary
data = json.load(f)


f.close()


sortedData = sorted(data, key=lambda x: x['title'])

with open('sortedData.json', "w") as file:
    json.dump(sortedData, file, indent=4)
