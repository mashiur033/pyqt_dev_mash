# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:00:34 2024

@author: Mashiur
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pandas as pd
import numpy as np

# class Wndow()

# create class to import csv and create dataframe
class Import_file():
    pass

# create class to analyze data
class Analyze_data():
    pass

# class to create work package
class Create_WorkPackage():
    # we will add code in later stage
    pass

# app = QApplication([])

# label = QLabel('Hello World!')
# label.show()
# app.exec()
# subclass
class CheckableComboBox(QtWidgets.QComboBox):
    # once there is a checkState set, it is rendered
    # here we assume default Unchecked
    def addItem(self, item):
        super(CheckableComboBox, self).addItem(item)
        item = self.model().item(self.count()-1,0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)

    def itemChecked(self, index):
        item = self.model().item(i,0)
        return item.checkState() == QtCore.Qt.Checked


class PythonTool(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # set the title
        self.setWindowTitle("Do Less Do Better")
        self.setGeometry(30, 30, 1000, 1000)
        
        # Call the method 
        
        
        # show all the widgets
        self.show()
 
        
 
    def components(self):
        
        # Adding 
 
 
        # creating a label widget
        self.label_1 = QLabel("Fixed width", self)
 
        # moving position
        self.label_1.move(0, 0)
 
        # setting up the border
        self.label_1.setStyleSheet("border :3px solid black;")
 
        # resizing label
        self.label_1.resize(120, 80)
 
     
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())