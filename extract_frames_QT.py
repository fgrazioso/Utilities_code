#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
NB: this script has been rewritten. An older version (created for a previous experiment) has been fixed, but not tested
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os, sys

from pathlib import Path

import cv2

from math import ceil


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
        self.inputBtn.clicked.connect(self.selectInput)
        self.inputBtn.setToolTip("This button will open a system dialog window\nto choose a file. This is only for convenience,\nwhat counts is the text written in the field on the side\nwhich can be manually edited.")            
            
        rownum += 1
                
        self.isFolder = QCheckBox()
        layout.addWidget(self.isFolder, rownum, 0)#, alignment = Qt.AlignRight)
        self.isFolder.setText("input is folder")
        self.isFolder.setToolTip("If checked, all the files in the\nselected folder will be processed.")    
        
        self.isRecursive = QCheckBox()
        layout.addWidget(self.isRecursive, rownum, 1)#, alignment = Qt.AlignRight)
        self.isRecursive.setText("recursive")
        self.isRecursive.setToolTip("If checked, the folders\nwill be processed recursively.")    
        
        
        self.extension = QLineEdit()
        layout.addWidget(self.extension, rownum, 4, alignment = Qt.AlignRight)      
        layout.addWidget(QLabel("input\nextension"), rownum, 5)
        self.extension.setFixedSize(QSize(60, 25))
        self.extension.setText("mp4")
        self.extension.setToolTip("Extension for the input files. Don't write the dot.")  
        
        
        
        
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
        
        self.outExt = QComboBox()
        layout.addWidget(self.outExt, rownum, 4)#, alignment = Qt.AlignRight)      
        layout.addWidget(QLabel("output\nextension"), rownum, 5)
        self.outExt.setFixedSize(QSize(90, 25))
        self.outExt.addItem("png")
        self.outExt.addItem("jpg")
        self.outExt.addItem("bmp")
        self.outExt.setToolTip("Extension for the output files.")           
        
        rownum += 1
        
                
        self.fpsBtn = QPushButton("read par")
        #self.fpsBtn.setFixedSize(QSize(100, 30))
        layout.addWidget(self.fpsBtn, rownum, 0)#, alignment = Qt.AlignLeft)
        self.fpsBtn.clicked.connect(self.readfps) 
        self.fpsBtn.setToolTip("This reads some parameters from the video, such as duration in seconds and frames per seconds.")        
        
        self.totSec = QLineEdit()
        layout.addWidget(self.totSec, rownum, 2)
        layout.addWidget(QLabel("tot sec"), rownum, 3)
        self.totSec.setReadOnly(True)
        self.totSec.setToolTip("Total number of seconds in the video. This is a read-only field, to help the user set the values in the fields below.")
        
        self.isFull = QCheckBox()
        layout.addWidget(self.isFull, rownum, 5)#, alignment = Qt.AlignRight)
        self.isFull.setText("full")
        self.isFull.setToolTip("If checked, the file will be\nprocessed from start to end.")  
        
        rownum += 1
        
        self.decimate = QSpinBox()
        layout.addWidget(self.decimate, rownum, 0)
        self.decimate.setValue(0)
        self.decimate.setRange(0, 1000)
        self.decimate.setToolTip("This value decides how many frames to \"jump\".\nIf value \'0\' is given, all the frames will be generated;\nif value \'1\' is given, 1 frame will be discarded\nafter each frame saved;\n if value \'2\' is given, 2 frames will be discarded\nafter each frame saved.\nAnd so forth.")
        
        layout.addWidget(QLabel("jump num"), rownum, 1)     
        
        



        self.strtSec = QSpinBox()
        layout.addWidget(self.strtSec, rownum, 2)
        self.strtSec.setValue(0)
        self.strtSec.setRange(0, 1000)
        self.strtSec.setToolTip("Position in seconds of the first frame to be extracted.")
        
        layout.addWidget(QLabel("strt sec"), rownum, 3)              
        
        
        self.endSec = QSpinBox()
        layout.addWidget(self.endSec, rownum, 4)
        self.endSec.setValue(0)
        self.endSec.setRange(0, 1000)
        self.endSec.setToolTip("Position in seconds of the last frame to be extracted.")
        
        layout.addWidget(QLabel("end sec"), rownum, 5)   
                        
        
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
        


    def selectInput(self):
        if not self.isFolder.isChecked():
            self.selectFile()
            
        elif self.isFolder.isChecked():
            self.selectDir()
                       

    def selectFile(self): 
        
        self.inputpath = QFileDialog.getOpenFileName(self, 'Select input file')[0]
        self.inputbox.setText(self.inputpath)
        
        
    def selectDir(self):
    
        self.inputpath =  str(QFileDialog.getExistingDirectory(self, "Select input Directory"))
        
        #print(self.inputpath)
        self.refresh_text_box(self.inputpath)
        
        self.inputbox.setText(self.inputpath)


    def read_single_fps(self, inputfile_path):
        inputfile_path = str(inputfile_path)
        vidcap = cv2.VideoCapture(inputfile_path)
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        frameNumbers =  vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        #print("Frames per Seconds = {}".format(fps))
        self.refresh_text_box("\nfile: {0}\nFrames per Seconds: = {1}\ntotal frames = {2}\n".format(inputfile_path, fps, frameNumbers))
        
        durationsec = (frameNumbers/fps) 
        
        self.totSec.setText(str(durationsec))
        self.endSec.setValue(ceil(durationsec))



    def readfps(self):

    
        if self.isFolder.isChecked():
            inputDir  = self.inputbox.text()
            if self.isRecursive.isChecked():
            
                for inputfile_path in Path(inputDir).rglob("*." + self.extension.text()):
                    self.read_single_fps(inputfile_path)
                    
            else:
                for inputfile_path in Path(inputDir).glob("*." + self.extension.text()):
                    #print("test - ecco")
                    #print(inputfile_path)
                    self.read_single_fps(inputfile_path)
        
        else:
            inputfile_path = self.inputbox.text()
            self.read_single_fps(inputfile_path)
            
        
    def extractFnc(self):
    
        if not self.isFolder.isChecked():
        
            #print("eseguo: file singolo")
            self.refresh_text_box("work on a single file")
            
            inputfile_path  = self.inputbox.text()
            
            
            self.singleExtract(inputfile_path)
            
        elif self.isFolder.isChecked():
        
            #print("eseguo: cartella")
            self.refresh_text_box("work on a folder")
        
            inputDir = self.inputbox.text()
            
            if self.isRecursive.isChecked():
            
                for inputfile_path in Path(inputDir).rglob("*." + 
                                                        self.extension.text()):
                
                    self.singleExtract(inputfile_path)
            else:
                for inputfile_path in Path(inputDir).glob("*." + 
                                                        self.extension.text()):
                
                    self.singleExtract(inputfile_path)
            
        

    def singleExtract(self, inputfile_path):
        inputfile_path = str(inputfile_path)
        parent = Path(inputfile_path).parent.absolute()
        filename = Path(inputfile_path).stem
        
        
        if self.isFull.isChecked():
            strtMs = float(0) 
            self.strtSec.setValue(0)
            self.read_single_fps(inputfile_path)
            endMs = float(self.endSec.text()) * 1000
        
        
        else:
            strtMs = float(self.strtSec.text()) * 1000
            
            endMs = float(self.endSec.text()) * 1000
        
        # print("so far so good")

        # we create a folder named as the file
        output_path = os.path.join(parent, filename + "_frames")
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    
        vidcap = cv2.VideoCapture(inputfile_path)

        fps = vidcap.get(cv2.CAP_PROP_FPS)
        
        frameNumbers =  vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        videoLengthMs = (frameNumbers / fps) * 1000
        charnm = len(str(ceil(videoLengthMs)))

        # print("Frames per Seconds = {}".format(fps))
        
        self.refresh_text_box("Frames per Seconds = {0}\ntotal frames = {1}".format(fps, frameNumbers))
        

        frame_exists, curr_frame = vidcap.read()
        
        count = 0

        while frame_exists:
            
            
            timestamp = vidcap.get(cv2.CAP_PROP_POS_MSEC)
            
            if timestamp > endMs:
                return
                
    
            if timestamp < strtMs:
                vidcap.read()
                continue
            
            
            
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
                
            
            for i in range(self.decimate.value()):
                frame_exists, curr_frame = vidcap.read()
                 
            
            count += 1


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
