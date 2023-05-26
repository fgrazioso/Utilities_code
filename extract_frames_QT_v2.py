#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
NB: this script has been rewritten. An older version (created for a previous experiment) has been fixed, but not tested

This second version is for "loading an external file with timestamps", for 'cherrypicking' the frames needed.
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os, sys

from pathlib import Path

import cv2

import numpy as np


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        
        self.setWindowTitle("Frames extraction")
        
        layout = QGridLayout()
        
        rownum = 0
        
        self.label = QLabel()
        layout.addWidget(self.label, rownum, 0, 1, 6)
        self.label.setText("Script to extract frames from video files.\nInsert the input path in the first field, or use the button to select.\nIf you want to batch process all files in a folder, check the checkbox and add the extension of the files (without the dot).\nWhen ready, press the 'Extract' button. Folders will be created, with the same name of the file.\nIt is possible to write a watermark with the name on the corner of each file.\nIt is possible to skip every 'n' frames.")
        
        rownum += 1
        
        self.inputbox = QLineEdit()
        layout.addWidget(self.inputbox, rownum, 0, 1, 4)
        #self.inputbox.setFixedSize(QSize(800, 25))
        
        self.inputBtn = QPushButton("select input") 
        #self.inputBtn.setFixedSize(QSize(100, 30))       
        layout.addWidget(self.inputBtn, rownum, 4)
        self.inputBtn.clicked.connect(self.selectFile)
        self.inputBtn.setToolTip("This button will open a system dialog window\nto choose a file. This is only for convenience,\nwhat counts is the text written in the field on the side\nwhich can be manually edited.")            
            


        
        
        rownum += 1
        
        self.watermark = QCheckBox()
        layout.addWidget(self.watermark, rownum, 0)#, alignment = Qt.AlignRight)
        self.watermark.setText("watermark")
        self.watermark.setToolTip("If checked, a watermark containing the timestamp\nwill be added to the file.")
        

        
 

        self.doVidName = QCheckBox()
        layout.addWidget(self.doVidName, rownum, 1)#, alignment = Qt.AlignRight)
        self.doVidName.setText("video name")
        self.doVidName.setChecked(1)
        self.doVidName.setToolTip("If checked, the name of the video file is prefixed to all the frame file names.") 
        
        
        
        
        self.extension = QLineEdit()
        layout.addWidget(self.extension, rownum, 2, alignment = Qt.AlignRight)      
        layout.addWidget(QLabel("input\nextension"), rownum, 3)
        self.extension.setFixedSize(QSize(60, 25))
        self.extension.setText("mp4")
        self.extension.setToolTip("Extension for the input files. Don't write the dot.")  
        
        
        
        self.outExt = QComboBox()
        layout.addWidget(self.outExt, rownum, 4)#, alignment = Qt.AlignRight)      
        layout.addWidget(QLabel("output\nextension"), rownum, 5)
        self.outExt.setFixedSize(QSize(90, 25))
        self.outExt.addItem("png")
        self.outExt.addItem("jpg")
        self.outExt.addItem("bmp")
        self.outExt.addItem("tif")
        self.outExt.setToolTip("Extension for the output files.")           
        
        rownum += 1
        
                
        self.fpsBtn = QPushButton("read par")
        #self.fpsBtn.setFixedSize(QSize(100, 30))
        layout.addWidget(self.fpsBtn, rownum, 0)#, alignment = Qt.AlignLeft)
        self.fpsBtn.clicked.connect(self.read_fps) 
        self.fpsBtn.setToolTip("This reads some parameters from the video, such as duration in seconds and frames per seconds.")        
        
        self.totSec = QLineEdit()
        layout.addWidget(self.totSec, rownum, 2)
        layout.addWidget(QLabel("tot sec"), rownum, 3)
        self.totSec.setReadOnly(True)
        self.totSec.setToolTip("Total number of seconds in the video. This is a read-only field, to help the user set the values in the fields below.")
        
        
        self.fps = QLineEdit()
        layout.addWidget(self.fps, rownum, 4)
        layout.addWidget(QLabel("fps"), rownum, 5)
        self.fps.setReadOnly(True)
        self.fps.setToolTip("'frames per seconds' in the video.\n This is a read-only field, to help the user\n set the timestamps external file")
        

        
        rownum += 1
        
  
        
        self.inputbox2 = QLineEdit()
        layout.addWidget(self.inputbox2, rownum, 1, 1, 4)
        self.inputbox2.setToolTip("In this field we read the path to an external file,\nwith a list of the wanted timestamps\nof the frames to extract.")  
        #self.inputbox.setFixedSize(QSize(800, 25))
        
        self.inputBtn2 = QPushButton("sel. ext. file") 
        #self.inputBtn.setFixedSize(QSize(100, 30))       
        layout.addWidget(self.inputBtn2, rownum, 5)
        self.inputBtn2.clicked.connect(self.selectExFile)
        self.inputBtn2.setToolTip("This button will open a system dialog window\nto choose a file. This is only for convenience,\nwhat counts is the text written in the field on the side\nwhich can be manually edited.")          
                        
        
        rownum += 1
        
        self.extractBtn = QPushButton("Extract")
        #self.extractBtn.setFixedSize(QSize(100, 30))
        layout.addWidget(self.extractBtn, rownum, 2)#, alignment = Qt.AlignHCenter)
        self.extractBtn.clicked.connect(self.extractFnc)


 
        
        rownum += 1
                
        self.output_wdgt = QTextBrowser()
        #self.output_wdgt.setGeometry(QRect(10, 90, 800, 100))
        ###self.output_wdgt.setFixedSize(QSize(500, 150))
        layout.addWidget(self.output_wdgt, rownum, 0, 4, 6)     
        self.output_wdgt.setToolTip("In this field the messages to the user will be printed.\nThere may be **delay** to print the message.")       
        
    
        widget = QWidget()
        widget.setLayout(layout)
    
        # Set the central widget of the Window. 
        self.setCentralWidget(widget)    
        


                       

    def selectFile(self): 
        
        self.inputpath = QFileDialog.getOpenFileName(self, 'Select input file')[0]
        self.inputbox.setText(self.inputpath)
        
        


    def selectExFile(self): 
        
        self.extFilepath = QFileDialog.getOpenFileName(self, 'Select external file')[0]
        self.inputbox2.setText(self.extFilepath)
        
        
        

    def read_fps(self):
        inputfile_path = str(self.inputbox.text())
        vidcap = cv2.VideoCapture(inputfile_path)
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        frameNumbers =  vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        #print("Frames per Seconds = {}".format(fps))
        self.refresh_text_box("\nfile: {0}\nFrames per Seconds: = {1}\ntotal frames = {2}\n".format(inputfile_path, fps, frameNumbers))
        
        durationsec = (frameNumbers/fps) 
        
        self.totSec.setText(str(durationsec))
        self.fps.setText(str(fps))




            
        
    def extractFnc(self):
    
            
        inputfile_path  = str(self.inputbox.text())
        

        parent = Path(inputfile_path).parent.absolute()
        filename = Path(inputfile_path).stem
        

        
        # print("so far so good")

        # we create a folder named as the file
        output_path = os.path.join(parent, filename + "_frames")
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
            
        
    
        vidcap = cv2.VideoCapture(inputfile_path)

        fps = vidcap.get(cv2.CAP_PROP_FPS)
        
        frameNumbers =  vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        videoLengthMs = (frameNumbers / fps) * 1000
        charnm = len(str(np.ceil(videoLengthMs)))
        
        frame_int = videoLengthMs / frameNumbers
        # interval between frames, in milliseconds

        # print("Frames per Seconds = {}".format(fps))
        
        self.refresh_text_box("Frames per Seconds = {0}\ntotal frames = {1}".format(fps, frameNumbers))
        

        frame_exists, curr_frame = vidcap.read()
        

        timestamps_array = np.loadtxt(str(self.inputbox2.text()))
        
        print(f"timestaps array = {timestamps_array}")
        

        
        
        
        for req_timestamp in timestamps_array:
                
            while frame_exists:
                
                timestamp = vidcap.get(cv2.CAP_PROP_POS_MSEC)
                
                if abs(timestamp - req_timestamp) <= frame_int:
            
                    formatted_name = f"{{:0>{charnm}.0f}}".format(timestamp)
        
        
                    if self.watermark.isChecked():
                        curr_frame = cv2.putText(curr_frame, formatted_name, (30, 60), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3)
                        #print("watermark {} added".format(timestamp))
                        self.refresh_text_box("watermark {} added".format(timestamp))
                    
                    
                    if self.doVidName.isChecked():
                        formatted_name = filename + "_" + formatted_name   
                    
                    output_file = os.path.join(output_path, formatted_name + "." + self.outExt.currentText())                             
                

                    #print(".", end="")
                    self.refresh_text_box("saving frame {} ms".format(timestamp))
                    cv2.imwrite(output_file, curr_frame)     # save frame as file, the ype is chosen by the extension    
                    frame_exists, curr_frame = vidcap.read()
                    #print('Read a new frame: ', frame_exists)
                    self.refresh_text_box('Read a new frame: ' + str(frame_exists))
                    
                    
                    break
                    
                    
                else: frame_exists, curr_frame = vidcap.read()
                
            


                    
                
    


    def refresh_text_box(self, logstring): 
        """
        this function is needed, to have a constant update
        of the output in the "text browser" widget
        """
        self.output_wdgt.append(logstring) #append string
        QApplication.processEvents() #update gui for pyqt


#You need one QApplication instance per application.
app = QApplication(sys.argv)


window = MainWindow()
window.resize(600, 350)
window.show() #Windows are hidden by default.

#Start the event loop.
app.exec_()
