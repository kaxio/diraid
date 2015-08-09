#!/bin/python

file = open("read.txt","r")
outputFile = open('1','w')
outputFile2 = open('2','w')
cntr = 0
while 1:
	byte1 = file.read(1)
	if byte1 != '':
		if cntr % 2 == 0:
			outputFile.write(byte1)
		if cntr % 2 == 1:
			outputFile2.write(byte1)
		cntr = cntr + 1
	else:
		break

