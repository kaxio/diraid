file1 = open("1","r")
file2 = open("2","r")
cntr = 0
fileOut = open("out.txt","w")
while 1:	
		if cntr % 2 == 0:
			out = file1.read(1)
			if out != '':
				fileOut.write(out)
			else:
				break
		else:
			out = file1.read(1)
			if out != '':
				fileOut.write(out)
			else:
				break

