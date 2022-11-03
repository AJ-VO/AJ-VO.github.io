from utils import *

with open("jsons/results.json", "r", encoding='utf8') as f:
    resultsData = json.load(f)

resultsData.sort(reverse=True, key=lambda x: x["msDate"])

with open("jsons/results.json", "w", encoding='utf-8') as fp:
    json.dump(resultsData, fp, indent=4)
