# Autor: jossava
import sys

def map(k,v,c): # k: categoría de orden, v: que quiero de la categoría, c: promedio o sumatoria ?
# ---------->>>>> MAPPER <<<<<-----------------
	file = open(sys.argv[1], 'r')
	auxOutMap = {}
	outMap = {}
	for line in file:
		line = line.split(",")
		#print line
		second = [int(line[v]),1]
# ---------->>>>> REDUCER <<<<<-----------------
		if not line[k] in auxOutMap:
			if not c:
				auxOutMap[line[k]]=second
			else:
				auxOutMap[line[k]]=[1,1]
		else:
			if not c:
				auxOutMap[line[k]][0]+=second[0]
				auxOutMap[line[k]][1]+=second[1]
			else:
				auxOutMap[line[k]][0]+=1
	for i in auxOutMap:
		outMap[i]=auxOutMap[i][0]/auxOutMap[i][1]
	print outMap
	file.close()

map(1,0,True)