# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import copy
import math


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QPen,QFontMetrics)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
from data_reader import *
from data_creator import *
from useful_things import *
import copy
from math import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lowBorder = QLineEdit(self.centralwidget)
        self.lowBorder.setObjectName(u"lowBorder")
        self.lowBorder.setGeometry(QRect(10, 10, 113, 22))
        self.highBorder = QLineEdit(self.centralwidget)
        self.highBorder.setObjectName(u"highBorder")
        self.highBorder.setGeometry(QRect(130, 10, 113, 22))
        self.step = QLineEdit(self.centralwidget)
        self.step.setObjectName(u"step")
        self.step.setGeometry(QRect(260, 10, 113, 22))
        self.graphNum = QLineEdit(self.centralwidget)
        self.graphNum.setObjectName(u"graphNum")
        self.graphNum.setGeometry(QRect(390, 10, 113, 22))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 10, 251, 24))
        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")
        self.pushButton.setText("Clear")
        self.resetButton.setGeometry(QRect(820, 10, 150, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lowBorder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0436\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.highBorder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.step.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
        self.graphNum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0444\u0443\u043d\u043a\u0446\u0438\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0435\u0440\u0442\u0438\u0442\u044c", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi





class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.collectData)
        self.ui.resetButton.clicked.connect(self.resetGraph)
        self.Values()
        self.resetStack()
    def resetGraph(self):
        self.check = -1
        self.Values()
        self.update()
        print("False")


    def resetStack(self): #можно убрать, но после отрисовки графика нужно обнулять стак
        self.stack = {}

    def Values(self):
        self.inputLowBorder = 0
        self.inputHighBorder = 0
        self.inputStep = 0
        self.inputGraphNums = []
        self.check = 0
        self.global_nm = []
        self.global_pns = []
        self.global_lstX = []
        self.global_lstY = []
        self.collected_data = []
        self.stack = {}
        self.color = 0
    def collectData(self):
        self.check = 1
        self.inputLowBorder = float(self.ui.lowBorder.text())
        self.inputHighBorder = float(self.ui.highBorder.text())
        self.inputStep = float(self.ui.step.text())
        self.inputGraphNums = self.ui.graphNum.text()
        self.graphNumsList = self.inputGraphNums.split(',')
        if len(self.graphNumsList) > 3:
            while len(self.graphNumsList) != 3:
                self.graphNumsList.pop()
            self.update()

        for func in self.graphNumsList:
            file_name = ''
            if int(func) == 1:
                file_name = 'func_1'
            if int(func) == 2:
                file_name = 'func_2'
            if int(func) == 3:
                file_name = 'func_3'
            if int(func) == 4:
                file_name = 'func_4'
            if int(func) == 5:
                file_name = 'func_5'
            if int(func) == 6:
                file_name = 'func_6'
            if int(func) == 7:
                file_name = 'func_7'
            funcDataCreator(self.inputLowBorder, self.inputHighBorder, self.inputStep, int(func))
            self.stack[func] = []
            self.stack[func] = (DataReader(file_name))

        self.update()
        print(self.stack)
        print("True")

    def paintEvent(self, event):
        if self.check==1:
            qp = QPainter()
            qp.begin(self)
            self.drawMash(qp)
            qp.end()
        else:
            qp = QPainter()
            qp.begin(self)
            self.clearMash(qp)
            qp.end()

    def drawMash(self, qp):
        print(self.stack)
        Max_X = 950
        Max_Y = 850
        Start_X = 50
        Start_Y = 50
        Y_name = 75
        dName = 25
        colors = ['#00FF00','#FF0000','#0000FF']
        heightForBeginAxis = 0
        availableX = 800
        # borders
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(Start_X, Start_Y, Start_X, Max_Y)  # левая грань
        qp.drawLine(Max_X+25, Start_Y, Max_X+25, Max_Y)  # правая грань
        qp.drawLine(Start_X, Max_Y, Max_X+25, Max_Y)  # нижняя грань
        qp.drawLine(Start_X, Start_Y, Max_X+25, Start_Y)  # верхняя грань
        globalCoorsY = {}
        globalCoorsX = {}
        globalPNS = {}
        PositiveY = False
        NegativeY = False
        globalKeys=[]
        globalY = []
        globalX = []
        globalPNS = []
        signsY = []
        zeroY = 0
        zeroX = 0
        stepFunc = 0


        for func in self.stack:
            try:
                for Y in self.stack[func]['Y']:
                    if float(Y) > 0:
                        PositiveY = True
                        continue
                    if float(Y) < 0:
                        NegativeY = True
                        continue
            except:
                continue

        MaxValue = 0
        MinValue = 0
        for func in self.stack:
            MaxValue = self.stack[func]['Y'][0]
            MinValue = self.stack[func]['Y'][0]
            for Y in self.stack[func]['Y']:
                if MaxValue <= Y:
                    MaxValue = float(Y)
                if MinValue >= Y:
                    MinValue = float(Y)
        # отрисовка оси Y
        coors = 0
        if PositiveY and NegativeY:
            zeroX = int(Max_X / 2)
            zeroY = int(Max_Y / 2)
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            pen.setColor("#000")
            qp.setPen(pen)
            qp.drawLine(Start_X, zeroY-5, Max_X+25, zeroY-5)
            qp.drawLine(Start_X, zeroY+5, Max_X+25, zeroY+5)
            qp.drawText(Start_X - 25, zeroY, 30, 10, Qt.AlignCenter, "0")
            stepSign = round(MaxValue / 4, 3)
            maxStep = ceil(MaxValue)
            signsYcopy = []
            temp = 0
            temp_zero = 0
            for i in range(5):
                if i == 0:
                    signsYcopy.append(0)
                    continue
                if i > 1:
                    temp_zero -= stepSign
                    signsYcopy.append(round(temp_zero, 3))
                if i == 4:
                    signsYcopy.append(-maxStep)
            for i in range(4, 0, -1):
                signsY.append(-signsYcopy[i])
            for i in range(5):
                signsY.append(signsYcopy[i])
            stepYsign = int((Max_Y-zeroY) / (len(signsY)/2))
            temp = zeroY
            for sign in signsY:
                if float(sign)>0:
                    coors += stepYsign
                    globalCoorsY[sign] = coors
                    pen.setColor("#000")
                    qp.setPen(pen)
                    qp.drawText(Start_X - 30, coors - 5, 30, 10, Qt.AlignCenter, str(sign))  # отрисовка надписей
                    pen = QPen(Qt.black, 2, Qt.DashLine)
                    pen.setColor("#AAA")
                    qp.setPen(pen)
                    qp.drawLine(Start_X, coors, Max_X + 25, coors)
                if float(sign)<0:
                    temp += stepYsign
                    globalCoorsY[sign] = temp
                    pen.setColor("#000")
                    qp.setPen(pen)
                    qp.drawText(Start_X - 30, temp - 5, 30, 10, Qt.AlignCenter, str(sign))  # отрисовка надписей
                    pen = QPen(Qt.black, 2, Qt.DashLine)
                    pen.setColor("#AAA")
                    qp.setPen(pen)
                    qp.drawLine(Start_X, temp, Max_X + 25, temp)
                if sign == 0:
                    globalCoorsY[sign] = zeroY
        if not(PositiveY):
            zeroX = Start_X
            zeroY = Start_Y
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            pen.setColor("#000")
            qp.setPen(pen)
            qp.drawLine(Start_X, zeroY+10, Max_X+25, zeroY+10)
            qp.drawLine(Start_X, zeroY, Max_X, zeroY)
            qp.drawText(Start_X - 25, zeroY, 30, 10, Qt.AlignCenter, "0")
            signStep = (round(MinValue/8,3))
            temp = 0
            ceilStep = floor(MinValue)
            for i in range(8):
                if i == 0:
                    signsY.append(0)
                    continue
                temp-=signStep
                signsY.append(-round(temp,2))
                if i == 7:
                    signsY.append(ceilStep)
            stepYsign = int(Max_Y / 9) #4 - количество положительных\отрицательных чисел
            temp = 0
            for sign in signsY:
                if sign == 0:
                    globalCoorsY[sign] = zeroY
                if sign < 0:
                    temp += stepYsign
                    globalCoorsY[sign] = temp
                    pen.setColor("#000")
                    qp.setPen(pen)
                    qp.drawText(Start_X - 30, temp - 5, 30, 10, Qt.AlignCenter, str(sign))  # отрисовка надписей
                    pen = QPen(Qt.black, 2, Qt.DashLine)
                    pen.setColor("#AAA")
                    qp.setPen(pen)
                    qp.drawLine(Start_X, temp, Max_X + 25, temp)
                else:
                    continue
        signStep = round(MaxValue/9,2)
        temp = MaxValue
        ceilStep = ceil(signStep)
        if not(NegativeY):
            zeroX = Max_Y
            zeroY = Max_Y
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            pen.setColor("#000")
            qp.setPen(pen)
            qp.drawLine(Start_X, zeroY-10, Max_X+25, zeroY-10)
            qp.drawLine(Start_X, zeroY, Max_X+25, zeroY)
            qp.drawText(Start_X - 25, zeroY, 30, 10, Qt.AlignCenter, "0")

            for i in range(8):
                if i == 0:
                    signsY.append(ceilStep)
                    continue
                temp -= signStep
                signsY.append(round(temp,2))

            stepYsign = int(Max_Y / 9)
            for sign in signsY:
                if sign == 0:
                    globalCoorsY[sign] = zeroY
                if sign > 0:
                    coors += stepYsign
                    globalCoorsY[sign] = coors
                    pen.setColor("#000")
                    qp.setPen(pen)
                    qp.drawText(Start_X - 30, coors - 5, 30, 10, Qt.AlignCenter, str(sign))  # отрисовка надписей
                    pen = QPen(Qt.black, 2, Qt.DashLine)
                    pen.setColor("#AAA")
                    qp.setPen(pen)
                    qp.drawLine(Start_X, coors, Max_X + 25, coors)
                else:
                    continue

        #print(f"{globalCoorsY} - Y signs")

        stepFunc = 0
        # отрисовка оси X
        for func in self.stack:
            width = Max_X+50 #- Start_X
            step = int(width/(len(self.stack[func]['X'])+1))
            start = 0
            for X in self.stack[func]['X']:
                start += step
                globalCoorsX[X] = start
                globalX.append(start)
                pen.setColor("#000")
                qp.setPen(pen)
                qp.drawText(start-15,Max_Y+10,30,10,Qt.AlignCenter, str(X)) # отрисовка надписей
                pen = QPen(Qt.black, 2, Qt.DashLine)
                pen.setColor("#AAA")
                qp.setPen(pen)
                qp.drawLine(start,Start_Y,start,Max_Y) # отрисовка линий
            for Y in self.stack[func]['Y']:
                highBorder = 0
                lowBorder = 0
                if Y > 0:
                    for i in range(len(signsY)):
                        if signsY[i] > 0:
                            if Y == signsY[0]:
                                temp = globalCoorsY[signsY[0]]
                            if Y < signsY[i]:
                                highBorder = signsY[i]
                                lowBorder = signsY[i+1]
                                temp = floor(globalCoorsY[lowBorder]-(abs(round(float(Y/2),2)))*(abs(globalCoorsY[highBorder]-globalCoorsY[lowBorder])))
                    #temp = globalCoorsY[lowBorder]+(floor((Y/highBorder))*abs(ceil(abs(globalCoorsY[highBorder] - globalCoorsY[lowBorder]))))
                    globalY.append(temp)
                    continue
                if Y < 0:
                    for i in range(len(signsY)):
                        if signsY[i] < 0:
                            if Y > signsY[i]:
                                highBorder = signsY[i]
                                lowBorder = signsY[i-1]
                    #temp = globalCoorsY[lowBorder] + abs(ceil(abs(globalCoorsY[highBorder] - globalCoorsY[lowBorder]) * Y))
                    temp = floor((abs(round(float(Y/2),2)))*(abs(globalCoorsY[highBorder]-globalCoorsY[lowBorder])) + globalCoorsY[lowBorder])
                    globalY.append(temp)
                    continue
                if Y == 0:
                    globalY.append(zeroY)
                    continue
            for i in range(len(globalX)):
                globalPNS.append([globalX[i],globalY[i]])
            #print(f"{globalPNS} - {self.stack[func]['Name']}")
            try:
                color = colors[self.color]
                pen = QPen(Qt.black, 2, Qt.SolidLine)
                qp.setPen(pen)
                qp.setBrush(QColor(color))
                for point in globalPNS:
                    if point[1] > zeroY:
                        qp.drawRoundedRect(point[0] + stepFunc - 5, zeroY, 10, 5, 10, 50)  # нижний
                        qp.drawRect(point[0] + stepFunc - 5, point[1] + 5, 10, zeroY - point[1])
                        qp.drawRoundedRect(point[0] + stepFunc - 5, point[1] + 4, 10, 5, 10, 50)  # верхний
                    if point[1] < zeroY:
                        qp.drawRect(point[0] - stepFunc - 5, point[1], 10, zeroY - point[1])
                        qp.drawRoundedRect(point[0] - stepFunc - 5, zeroY - 1, 10, 5, 10, 50)  # - по оси
                        qp.drawRoundedRect(point[0] - stepFunc - 5, point[1] - 4, 10, 5, 10, 50)  # верхний
                    if point[1] == zeroY:
                        qp.drawRoundedRect(point[0] + stepFunc - 5, zeroY - 1.5, 10, 5, 10, 50)  # -по оси
                stepFunc += 10
                self.color += 1
            except:
                continue
            globalX = []
            globalY = []
            globalPNS = []
        self.color = 0
        #название графиков + отрисовка
        for func in self.stack:
            try:
                localFuncName = str(self.stack[func]['Name'])
                color = colors[self.color]
                pen = QPen(Qt.black, 2, Qt.SolidLine)
                qp.setPen(pen)
                qp.setBrush(QColor(color))
                # for point in globalPNS:
                #     if point[1]>zeroY:
                #         qp.drawRoundedRect(point[0] + stepFunc, zeroY, 10, 5, 10, 50)  #нижний
                #         qp.drawRect(point[0] + stepFunc, point[1] + 5, 10, zeroY - point[1])
                #         qp.drawRoundedRect(point[0] + stepFunc, point[1] + 4, 10, 5, 10, 50)   #верхний
                #     if point[1]<zeroY:
                #         qp.drawRect(point[0] - stepFunc, point[1], 10, zeroY - point[1])
                #         qp.drawRoundedRect(point[0] - stepFunc, zeroY - 1, 10, 5, 10, 50)  # - по оси
                #         qp.drawRoundedRect(point[0] - stepFunc, point[1] - 4, 10, 5, 10, 50) #верхний
                #     if point[1]==zeroY:
                #         qp.drawRoundedRect(point[0]+stepFunc, zeroY-1.5, 10, 5, 10, 50)  # -по оси
                qp.drawRoundedRect(Max_X+55, Y_name, 15, 15, 1000, 1000)
                pen.setColor("#000")
                qp.setPen(pen)
                qp.drawText(Max_X+80,Y_name-2,40,30,Qt.AlignLeft, str(localFuncName))
                Y_name+=dName
                    # qp.drawRect(key - 13, int(Max_Y / 2) - 5, 25,-(abs(int(Max_Y / 2) - value) - 10))
                    #qp.drawRoundedRect(point[0]+5, zeroY, 10, 5, 10, 50)  # -по оси
                    #qp.drawRect(point[0]+5,point[1]+5,10,zeroY-point[1]) #x,y,w,h; h-высота прямоугольника до точки
                    #qp.drawRoundedRect(point[0]+5, point[1] - 1, 10, 5, 10, 50)  # -нижний
                self.color+=1
            except:
                continue

        Max_X = 950
        Max_Y = 850
        Start_X = 50
        Start_Y = 50
        Y_name = 75
        dName = 25
        colors = ['#00FF00', '#FF0000', '#0000FF']
        signsY = [2, 1.5, 1, 0.5, 0, -0.5, -1, -1.5, -2]
        heightForBeginAxis = 0
        availableX = 800
        # borders
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(Start_X, Start_Y, Start_X, Max_Y)  # левая грань
        qp.drawLine(Max_X + 25, Start_Y, Max_X + 25, Max_Y)  # правая грань
        qp.drawLine(Start_X, Max_Y, Max_X + 25, Max_Y)  # нижняя грань
        qp.drawLine(Start_X, Start_Y, Max_X + 25, Start_Y)  # верхняя грань
        globalCoorsY = {}
        globalCoorsX = {}
        globalPNS = {}
        PositiveY = False
        NegativeY = False
        globalKeys = []
        globalY = []
        globalX = []
        globalPNS = []


    def clearMash(self,qp):
        color = QColor('#FFF')
        qp.setPen(color)
        qp.setBrush(QColor("#FFF"))
        qp.drawRect(0, 0, 1000, 800)



if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
