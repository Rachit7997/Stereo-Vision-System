#Sharp_Eye extended....
#algorithm of next generation..
#A perfect content library
import cv2
import numpy as np
import math
import os

#global camera, frame1, frame2, deviation, mouseR, mouseC, originR, originC, destinationR, destinationC, Distance

def Go(mouse_C, mouse_R, new_frame1, new_frame2):
	global mouseC, mouseR, frame1, frame2
	mouseC = mouse_C
	mouseR = mouse_R
	frame1 = new_frame1
	frame2 = new_frame2
	Criteria(frame1[mouseR, mouseC])


	

def Criteria (channel):
	global intense, bg, br, gb, gr, rb, rg, reference
	reference = channel
	if channel[0]>180:
		intense=[1]
		BG=int(channel[0])-int(channel[1])
		BR=int(channel[0])-int(channel[2])
		if BG<0:
			bg=-1
		elif BG>100:
			bg=100
		else:
			bg=1
		if BR<0:
			br=-1
		elif BR>100:
			br=100
		else:
			br=1
	else:
		intense=[0]
	if channel[1]>180:
		intense.append(1)
		GB=int(channel[1])-int(channel[0])
		GR=int(channel[1])-int(channel[2])
		if GB<0:
			gb=-1
		elif GB>=100:
			gb=100
		else:
			gb=1
		if GR<0:
			gr=-1
		elif GR>=100:
			gr=100
		else:
			gr=1
	else:
		intense.append(0)
	if channel[2]>180:
		intense.append(1)
		RB=int(channel[2])-int(channel[0])
		RG=int(channel[2])-int(channel[1])
		if RB<0:
			rb=-1
		elif RB>=100:
			rb=100
		else:
			rb=1
		if RG<0:
			rg=-1
		elif RG>=100:
			rg=100
		else:
			rg=1
	else:
		intense.append(0)
	
#	global deviation
#	if channel[0]>200:
#		deviation=[51]
#	else:
#		deviation=[11]
#	if channel[1]>200:
#		deviation.append(51)
#	else:
#		deviation.append(11)
#	if channel[2]>200:
#		deviation.append(51)
#	else:
#		deviation.append(11)
	Detect()

def Valid(color):
	global validity
	validity=1
	if intense[0]==1:
		if bg==-1:
			if color[0]<=color[1]:
				validity*=1
			else:
				validity*=0
		elif bg==100:
			if (int(color[0])-int(color[1])>=100):
				validity*=1
			else:
				validity*=0
		else:
			#if color[0]>color[1]:
				#validity*=1
			#else:
				#validity*=0
			BG=int(color[0]) - int(color[1])
			referBG =int(reference[0])-int(reference[1])
			if (BG <= referBG+20 and BG >= referBG-20 and BG>0):
				validity*=1
			else:
				validity*=0
				
		
		if (validity==1 and br==-1):
			if color[0]<=color[2]:
				validity*=1
			else:
				validity*=0
		elif (validity==1 and br==100):
			if (int(color[0])-int(color[2])>=100):
				validity*=1
			else:
				validity*=0
		elif (validity==1):
			#if color[0]>=color[2]:
				#validity*=1
			#else:
				#validity*=0
			BR=int (color[0]) - int(color[2])
			referBR=int(reference[0])-int(reference[2])
			if (BR <= referBR+20 and BR >= referBR-20 and BR>0):
				validity*=1
			else:
				validity*=0
	
	elif color[0]>180:
		validity*=0
		
	if (intense[1]==1 and validity==1):
		if gb==-1:
			if color[1]<=color[0]:
				validity*=1
			else:
				validity*=0
		elif gb==100:
			if (int(color[1])-int(color[0])>=100):
				validity*=1
			else:
				validity*=0
		else:
			#if color[1]>=color[0]:
				#validity*=1
			#else:
				#validity*=0
			GB=int(color[1]) - int(color[0])
			referGB=int(reference[1])-int(reference[0])
			if (GB <= referGB+20 and GB >= referGB-20 and GB>0):
				validity*=1
			else:
				validity*=0	
				
		if (gr==-1 and validity==1):
			if color[1]<=color[2]:
				validity*=1
			else:
				validity*=0
		elif (gr==100 and validity==1):
			if (int(color[1])-int(color[2])>=100):
				validity*=1
			else:
				validity*=0
		elif (validity==1):
			#if color[1]>=color[2]:
				#validity*=1
			#else:
				#validity*=0
			GR=int(color[1]) - int(color[2])
			referGR=int(reference[1])-int(reference[2])
			if (GR <= referGR+20 and GR >= referGR-20 and GR>0):
				validity*=1
			else:
				validity*=0
				
	elif color[1]>180:
		validity*=0
		
		
	if (intense[2]==1 and validity==1):
		if rb==-1:
			if color[2]<=color[0]:
				validity*=1
			else:
				validity*=0
		elif rb==100:
			if (int(color[2])-int(color[0])>=100):
				validity*=1
			else:
				validity*=0
		else:
			#if color[2]>=color[0]:
				#validity*=1
			#else:
				#validity*=0
			RB=int(color[2]) - int(color[0])
			referRB=int(reference[2])-int(reference[0])
			if (RB <= referRB+20 and RB >= referRB-20 and RB>0):
				validity*=1
			else:
				validity*=0
		
		if (rg==-1 and validity==1):
			if color[2]<=color[1]:
				validity*=1
			else:
				validity*=0
		elif (rg==100 and validity==1):
			if (int(color[2])-int(color[1])>=100):
				validity*=1
			else:
				validity*=0
		elif (validity==1):
			#if color[2]>=color[1]:
				#validity*=1
			#else:
				#validity*=0
			RG=int(color[2]) - int(color[1])
			referRG=int(reference[2])-int(reference[1])
			if (RG <= referRG+20 and RG >= referRG-20 and RG>0):
				validity*=1
			else:
				validity*=0
	
	elif color[2]>180:
		validity*=0
	
	if (intense[0]+intense[1]+intense[2]==0):
		if (color[0]>=frame1[mouseR, mouseC,0]-21 and color[0]<=frame1[mouseR, mouseC, 0]+21 and color[1]>=frame1[mouseR, mouseC,1]-21 and color[1]<=frame1[mouseR, mouseC, 1]+21 and color[2]>=frame1[mouseR, mouseC,2]-21 and color[2]<=frame1[mouseR, mouseC, 2]+21):
			validity*=1
		else:
			validity*=0
	
	return validity


def Detect():
	global originC, originR, right1, right2, displacement
	r=mouseR
	c=mouseC
	while True:
		#if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		while True:#for c in range(mouseC,640):
#			if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
			if (Valid(frame1[r,c])):
#				if (frame1[r,c+1,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c+1,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c+1,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c+1,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c+1,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c+1,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame1[r,c+1])):
					c+=2
				else:
					r-=1
					break
			else:
				r-=1
				c-=1
				break
#		if  not (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if not (Valid(frame1[r,c])):
		
		#	originR1=r+1
		#	originC1=c
			R=r+1
			C=c
			c+=10
			if c >= 640:
				c=639
			k=0
			for i in range(10):
				c-=1
				for r in range(R-30, R+31):
					if (Valid(frame1[r,c])):
						originR1=r
						originC1=c
						k+=1
						break
				if (k==1):
					break
			break
		else:
			c+=1
	
	r=mouseR
	c=mouseC
	while True:
		while True:
#			if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
			if (Valid(frame1[r,c])):
#				if (frame1[r,c+1,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c+1,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c+1,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c+1,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c+1,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c+1,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame1[r,c+1])):
					c+=2
				else:
					r+=1
					break
			else:
				r+=1
				c-=1
				break
#		if  not (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if not (Valid(frame1[r,c])):
			#originR2=r-1
			#originC2=c
			R=r-1
			C=c
			c+=7
			k=0
			for i in range(10):
				c-=1
				for r in range(R-20, R+20):
					if r>=480:
						r=479
					if (Valid(frame1[r,c])):
						originR2=r
						originC2=c
						k+=1
						break
				if (k==1):
					break
			break
		else:
			c+=1
	
	if originC1>originC2:
		originC=originC1
		originR=originR1
	elif originC2>originC1:
		originC=originC2
		originR=originR2
	else:
		originC=originC1
		originR=originR1
	print "originC1=",originC1
	print "originC2=",originC2
	print "originC=",originC
	print "originR1=",originR1
	print "originR2=",originR2
	print "originR=",originR
	right1=[originR1, originC1]
	right2=[originR2, originC2]
	Determine()

def  Determine():
	global destinationC, destinationR, Distance, displacement
	c=originC
	k=0
	while True:
		if c>0:
			for r in range(originR-2, originR+2):
#				if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame2[r,c])):
					destinationR=r
					destinationC=c
					k=1
					break
			c-=1
		else:
			print "Unpredictable!! Sorry..Check Your Algorithm!"
			break	
		if k==1:
			break
	print "destinationC=",destinationC
	print "destinationR=",destinationR
	deltaR=destinationR-originR
	deltaC=destinationC-originC
	deltaL=math.sqrt((deltaR**2)+(deltaC**2))
	print "deltaC=",deltaC
	print "deltaR=",deltaR
	print "deltaL=",deltaL
	
	displacement=60#20 millimeter
	T=2.47
	L=320*displacement/abs(deltaC)
	Distance=T*L
	print "L=",L
	
	print "Finely the Distance of object from your camera source is %f "%Distance

	Find_Points()


	
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	




	
def Find_Points():
	#Here Right most points have been discovered in the operation of determine
	#Now we need to find out Three/Four more points (top most 2 or 1, left most 2)
	#Left most point...
	global left1, left2, topL, topR
	r=mouseR
	c=mouseC
	while True:
		while True:
#			if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
			if (Valid(frame1[r,c])):
#				if (frame1[r,c-1,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c-1,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c-1,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c-1,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c-1,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c-1,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame1[r,c-1])):
					c-=2
				else:
					r-=1
					break
			else:
				r-=1
				c+=1
				break
#		if  not (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if not(Valid(frame1[r,c])):
			#left1=[r+1, c]
			R=r+1
			C=c
			c-=7
			if c<0:
				c=0
			k=0
			for i in range(10):
				c+=1
				for r in range(R-7, R+8):
					if (Valid(frame1[r,c])):
						left1=[r, c]
						k+=1
						break
				if (k==1):
					break
			break
		else:
			c-=1
	
	r=mouseR
	c=mouseC
	while True:
		while True:
#			if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
			if (Valid(frame1[r,c])):
#				if (frame1[r,c-1,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c-1,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c-1,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c-1,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c-1,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c-1,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame1[r,c-1])):
					c-=2
				else:
					r+=1
					break
			else:
				r+=1
				c+=1
				break
#		if  not (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if not (Valid(frame1[r,c])):
			#left2=[r-1,c]
			R=r-1
			C=c
			c-=7
			if c<0:
				c=0
			k=0
			for i in range(10):
				c+=1
				for r in range(R-7, R+8):
					if r>=480:
						r=479
					if (Valid(frame1[r,c])):
						left2=[r, c]
						k+=1
						break
				if (k==1):
					break
			break
		else:
			c-=1
	
	r=left1[0]
	c=left1[1]
	while True:
		if r==0:
			break;
#		if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if (Valid(frame1[r,c])):
			r-=1
		else:
			for i in range(0,10):
				c+=1
				k=0
#				if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame1[r,c])):
					r-=1
					k+=1
					break
			
			if k==0:
				r+=1
				c-=10
				break
	
	topL=[r,c]
				
	r=right1[0]
	c=right1[1]
	while True:
		if r==0:
			break
#		if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if (Valid(frame1[r,c])):
			r-=1
		else:
			for i in range(0,10):
				c-=1
				k=0
#				if (frame1[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame1[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame1[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame1[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame1[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame1[r,c])):
					r-=1
					k+=1
					break
			
			if k==0:
				r+=1
				c+=10
				break
		
	topR=[r,c]
	print "topL=",topL
	print "topR=",topR
	print "left1=",left1
	print "left2=",left2
	print "right1=",right1
	print "right2=",right2
	
	Find_Distance()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def Find_Distance():
	global dist_L1, dist_L2, dist_R1, dist_R2, dist_TopL, dist_TopR
	#first find distance of "left1" point....
	r=left1[0]+10
	c=left1[1]
	
	while True:
		while True:
#			if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
			if (Valid(frame2[r,c])):
#				if (frame2[r,c-1,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c-1,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c-1,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c-1,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c-1,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c-1,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame2[r,c-1])):
					c-=2
				else:
					r-=1
					break
			else:
				r-=1
				c+=1
				break
#		if  not (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if not (Valid(frame2[r,c])):
			dest_Point=[r+1, c]
			break
		else:
			c-=1
	
	
	deltaR=dest_Point[0]-left1[0]
	deltaC=dest_Point[1]-left1[1]
	deltaL=math.sqrt((deltaR**2)+(deltaC**2))
	T=2.778#2.45
	L=320*displacement/deltaL
	dist_L1=T*L

#fine the distance of left2..
	r=left2[0]+10
	c=left2[1]
	
	while True:
		while True:
#			if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
			if (Valid(frame2[r,c])):
#				if (frame2[r,c-1,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c-1,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c-1,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c-1,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c-1,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c-1,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame2[r,c-1])):
					c-=2
				else:
					r+=1
					break
			else:
				r+=1
				c+=1
				break
#		if  not (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if not (Valid(frame2[r,c])):
			dest_Point=[r-1,c]
			break
		else:
			c-=1
	
	deltaR=dest_Point[0]-left2[0]
	deltaC=dest_Point[1]-left2[1]
	deltaL=math.sqrt((deltaR**2)+(deltaC**2))
	T=2.778
	L=320*displacement/deltaL
	dist_L2=T*L
	
#The dist_R1 is already determined
	dist_R1=Distance
#Find distance  "dist_R2"...
	
	
	c=right2[1]
	k=0
	while True:
		if c>0:
			for r in range(right2[0]-15, right2[0]+16):
#				if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame2[r,c])):
					dest_Point=[r,c]
					k=1
					break
			c-=1
		else:
			print "Unpredictable!! Sorry..Check Your Algorithm!"
			break	
		if k==1:
			break

	deltaR=dest_Point[0]-right2[0]
	deltaC=dest_Point[1]-right2[1]
	deltaL=math.sqrt((deltaR**2)+(deltaC**2))
	T=2.778
	L=320*displacement/deltaL
	dist_R2=T*L
	
#Find the distance of "dist_TopL".......
	r=topL[0]+8
	c=topL[1]

	while True:
#		if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if (Valid(frame2[r,c])):
			c-=1
		else:
			c+=1
			break
	
	while True:
#		if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame2[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if (Valid(frame2[r,c])):
			r-=1
		else:
			for i in range(0,10):
				c+=1
				k=0
#				if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame2[r,c])):
					r-=1
					k+=1
					break
			
			if k==0:
				r+=1
				c-=10
				break
	
	dest_Point=[r,c]
	
	deltaR=dest_Point[0]-topL[0]
	deltaC=dest_Point[1]-topL[1]
	deltaL=math.sqrt((deltaR**2)+(deltaC**2))
	T=2.778
	L=320*displacement/deltaL
	dist_TopL=T*L
	
#Find the distance "dist_TopR".....
	r=topR[0]+8
	c=topR[1]

	while True:
#		if not(frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if (Valid(frame2[r,c])):
			c-=1
		else:
			break
	
	while True:
#		if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame1[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
		if (Valid(frame2[r,c])):
			r-=1
		else:
			for i in range(0,10):
				c-=1
				k=0
#				if (frame2[r,c,0]<=(frame1[mouseR,mouseC,0]+deviation[0]) and frame2[r,c,0]>=(frame1[mouseR,mouseC,0]-deviation[0]) and frame2[r,c,1]<=(frame1[mouseR,mouseC,1]+deviation[1]) and frame2[r,c,1]>=(frame1[mouseR,mouseC,1]-deviation[1]) and  frame2[r,c,2]<=(frame1[mouseR,mouseC,2]+deviation[2]) and frame2[r,c,2]>=(frame1[mouseR,mouseC,2]-deviation[2])):
				if (Valid(frame2[r,c])):
					r-=1
					k+=1
					break
			
			if k==0:
				r+=1
				c+=10
				break
		
	dest_Point=[r,c]
	
	deltaR=dest_Point[0]-topR[0]
	deltaC=dest_Point[1]-topR[1]
	deltaL=math.sqrt((deltaR**2)+(deltaC**2))
	T=2.778
	L=320*displacement/deltaL
	dist_TopR=T*L

	print "dist_TopL=",dist_TopL
	print "dist_TopR=",dist_TopR
	print "dist_L1=",dist_L1
	print "dist_L2=",dist_L2
	print "dist_R1=",dist_R1
	print "dist_R2=",dist_R2

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------			

def Identify():
	cv2.circle(frame1, (right1[1], right1[0]), 4, (0,255,0), -1)
	cv2.circle(frame1, (right2[1], right2[0]), 4, (0,255,0), -1)
	cv2.circle(frame1, (left1[1], left1[0]), 4, (0,255,0), -1)
	cv2.circle(frame1, (left2[1], left2[0]), 4, (0,255,0), -1)
	cv2.circle(frame1, (topL[1], topL[0]), 4, (0,255,0), -1)
	cv2.circle(frame1, (topR[1], topR[0]), 4, (0,255,0), -1)
	cv2.circle(frame2, (destinationC, destinationR), 4, (0,255,0), -1)
	#while True:
		#cv2.imshow("Identify_Frame1", frame1)
		#if cv2.waitKey(1)==ord('a'):
			#break
	cv2.imwrite("Id_Frame1.jpg", frame1)
	#while True:
		#cv2.imshow("Identify_Frame2", frame2)
		#if cv2.waitKey(1)==ord('b'):
			#break
	cv2.imwrite("Id_Frame2.jpg", frame2)
	#cv2.destroyAllWindows()
	return frame1, frame2, Distance
	

def SharpEye():
	global camera, frame1, frame2
	camera=cv2.VideoCapture(1)
	cv2.namedWindow("Frame1")
	cv2.setMouseCallback("Frame1", On_Click)
	while True:
		ret, frame1=camera.read()
		cv2.imshow("Frame1", frame1)
		if cv2.waitKey(1)==49:
			break
	cv2.imwrite("Frame1.jpg",frame1)
	cv2.namedWindow("Frame2")
	while True:
		ret, frame2=camera.read()
		cv2.imshow("Frame2", frame2)
		if cv2.waitKey(1)==50:
			break
	cv2.imwrite("Frame2.jpg",frame2)
	Go()
	Identify()
	cv2.destroyAllWindows()
	camera.release()