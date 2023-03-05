import json
state = []
with open("data.json","r") as f:
    data = json.load(f)
    for i in data:
        if state == [] or i.get("State","") not in state:
            state.append(i['State'])
print(state)
            
