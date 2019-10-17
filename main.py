import dijkstra
import os
import csv

def makeFileKey(filename):
	key = os.path.splitext(filename)[0]
	key = key.replace("_"," ").title()
	return key


def createdictionary():
	lines = {}
	for f in os.listdir('resources'):
		tempList = []
		filepath = 'resources//'+f
		with open(filepath) as csv_file:
			csv_reader = csv.reader(csv_file,delimiter=',')
			line_c = 0
			for row in csv_reader:
				if line_c == 0:
					tempList=row
					line_c = line_c + 1
				else:
					tempList = tempList + row
			filter(None,tempList)
			lines.update({makeFileKey(f):tempList})
	return lines

def extractKeys(dictionary):
	keys = []
	for entry in dictionary:
		keys.append(entry)
	return keys



def defineEdgeWeight(line, first, last) :
	a = 0
	b = 0
	for index, check in enumerate(line, start = 1):
		if check == first: 
			a = index
		elif check == last:
			b = index
	if a == 0 or b == 0: 
		print("One of the stations isn't on this line.")
	else:
		if b > a : 
			v = b - a
		elif a > b : 
			v = a - b
	return v	

def commonStations(line1, line2): 
	result = []
	for station in line1: 
		for station_check in line2: 
			if station == station_check: 
				result.append(station)
	return result 


def lineConnections(train_line):
	graph = {}
	for a in train_line:
		connected = {}
		for b in train_line:
			if a != b:
				connected_stations = commonStations(train_line[a],train_line[b])
				if len(connected_stations) > 0:
					connected.update({b:connected_stations})
		graph.update({a:connected})
	return graph	


if __name__ == '__main__':
	test = createdictionary()
	for i in test:
		# Line Name
		print("\n\n" + i)
		# All Stops
		print(test[i])	


