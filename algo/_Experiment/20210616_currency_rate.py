
def solve(data, queryList):
	if not data:
		return 
	
	dataMap = parseMap(data)
	queryMap = buildQueryMap(dataMap)  # cur -> {cur -> float} 
	result = parseQuery(queryList)

	return result

def parseMap(data)
	dataMap = {}  #cur -> {cur -> float}
	for cur1, cur2, rate in data: #
		if cur1 not in dataMap:
			dataMap[cur1] = {}
		dataMap[cur1][cur2] = rate

		if cur2 not in dataMap:
			dataMap[cur2] = {}
		dataMap[cur2][cur1] = 1 / rate
	return dataMap

# DFS
def buildQueryMap(dataMap):
	def dfs(dataMap):


# BFS 
def buildQueryMap(dataMap):
	queryMap = {}
	for head in dataMap:
		if head in queryMap:
			continue

		deq = collections.deque([(head, 1)])
		while deq:
			curCur, curRate = deq.popleft()
			assert(curCur not in queryMap)

			queryMap[curCur] = (head, curRate)
			for nextCur, nextRate in map[curCur].items():
				if nextCur in queryMap:
					continue
				pathRate = curRate * nextRate
				deq.append((nextCur, pathRate))
				
				#queryMap[nextCur] = (head, pathRate)
	return queryMap

def parseQuery():
	result = []
	for cur1, cur2 in queryList: 
		if queryMap[cur1][0] == queryMap[cur2][0]:
			finalRate = queryMap[cur2][1] / queryMap[cur1][1]
			result.append(finalRate)
		else:
			result.append(-1)
	return result 