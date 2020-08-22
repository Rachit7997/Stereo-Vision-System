#Dual camera with multi threads...
from sys import argv
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import cv2
import numpy as np
import time
import March_21

class cam1(QThread):
	def __init__(self):
		super(cam1, self).__init__()
		
	def __del__(self):
		self.wait()
	
	def run(self):
		self.emit(SIGNAL('1'))
		#time.sleep(0.15)
		
		

class cam2(QThread):
	
	def __init__(self):
		super(cam2, self).__init__()
	
	def __del__(self):
		self.wait()
	
	def run(self):
		self.emit(SIGNAL('2'))
		#time.sleep(0.15)
			

class Sharp_Eye(QThread):
	def __init__(self):
		super(Sharp_Eye, self).__init__()
		#self.mouse_C = mouseC
		#self.mouse_R = mouseR
		#self.F1 = frame1
		#self.F2 = frame2
		
	def get_Info(self, mouseC, mouseR, frame1, frame2):
		self.mouse_C = mouseC
		self.mouse_R = mouseR
		self.F1 = frame1
		self.F2 = frame2
	
	def __del__(self):
		self.wait()
	
	def run(self):
		March_21.Go(self.mouse_C, self.mouse_R, self.F1, self.F2)
		self.Id_Frame1, self.Id_Frame2, self.result = March_21.Identify()
		self.emit(SIGNAL('7'))
	
	
class main_window (QMainWindow):
	def __init__(self, parent=None):
		super(main_window, self).__init__(parent)
		self.wg = widget(self)
		self.setCentralWidget(self.wg)
		self.setWindowTitle("Welcome To SharpEyes.")
		
class widget (QWidget):
	def __init__(self, parent):
		super(widget, self).__init__(parent)
		#self.camera1 = cv2.VideoCapture(1)
		#self.camera1.release()
		#self.camera2 = cv2.VideoCapture(2)
		#self.camera2.release()
		self.mouseC = 0
		self.mouseR = 0
		self.wallpaper = QImage("D:\WorkSpace\PYTHON\THREAD\SharpEye")
		self.FRAME1 = QImage("D:\WorkSpace\PYTHON\THREAD\SharpEye")
		self.FRAME2 = QImage("D:\WorkSpace\PYTHON\THREAD\SharpEye")
		self.frame1 = cv2.imread("D:\WorkSpace\PYTHON\THREAD\SharpEye")
		self.frame2 = cv2.imread("D:\WorkSpace\PYTHON\THREAD\SharpEye")
		self.Graphic1 = QGraphicsView()
		self.Graphic2 = QGraphicsView()
		self.Scene1 = QGraphicsScene()
		self.Scene2 = QGraphicsScene()
		self.pixmapitem1 = QGraphicsPixmapItem(QPixmap(self.wallpaper), None, self.Scene1)
		self.pixmapitem1.mousePressEvent = self.PixSelect
		self.Graphic1.setScene(self.Scene1)
		self.pixmapitem2 = QGraphicsPixmapItem(QPixmap(self.wallpaper), None, self.Scene2)
		#self.pixmapitem2.mousePressEvent = self.PixSelect_2
		self.Graphic2.setScene(self.Scene2)
		self.label1 = QLabel("select Pixel in screen_1")
		self.warning = QLabel("<font color =red><I>Please! Reastart the application after 1min & 30 sec !!</I></font>")
		
		self.ON = QPushButton("&ON")
		self.OFF = QPushButton("&OFF")
		self.Get_Distance = QPushButton("&GET_DISTANCE")
		self.Result = QTextBrowser()
		self.Status = QLabel("STATUS: Check status here !!")
		
		
		glayout = QGridLayout()
		glayout.addWidget(self.ON, 0, 0)
		glayout.addWidget(self.OFF, 0, 1)
		glayout.addWidget(self.Get_Distance, 1, 0, 1, 2)
		glayout.addWidget(self.Result, 2, 0, 2, 2)
		layout1 = QHBoxLayout()
		layout1.addWidget(self.Graphic1)
		layout1.addWidget(self.Graphic2)
		layout1.addLayout(glayout)
		layout2 = QVBoxLayout()
		layout2.addWidget(self.warning)
		layout2.addWidget(self.label1)
		layout2.addLayout(layout1)
		layout2.addWidget(self.Status)
		self.setLayout(layout2)		#Final Layout is formed out
		
		self.C1 = cam1()
		self.C2 = cam2()
		
		self.timer1 = QTimer()
		self.timer2 = QTimer()
		self.T3 = Sharp_Eye()
		
		#self.connect(self.start_cam1, SIGNAL("clicked()"), self.Start)
		#self.connect(self.stop_cam1, SIGNAL("clicked()"), self.Stop)
		self.connect(self.ON, SIGNAL("clicked()"), self.Start)
		self.connect(self.OFF, SIGNAL("clicked()"), self.Stop)
		
		self.connect(self.C1, SIGNAL('1'), self.Function1)
		self.connect(self.C2, SIGNAL('2'), self.Function2)
		
		self.connect(self.Get_Distance, SIGNAL("clicked()"), self.Calculate)
		self.connect(self.T3, SIGNAL('7'), self.make_ID)
	
	def PixSelect (self, event):
		Position = QPoint (event.pos().x(), event.pos().y())
		color = QColor.fromRgb (self.FRAME1.pixel(Position))
		self.mouseC = int (event.pos().x())
		self.mouseR = int (event.pos().y())
		if color.isValid():
			rgbColor = '('+str(color.red())+','+str(color.green())+','+str(color.blue())+','+str(color.alpha())+')'
			self.label1.setText('Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() )+ ') - Value (R,G,B,A)= ' + rgbColor)
		else:
			self.label1.setText('Pixel position = (' + str( event.pos().x() ) + ' , ' + str( event.pos().y() )+ ') - color not valid')
	
	def Start (self):
		self.camera1 = cv2.VideoCapture(0)
		self.C1.start()
		self.camera2 = cv2.VideoCapture(2)
		self.C2.start()
	
		
	def Stop (self):
		self.timer1.stop()
		self.timer2.stop()
		self.C1.quit()
		self.C1.terminate()
		self.pixmapitem1 = QGraphicsPixmapItem(QPixmap(self.wallpaper), None, self.Scene1)
		self.Graphic1.setScene(self.Scene1)
		self.camera1.release()
		self.C2.quit()
		self.C2.terminate()
		self.pixmapitem2 = QGraphicsPixmapItem(QPixmap(self.wallpaper), None, self.Scene2)
		self.Graphic2.setScene(self.Scene2)
		self.camera2.release()	
		self.T3.quit()
		self.T3.terminate()
	
	
	def Function1(self):
		self.timer1.timeout.connect(self.function1)
		self.timer1.start(30)
		
	def Function2(self):
		self.timer1.timeout.connect(self.function2)
		self.timer1.start(30)
		
	def function1(self):
		ret, self.frame1=self.camera1.read()
		Qframe1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2RGB) #Remind It.....
		self.FRAME1 = QImage(Qframe1, Qframe1.shape[1], Qframe1.shape[0], QImage.Format_RGB888)		#An Important Statement....
		self.pixmapitem1 = QGraphicsPixmapItem(QPixmap(self.FRAME1), None, self.Scene1)
		self.Graphic1.setScene(self.Scene1)
				
	def function2(self):
		ret, self.frame2=self.camera2.read()
		
		
	def Calculate(self):
		#self.T3 = Sharp_Eye()	
		self.T3.get_Info( self.mouseC, self.mouseR, self.frame1, self.frame2)#Tricky Point.. If any error found, first examine this one!
		self.T3.start()
		#self.frame2 = self.T3.Id_Frame1
				
	def make_ID(self):
		self.frame2 = self.T3.Id_Frame1
		#self.frame2 = cv2.imread("Id_Frame1.jpg")
		self.frame2 = cv2.cvtColor(self.frame2, cv2.COLOR_BGR2RGB) #Remind It.....
		self.FRAME2 = QImage(self.frame2, self.frame2.shape[1], self.frame2.shape[0], QImage.Format_RGB888)		#An Important Statement....
		self.pixmapitem2 = QGraphicsPixmapItem(QPixmap(self.FRAME2), None, self.Scene2)
		self.Graphic2.setScene(self.Scene2)
		self.Result.append("<font color=red>The DIstance of this Object is :<b>%f</b></font>"%self.T3.result)
		cv2.imshow("Id_Frame2", self.T3.Id_Frame2)
		cv2.waitKey(0)
		
		
		
app =QApplication(argv)
MyWindow = main_window()
MyWindow.show()
app.exec_()