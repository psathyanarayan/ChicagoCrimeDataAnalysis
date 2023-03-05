import json
import matplotlib.pyplot as plt

def plotit():
    crimes = {}
    d = {}
    ls = []
    with open("data.json","r") as f:
        data = json.load(f)
        for i in data:
            jsonData = []
            for j in i['Data']:
                d = i['Data'].get("Totals")
            if crimes == {} or i.get("State","") not in crimes:
                crimes[i['State']] = d['Property'].get("All")

    state = list(crimes.keys())
    total = list(crimes.values())
    plt.bar(range(len(crimes)), total, tick_label=state)
    plt.xticks(rotation=-90, ha='right')
    plt.savefig('graph.png')
