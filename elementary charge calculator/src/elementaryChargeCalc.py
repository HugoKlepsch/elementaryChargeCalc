import math



def printAvgDevs(avgDevArray):
	for index in range(len(avgDevArray)):
		print "Charge Const: 	", avgDevArray[index][1], "Average deviation: 	", avgDevArray[index][0], "%"

def bubbleSort(avgDevArray):
	keepGoing = True
	while(keepGoing):
		keepGoing = False
		for ind in range(1, len(avgDevArray)):
			after = avgDevArray[ind][0]
			before = avgDevArray[ind - 1][0]
			if (after < before):
				keepGoing = True
				temp = avgDevArray[ind]
				avgDevArray[ind] = avgDevArray[ind - 1] 
				avgDevArray[ind - 1] = temp 
	return avgDevArray

def calcDev(x):
	x = x - math.floor(x)
	if(x < 0.5):
		return (x * 100)
	else:
		return ((1 - x) * 100)
	
def calcX(charge, elem):
	return charge / elem
	
def calcAvgDev(devArray):
	sum = 0.0
	for i in devArray:
		sum += i
	return sum / len(devArray)

def main():
	global elem
	charges = [3.374, 1.585, 3.108, 5.007, 1.687, 3.186]
	avgDevArray = []
	for i in range(1000):
		elem = 1 + (float(i) / 1000)
		devArray = []
		for chargeInd in range(len(charges)):
			x = calcX(charges[chargeInd], elem)
			devArray.append(calcDev(x))
		avgDev = calcAvgDev(devArray)
		avgDevArray.append([avgDev, elem])
	avgDevArray = bubbleSort(avgDevArray)
	printAvgDevs(avgDevArray)
		


main()