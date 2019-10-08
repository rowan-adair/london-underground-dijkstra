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

if __name__ == '__main__':
	test = createdictionary()
	for i in test:
		# Line Name
		print("\n\n" + i)
		# All Stops
		print(test[i])	


