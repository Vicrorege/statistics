def static_info(raw:list):
# init
	middle_find = 0

	max = 0.0
	min = 9999999999999999999999999.9

	FDict = {}
	fashion = []
	maxItemfashion = 0

	median = 0

	output = {"middle":0.0, "scope":0.0, "fashion":[], "median":0.0}
# auto loop
	raw.sort()
	for i in range(len(raw)):
		item = raw[i]
# middle
		middle_find += item
# scope
		if item > max : max = item
		if item<min: min= item
# fashion
		if item in FDict.keys():
			FDict[item] += 1
		else:
			FDict[item] = 1
	for i in range(len(FDict)): 
		if FDict[list(FDict.keys())[i]] > maxItemfashion : maxItemfashion = FDict[list(FDict.keys())[i]]
	if maxItemfashion != 1:
		for i in range(len(FDict)):
			if FDict[list(FDict.keys())[i]] == maxItemfashion :
				
				fashion.append(list(FDict.keys())[i])
	else:
		fashion = None
# median
	if len(raw)%2 == 1:
		median = raw[int(len(raw)/2)]
	else:
		median = (raw[int(len(raw)/2)]+(raw[int(len(raw)/2)-1]))/2

	middle_find = middle_find/len(raw)
	scope = max-min

	output["middle"] = middle_find
	output["scope"] = scope
	output["fashion"] = fashion
	output["median"] = median

	return output

inp = input("Enter number raw:\n")
inpList = inp.split(", ")
outList = []
for i in range(len(inpList)):
	outList.append(int(inpList[i]))
# print(outList)
print(static_info(outList))
# print(static_info())