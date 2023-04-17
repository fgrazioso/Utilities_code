#!/usr/bin/env python
"""
Script to find and replace strings in the filenames of a folder
QT gui version
"""

import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import re


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Filenames manipulation")
        
        layout = QGridLayout()
        
        rownum = 0
        
        
        self.label = QLabel()
        layout.addWidget(self.label, rownum, 0, 1, 6)
        self.label.setText("Script manipulate filenames.")
        
        rownum += 1
        
        self.inputbox = QLineEdit()
        layout.addWidget(self.inputbox, rownum, 0, 1, 4)
        #self.inputbox.setFixedSize(QSize(800, 25))
        
        
        self.inputBtn = QPushButton("select input") 
        #self.inputBtn.setFixedSize(QSize(100, 30))       
        layout.addWidget(self.inputBtn, rownum, 4)
        self.inputBtn.clicked.connect(self.selectDir)
        self.inputBtn.setToolTip("This button will open a system dialog window\nto choose a file. This is only for convenience,\nwhat counts is the text written in the field on the side\nwhich can be manually edited.")            
            
        rownum += 1      
        
        
        self.find = QLineEdit()
        layout.addWidget(self.find, rownum, 0,1,4)      
        layout.addWidget(QLabel("find"), rownum, 4)
        #self.find.setFixedSize(QSize(300, 25))
        self.find.setToolTip("string to find.") 
        
        rownum += 1        
        
        self.replace = QLineEdit()
        layout.addWidget(self.replace, rownum, 0,1,4)      
        layout.addWidget(QLabel("replace"), rownum, 4)
        #self.replace.setFixedSize(QSize(300, 25))
        self.replace.setToolTip("string to replace.")         
        
        rownum += 1 
        
        self.execBtn = QPushButton("Execute")
        #self.execBtn.setFixedSize(QSize(100, 30))
        layout.addWidget(self.execBtn, rownum, 3)#, alignment = Qt.AlignHCenter)
        self.execBtn.clicked.connect(self.search_rename)

 
        
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
        
        
    def selectDir(self):
    
        self.inputpath =  str(QFileDialog.getExistingDirectory(self, "Select input Directory"))
        
        #print(self.inputpath)
        self.refresh_text_box(self.inputpath)
        
        self.inputbox.setText(self.inputpath)
        
        

					
    def search_rename(self):
        
        folder_path = Path(self.inputbox.text())
        pattern = self.find.text()
        replacement = self.replace.text()
        
        for file_path in folder_path.rglob("*.*"):   
            
            filename = file_path.stem
            #filextension = file_path.suffix
            #parentpath = file_path.parent
            
            
            newfilename = re.sub(pattern, replacement, filename)
            
            
            newfile_path = file_path.with_name(newfilename)
            
            
            file_path.rename(newfile_path)
    
            self.refresh_text_box("replaced " + str(newfile_path))
            
            
            

    def refresh_text_box(self, logstring): 
        """
        this function is needed, to have a constant update
        of the output in the "text browser" widget
        """
        self.output_wdgt.append(logstring) #append string
        QApplication.processEvents() #update gui for pyqt


###					
# main
###



#You need one QApplication instance per application.
app = QApplication(sys.argv)


window = MainWindow()
window.resize(600, 350)
window.show() #Windows are hidden by default.

#Start the event loop.
app.exec_()

