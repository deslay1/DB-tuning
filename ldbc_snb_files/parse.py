import json

results = json.load(open("results/LDBC-SNB-results.json"))
with open('results.txt', 'a') as f:
    f.write(str(round(results['throughput'],2)) + ', ')