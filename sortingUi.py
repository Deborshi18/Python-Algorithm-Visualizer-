'''
Sorting Algorithm Visualizer 
Python, tkinter module
---Debarshi Raj Basumatary

'''





from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort

root=Tk()
root.title(' Algorithm Visualizer')
root.maxsize(900,600)
root.config(bg='#2B2B52')
#variables
selected_alg=StringVar()
data=[]

#functions




def drawData(data,colorArray):
	canvas.delete('all')
	c_height=600
	c_width=600
	x_width=c_width/(len(data)+1)
	offset=30
	spacing=10
	normalizedData=[i/max(data) for i in data]
	for i, height in enumerate(normalizedData):
		x0=i*x_width+offset+spacing
		y0=c_height-height*340

		x1=(i+1)*x_width+offset
		y1=c_height

		canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
		canvas.create_text(x0+4,y0,anchor=SW,text=str(data[i]))
	root.update_idletasks()	

def Generate():
	global data

	minVal=int(minEntry.get())
	maxVal=int(maxEntry.get())
	size=int(sizeEntry.get())
	data=[]
	for _ in range(size):
		data.append(random.randrange(minVal,maxVal+1))

	drawData(data,['red' for x in range(len(data))])

def StartAlgorithm():
	global data
	if not  data: return

	if algMenu.get()=='Quick Sort':
		quick_sort(data,0,len(data)-1,drawData,speedScale.get())
		drawData(data,['green' for x in range(len(data))])
	elif algMenu.get()=="Bubble Sort":
		bubble_sort(data,drawData,speedScale.get())
	elif algMenu.get()=="Merge Sort":
		merge_sort(data,drawData,speedScale.get())
	elif algMenu.get()=="Insertion Sort":
		insertion_sort(data,drawData,speedScale.get())
	drawData(data,['green' for x in range(len(data))])

#frame 

UI_frame = Frame(root,width=200,height=600,bg='grey')
UI_frame.grid(row=0,column=0,padx=10,pady=5)

canvas=Canvas(root,width=600,height=600,bg='#DAE0E2')
canvas.grid(row=0,column=1,padx=10,pady=5)


#user interface menu
#column[0]

Label(UI_frame,text="Algorithm:",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)
algMenu=ttk.Combobox(UI_frame,textvariable=selected_alg,values=['Bubble Sort','Merge Sort','Quick Sort','Insertion Sort'])
algMenu.grid(column=0,row=1,pady=5,padx=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=2, column=0, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=6, column=0, padx=5, pady=5)

sizeEntry=Scale(UI_frame,from_=3, to=25,resolution=1,orient=HORIZONTAL,label="Data Size")
sizeEntry.grid(row=3,column=0,padx=5,pady=5)

minEntry=Scale(UI_frame,from_=0, to=10,resolution=1,orient=HORIZONTAL,label="Min Value")
minEntry.grid(row=4,column=0,pady=5,padx=5)

maxEntry=Scale(UI_frame,from_=10,to=100,resolution=1,orient=HORIZONTAL,label="Max Value")
maxEntry.grid(row=5,column=0,padx=5,pady=5)

Button(UI_frame,text="Generate",command=Generate,bg='#019031').grid(row=7,column=0)
#Button(UI_frame,text="Info",command=info2,bg='white').grid(row=8,column=0)



root.mainloop()