import time

def insertion_sort(data,drawData,timeTick):

	for i in range(1,len(data)):

		key=data[i]
		
	
		j=i-1
		drawData(data,getColorArray(data,i,j))
		time.sleep(timeTick)
		while(j>=0 and key < data[j]):
			data[j+1] = data[j]
			j-=1
			drawData(data,getColorArray(data,i,j))
			time.sleep(timeTick)
		data[j+1] = key
	drawData(data,['green' for x in range(len(data))])

def getColorArray(data,x,y):
	colorArray=[]
	for i in range(len(data)):
		if i == x :
			colorArray.append('blue')
		elif i==y:
			colorArray.append('green')
		else:
			colorArray.append('red')
	return colorArray

