import time


def partition(data,head ,tail,drawData,timeTick):
	border=head
	pivot=data[tail]

	drawData(data,getColorArray(len(data),head,tail,border,border))
	time.sleep(timeTick)
	for j in range(head,tail):
		if data[j]<pivot:

			drawData(data,getColorArray(len(data),head,tail,border,border))
			time.sleep(timeTick)

			data[border],data[j] = data[j],data[border]
			border+=1

		drawData(data,getColorArray(len(data),head,tail,border,border))
		time.sleep(timeTick)	

	#pivot swapping
	drawData(data,getColorArray(len(data),head,tail,border,border))
	time.sleep(timeTick)

	data[border],data[tail] = data[tail],data[border]
	return border

def quick_sort(data,head,tail,drawData,timeTick):
	if head<tail:
		partitionInd = partition(data,head,tail,drawData,timeTick)

		#left half
		quick_sort(data,head,partitionInd-1,drawData,timeTick)

		#Right half
		quick_sort(data,partitionInd+1,tail,drawData,timeTick)

def getColorArray(dataLen,head,tail,border,currInd,isSwaping=False):
	colorArray=[]

	for i in range(dataLen):
		#base
		if i>=head and i <=tail:
			colorArray.append('gray')
		else:
			colorArray.append('white')

		if i==tail:
			colorArray[i] = 'blue'
		elif i==border:
			colorArray[i]= 'red'
		elif i==currInd:
			colorArray[i]='yellow'
		if isSwaping:
			if i==border or i==currInd:
				colorArray[i]='green'
	return colorArray