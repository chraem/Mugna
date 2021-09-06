# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowisSXMZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1166, 566)
        icon = QIcon()
        icon.addFile(u":/images/cat.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.inputs = QFrame(self.centralwidget)
        self.inputs.setObjectName(u"inputs")
        self.inputs.setMinimumSize(QSize(0, 0))
        self.inputs.setStyleSheet(u"")
        self.inputs.setFrameShape(QFrame.NoFrame)
        self.inputs.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.inputs)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 5, 20)
        self.frame_5 = QFrame(self.inputs)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"color: rgb(5, 55, 66);\n"
"font: bold 20pt \"assets/font/monda.ttf\";")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.clear_BTN = QPushButton(self.frame_5)
        self.clear_BTN.setObjectName(u"clear_BTN")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clear_BTN.sizePolicy().hasHeightForWidth())
        self.clear_BTN.setSizePolicy(sizePolicy1)
        self.clear_BTN.setMinimumSize(QSize(80, 25))
        self.clear_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold 12pt \"assets/font/monda.ttf\";\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.clear_BTN.setFlat(True)

        self.horizontalLayout_3.addWidget(self.clear_BTN)

        self.add_BTN = QPushButton(self.frame_5)
        self.add_BTN.setObjectName(u"add_BTN")
        sizePolicy1.setHeightForWidth(self.add_BTN.sizePolicy().hasHeightForWidth())
        self.add_BTN.setSizePolicy(sizePolicy1)
        self.add_BTN.setMinimumSize(QSize(80, 25))
        self.add_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold 12pt \"assets/font/monda.ttf\";\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.add_BTN.setFlat(True)

        self.horizontalLayout_3.addWidget(self.add_BTN)

        self.report_BTN = QPushButton(self.frame_5)
        self.report_BTN.setObjectName(u"report_BTN")
        sizePolicy1.setHeightForWidth(self.report_BTN.sizePolicy().hasHeightForWidth())
        self.report_BTN.setSizePolicy(sizePolicy1)
        self.report_BTN.setMinimumSize(QSize(80, 25))
        self.report_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.report_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold 12pt \"assets/font/monda.ttf\";\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.report_BTN.setFlat(True)

        self.horizontalLayout_3.addWidget(self.report_BTN)

        self.delete_BTN = QPushButton(self.frame_5)
        self.delete_BTN.setObjectName(u"delete_BTN")
        sizePolicy1.setHeightForWidth(self.delete_BTN.sizePolicy().hasHeightForWidth())
        self.delete_BTN.setSizePolicy(sizePolicy1)
        self.delete_BTN.setMinimumSize(QSize(80, 25))
        self.delete_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold 12pt \"assets/font/monda.ttf\";\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.delete_BTN.setFlat(True)

        self.horizontalLayout_3.addWidget(self.delete_BTN)

        self.back_BTN = QPushButton(self.frame_5)
        self.back_BTN.setObjectName(u"back_BTN")
        sizePolicy1.setHeightForWidth(self.back_BTN.sizePolicy().hasHeightForWidth())
        self.back_BTN.setSizePolicy(sizePolicy1)
        self.back_BTN.setMinimumSize(QSize(80, 25))
        self.back_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold 12pt \"assets/font/monda.ttf\";\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.back_BTN.setFlat(True)

        self.horizontalLayout_3.addWidget(self.back_BTN)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.company_FRAME = QFrame(self.inputs)
        self.company_FRAME.setObjectName(u"company_FRAME")
        self.company_FRAME.setMinimumSize(QSize(0, 55))
        self.company_FRAME.setFrameShape(QFrame.NoFrame)
        self.company_FRAME.setFrameShadow(QFrame.Plain)
        self.gridLayout_7 = QGridLayout(self.company_FRAME)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.company_name_LBL = QLabel(self.company_FRAME)
        self.company_name_LBL.setObjectName(u"company_name_LBL")
        self.company_name_LBL.setStyleSheet(u"color: rgb(5, 55, 66);\n"
"font: bold 15pt \"assets/font/monda.ttf\";")
        self.company_name_LBL.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.company_name_LBL, 2, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_10, 1, 1, 1, 1)

        self.company_name_LE = QLineEdit(self.company_FRAME)
        self.company_name_LE.setObjectName(u"company_name_LE")
        self.company_name_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;\n"
"color: rgb(5, 55, 66);\n"
"font: bold 15pt \"assets/font/monda.ttf\";")
        self.company_name_LE.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.company_name_LE, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.company_FRAME)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.emp_SW = QStackedWidget(self.inputs)
        self.emp_SW.setObjectName(u"emp_SW")
        self.emp_SW.setStyleSheet(u"font: 11pt \"asstes/font/monda.ttf\" rgb(0,0,0);\n"
"border: 1px solid rgb(0,0,0);")
        self.input_SWP = QWidget()
        self.input_SWP.setObjectName(u"input_SWP")
        self.verticalLayout_4 = QVBoxLayout(self.input_SWP)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.frame_2 = QFrame(self.input_SWP)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"border: none;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.ln_emp_LE = QLineEdit(self.frame_2)
        self.ln_emp_LE.setObjectName(u"ln_emp_LE")
        self.ln_emp_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")

        self.gridLayout_5.addWidget(self.ln_emp_LE, 6, 1, 1, 1)

        self.mn_emp_LE = QLineEdit(self.frame_2)
        self.mn_emp_LE.setObjectName(u"mn_emp_LE")
        self.mn_emp_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")

        self.gridLayout_5.addWidget(self.mn_emp_LE, 5, 1, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border: none;")

        self.gridLayout_5.addWidget(self.label_11, 6, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: none;")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"border: none;")

        self.gridLayout_5.addWidget(self.label_5, 3, 0, 1, 1)

        self.id_emp_LE = QLineEdit(self.frame_2)
        self.id_emp_LE.setObjectName(u"id_emp_LE")
        self.id_emp_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")

        self.gridLayout_5.addWidget(self.id_emp_LE, 0, 1, 1, 1)

        self.total_deduction_LE = QLineEdit(self.frame_2)
        self.total_deduction_LE.setObjectName(u"total_deduction_LE")
        self.total_deduction_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.total_deduction_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.total_deduction_LE.setReadOnly(True)

        self.gridLayout_5.addWidget(self.total_deduction_LE, 5, 4, 1, 1)

        self.fn_emp_LE = QLineEdit(self.frame_2)
        self.fn_emp_LE.setObjectName(u"fn_emp_LE")
        self.fn_emp_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")

        self.gridLayout_5.addWidget(self.fn_emp_LE, 3, 1, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border: none;")

        self.gridLayout_5.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"border: none;")

        self.gridLayout_5.addWidget(self.label_29, 6, 2, 1, 1)

        self.net_pay_LE = QLineEdit(self.frame_2)
        self.net_pay_LE.setObjectName(u"net_pay_LE")
        self.net_pay_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.net_pay_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.net_pay_LE.setReadOnly(True)

        self.gridLayout_5.addWidget(self.net_pay_LE, 6, 4, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border: none;")

        self.gridLayout_5.addWidget(self.label_18, 5, 2, 1, 1)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border: none;")

        self.gridLayout_5.addWidget(self.label_17, 3, 2, 1, 1)

        self.gross_pay_LE = QLineEdit(self.frame_2)
        self.gross_pay_LE.setObjectName(u"gross_pay_LE")
        self.gross_pay_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.gross_pay_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gross_pay_LE.setReadOnly(True)

        self.gridLayout_5.addWidget(self.gross_pay_LE, 3, 4, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.input_SWP)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border: none;")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.rates = QFrame(self.frame_7)
        self.rates.setObjectName(u"rates")
        self.rates.setStyleSheet(u"border: none;")
        self.rates.setFrameShape(QFrame.NoFrame)
        self.rates.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.rates)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.frame_11 = QFrame(self.rates)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.night_worked_LE = QLineEdit(self.frame_11)
        self.night_worked_LE.setObjectName(u"night_worked_LE")
        self.night_worked_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")

        self.gridLayout_2.addWidget(self.night_worked_LE, 1, 3, 1, 1)

        self.label_40 = QLabel(self.frame_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_40, 3, 2, 1, 1)

        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.total_day_pay_LE = QLineEdit(self.frame_11)
        self.total_day_pay_LE.setObjectName(u"total_day_pay_LE")
        self.total_day_pay_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.total_day_pay_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.total_day_pay_LE.setReadOnly(True)

        self.gridLayout_2.addWidget(self.total_day_pay_LE, 0, 5, 1, 1)

        self.total_night_pay_LE = QLineEdit(self.frame_11)
        self.total_night_pay_LE.setObjectName(u"total_night_pay_LE")
        self.total_night_pay_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.total_night_pay_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.total_night_pay_LE.setReadOnly(True)

        self.gridLayout_2.addWidget(self.total_night_pay_LE, 1, 5, 1, 1)

        self.label_38 = QLabel(self.frame_11)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_38, 0, 2, 1, 1)

        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)

        self.day_worked_LE = QLineEdit(self.frame_11)
        self.day_worked_LE.setObjectName(u"day_worked_LE")
        self.day_worked_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")

        self.gridLayout_2.addWidget(self.day_worked_LE, 0, 3, 1, 1)

        self.ot_hours_LE = QLineEdit(self.frame_11)
        self.ot_hours_LE.setObjectName(u"ot_hours_LE")
        self.ot_hours_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")

        self.gridLayout_2.addWidget(self.ot_hours_LE, 3, 3, 1, 1)

        self.label_21 = QLabel(self.frame_11)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_21, 1, 4, 1, 1)

        self.day_rate_LE = QLineEdit(self.frame_11)
        self.day_rate_LE.setObjectName(u"day_rate_LE")
        self.day_rate_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.day_rate_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.day_rate_LE, 0, 1, 1, 1)

        self.label_39 = QLabel(self.frame_11)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_39, 1, 2, 1, 1)

        self.ot_rate_LE = QLineEdit(self.frame_11)
        self.ot_rate_LE.setObjectName(u"ot_rate_LE")
        self.ot_rate_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.ot_rate_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.ot_rate_LE, 3, 1, 1, 1)

        self.night_rate_LE = QLineEdit(self.frame_11)
        self.night_rate_LE.setObjectName(u"night_rate_LE")
        self.night_rate_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.night_rate_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.night_rate_LE, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_20, 0, 4, 1, 1)

        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)

        self.holiday_rate_LE = QLineEdit(self.frame_11)
        self.holiday_rate_LE.setObjectName(u"holiday_rate_LE")
        self.holiday_rate_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.holiday_rate_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.holiday_rate_LE, 2, 1, 1, 1)

        self.label_22 = QLabel(self.frame_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_22, 3, 4, 1, 1)

        self.total_ot_pay_LE = QLineEdit(self.frame_11)
        self.total_ot_pay_LE.setObjectName(u"total_ot_pay_LE")
        self.total_ot_pay_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.total_ot_pay_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.total_ot_pay_LE.setReadOnly(True)

        self.gridLayout_2.addWidget(self.total_ot_pay_LE, 3, 5, 1, 1)

        self.label_23 = QLabel(self.frame_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_23, 2, 4, 1, 1)

        self.total_holiday_pay_LE = QLineEdit(self.frame_11)
        self.total_holiday_pay_LE.setObjectName(u"total_holiday_pay_LE")
        self.total_holiday_pay_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.total_holiday_pay_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.total_holiday_pay_LE.setReadOnly(True)

        self.gridLayout_2.addWidget(self.total_holiday_pay_LE, 2, 5, 1, 1)

        self.label_19 = QLabel(self.frame_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.label_19, 2, 2, 1, 1)

        self.holiday_worked_LE = QLineEdit(self.frame_11)
        self.holiday_worked_LE.setObjectName(u"holiday_worked_LE")
        self.holiday_worked_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"padding: 2px;")
        self.holiday_worked_LE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.holiday_worked_LE, 2, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout_4.addWidget(self.rates)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border: none;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 3)

        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border: none;")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 3, 3)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.add_deduction_BTN = QPushButton(self.frame_14)
        self.add_deduction_BTN.setObjectName(u"add_deduction_BTN")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add_deduction_BTN.sizePolicy().hasHeightForWidth())
        self.add_deduction_BTN.setSizePolicy(sizePolicy2)
        self.add_deduction_BTN.setMinimumSize(QSize(25, 25))
        self.add_deduction_BTN.setMaximumSize(QSize(25, 25))
        self.add_deduction_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_deduction_BTN.setLayoutDirection(Qt.LeftToRight)
        self.add_deduction_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 12px;\n"
"	color: rgb(255, 255, 255);\n"
"	image: url(:/images/addition.png);\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.add_deduction_BTN.setFlat(True)

        self.horizontalLayout_6.addWidget(self.add_deduction_BTN)

        self.remove_deduction_BTN = QPushButton(self.frame_14)
        self.remove_deduction_BTN.setObjectName(u"remove_deduction_BTN")
        sizePolicy2.setHeightForWidth(self.remove_deduction_BTN.sizePolicy().hasHeightForWidth())
        self.remove_deduction_BTN.setSizePolicy(sizePolicy2)
        self.remove_deduction_BTN.setMinimumSize(QSize(25, 25))
        self.remove_deduction_BTN.setMaximumSize(QSize(25, 25))
        self.remove_deduction_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_deduction_BTN.setLayoutDirection(Qt.LeftToRight)
        self.remove_deduction_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 12px;\n"
"	color: rgb(255, 255, 255);\n"
"	image: url(:/images/subraction.png);\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.remove_deduction_BTN.setFlat(True)

        self.horizontalLayout_6.addWidget(self.remove_deduction_BTN)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.deductions_TBL = QTableWidget(self.frame_15)
        if (self.deductions_TBL.columnCount() < 2):
            self.deductions_TBL.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.deductions_TBL.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.deductions_TBL.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.deductions_TBL.setObjectName(u"deductions_TBL")
        sizePolicy2.setHeightForWidth(self.deductions_TBL.sizePolicy().hasHeightForWidth())
        self.deductions_TBL.setSizePolicy(sizePolicy2)
        self.deductions_TBL.setMinimumSize(QSize(250, 136))
        self.deductions_TBL.setStyleSheet(u"border: 1px solid rgb(0,0,0);")
        self.deductions_TBL.setFrameShape(QFrame.NoFrame)
        self.deductions_TBL.setFrameShadow(QFrame.Plain)
        self.deductions_TBL.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.deductions_TBL.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.deductions_TBL.setSortingEnabled(True)
        self.deductions_TBL.horizontalHeader().setStretchLastSection(True)
        self.deductions_TBL.verticalHeader().setVisible(False)

        self.horizontalLayout_7.addWidget(self.deductions_TBL)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_13)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_14)

        self.emp_SW.addWidget(self.input_SWP)
        self.summary_SWP = QWidget()
        self.summary_SWP.setObjectName(u"summary_SWP")
        self.gridLayout_3 = QGridLayout(self.summary_SWP)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.summary_SWP)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"color: rgb(5, 55, 66);\n"
"font: bold 20pt \"assets/font/monda.ttf\";\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.report_TBL = QTableWidget(self.summary_SWP)
        if (self.report_TBL.columnCount() < 19):
            self.report_TBL.setColumnCount(19)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(13, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(14, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(15, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(16, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(17, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.report_TBL.setHorizontalHeaderItem(18, __qtablewidgetitem20)
        self.report_TBL.setObjectName(u"report_TBL")
        self.report_TBL.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.report_TBL.setFrameShape(QFrame.NoFrame)
        self.report_TBL.setFrameShadow(QFrame.Plain)
        self.report_TBL.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.report_TBL.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.report_TBL.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.report_TBL.setSortingEnabled(True)
        self.report_TBL.horizontalHeader().setMinimumSectionSize(100)
        self.report_TBL.horizontalHeader().setDefaultSectionSize(100)
        self.report_TBL.horizontalHeader().setStretchLastSection(True)
        self.report_TBL.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.report_TBL, 1, 0, 1, 1)

        self.emp_SW.addWidget(self.summary_SWP)

        self.verticalLayout_3.addWidget(self.emp_SW)

        self.frame_10 = QFrame(self.inputs)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color:  rgb(0,0,0);\n"
"font: 11pt \"asstes/font/monda.ttf\";")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.prepared_by_LE = QLineEdit(self.frame_10)
        self.prepared_by_LE.setObjectName(u"prepared_by_LE")
        self.prepared_by_LE.setMaximumSize(QSize(255, 16777215))
        self.prepared_by_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"font: 12pt \"assets/font/monda.ttf\";\n"
"padding: 2px;")

        self.horizontalLayout_5.addWidget(self.prepared_by_LE)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:  rgb(0,0,0);\n"
"font: 11pt \"asstes/font/monda.ttf\";")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.period_LE = QLineEdit(self.frame_10)
        self.period_LE.setObjectName(u"period_LE")
        self.period_LE.setMaximumSize(QSize(255, 16777215))
        self.period_LE.setStyleSheet(u"border: none;\n"
"border-bottom: 1px solid rgb(0,0,0);\n"
"background-color: rgba(5, 55, 66, 50);\n"
"font: 12pt \"assets/font/monda.ttf\";\n"
"padding: 2px;")

        self.horizontalLayout_5.addWidget(self.period_LE)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.inputs)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.notification_LBL = QLabel(self.frame_4)
        self.notification_LBL.setObjectName(u"notification_LBL")
        self.notification_LBL.setStyleSheet(u"color:  rgb(0,0,0);\n"
"font: bold 11pt \"asstes/font/monda.ttf\";")
        self.notification_LBL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.notification_LBL)

        self.horizontalSpacer = QSpacerItem(607, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.export_BTN = QPushButton(self.frame_4)
        self.export_BTN.setObjectName(u"export_BTN")
        sizePolicy1.setHeightForWidth(self.export_BTN.sizePolicy().hasHeightForWidth())
        self.export_BTN.setSizePolicy(sizePolicy1)
        self.export_BTN.setMinimumSize(QSize(80, 25))
        self.export_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.export_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold 12pt \"assets/font/monda.ttf\";\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.export_BTN.setFlat(True)

        self.horizontalLayout_2.addWidget(self.export_BTN)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.inputs)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(20, 0))
        self.frame_6.setMaximumSize(QSize(20, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 0)
        self.open_calc_BTN = QPushButton(self.frame_6)
        self.open_calc_BTN.setObjectName(u"open_calc_BTN")
        sizePolicy1.setHeightForWidth(self.open_calc_BTN.sizePolicy().hasHeightForWidth())
        self.open_calc_BTN.setSizePolicy(sizePolicy1)
        self.open_calc_BTN.setMinimumSize(QSize(35, 50))
        self.open_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_calc_BTN.setLayoutDirection(Qt.LeftToRight)
        self.open_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(5, 55, 66);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	image: url(:/images/open.png);\n"
"	padding: 2px;\n"
"	padding-right: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding-right: 10px;\n"
"}")
        self.open_calc_BTN.setFlat(True)

        self.verticalLayout_8.addWidget(self.open_calc_BTN)

        self.verticalSpacer_12 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_12)


        self.horizontalLayout.addWidget(self.frame_6)

        self.calculator = QFrame(self.centralwidget)
        self.calculator.setObjectName(u"calculator")
        self.calculator.setMinimumSize(QSize(0, 0))
        self.calculator.setMaximumSize(QSize(400, 16777215))
        self.calculator.setStyleSheet(u"background-color: rgb(5, 55, 66);")
        self.calculator.setFrameShape(QFrame.StyledPanel)
        self.calculator.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.calculator)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.calculator)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: rgb(232, 240, 242);\n"
"font: bold 25pt \"assets/font/monda.ttf\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.cache_calc_BTN = QLineEdit(self.calculator)
        self.cache_calc_BTN.setObjectName(u"cache_calc_BTN")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cache_calc_BTN.sizePolicy().hasHeightForWidth())
        self.cache_calc_BTN.setSizePolicy(sizePolicy3)
        self.cache_calc_BTN.setMinimumSize(QSize(0, 30))
        self.cache_calc_BTN.setLayoutDirection(Qt.RightToLeft)
        self.cache_calc_BTN.setStyleSheet(u"color: rgb(157, 157, 157);\n"
"font:  15pt \"assets/font/monda.ttf\";\n"
"background-color: rgb(4, 41, 48);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.cache_calc_BTN.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.cache_calc_BTN.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.cache_calc_BTN)

        self.current_calc_LE = QLineEdit(self.calculator)
        self.current_calc_LE.setObjectName(u"current_calc_LE")
        self.current_calc_LE.setMinimumSize(QSize(0, 45))
        self.current_calc_LE.setCursor(QCursor(Qt.IBeamCursor))
        self.current_calc_LE.setLayoutDirection(Qt.RightToLeft)
        self.current_calc_LE.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font:  18pt \"assets/font/monda.ttf\";\n"
"border: 2px solid rgb(232, 240, 242);\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"")
        self.current_calc_LE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.current_calc_LE)

        self.frame_3 = QFrame(self.calculator)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calc_Btns = QFrame(self.frame_3)
        self.calc_Btns.setObjectName(u"calc_Btns")
        self.calc_Btns.setFrameShape(QFrame.NoFrame)
        self.calc_Btns.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.calc_Btns)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.zero_calc_BTN = QPushButton(self.calc_Btns)
        self.zero_calc_BTN.setObjectName(u"zero_calc_BTN")
        sizePolicy2.setHeightForWidth(self.zero_calc_BTN.sizePolicy().hasHeightForWidth())
        self.zero_calc_BTN.setSizePolicy(sizePolicy2)
        self.zero_calc_BTN.setMinimumSize(QSize(50, 50))
        self.zero_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.zero_calc_BTN.setStyleSheet(u"QPushButton{\n"
"padding: 2px;\n"
"color: rgb(232, 240, 242);\n"
"font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.zero_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.zero_calc_BTN, 4, 1, 1, 1)

        self.two_calc_BTN = QPushButton(self.calc_Btns)
        self.two_calc_BTN.setObjectName(u"two_calc_BTN")
        sizePolicy2.setHeightForWidth(self.two_calc_BTN.sizePolicy().hasHeightForWidth())
        self.two_calc_BTN.setSizePolicy(sizePolicy2)
        self.two_calc_BTN.setMinimumSize(QSize(50, 50))
        self.two_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.two_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.two_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.two_calc_BTN, 3, 1, 1, 1)

        self.decimal_calc_BTN = QPushButton(self.calc_Btns)
        self.decimal_calc_BTN.setObjectName(u"decimal_calc_BTN")
        sizePolicy2.setHeightForWidth(self.decimal_calc_BTN.sizePolicy().hasHeightForWidth())
        self.decimal_calc_BTN.setSizePolicy(sizePolicy2)
        self.decimal_calc_BTN.setMinimumSize(QSize(50, 50))
        self.decimal_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.decimal_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.decimal_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.decimal_calc_BTN, 4, 2, 1, 1)

        self.equal_calc_BTN = QPushButton(self.calc_Btns)
        self.equal_calc_BTN.setObjectName(u"equal_calc_BTN")
        sizePolicy2.setHeightForWidth(self.equal_calc_BTN.sizePolicy().hasHeightForWidth())
        self.equal_calc_BTN.setSizePolicy(sizePolicy2)
        self.equal_calc_BTN.setMinimumSize(QSize(50, 50))
        self.equal_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.equal_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	image: url(:/images/equal.png);\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.equal_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.equal_calc_BTN, 4, 3, 1, 1)

        self.seven_calc_BTN = QPushButton(self.calc_Btns)
        self.seven_calc_BTN.setObjectName(u"seven_calc_BTN")
        sizePolicy2.setHeightForWidth(self.seven_calc_BTN.sizePolicy().hasHeightForWidth())
        self.seven_calc_BTN.setSizePolicy(sizePolicy2)
        self.seven_calc_BTN.setMinimumSize(QSize(50, 50))
        self.seven_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.seven_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.seven_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.seven_calc_BTN, 1, 0, 1, 1)

        self.multiply_calc_BTN = QPushButton(self.calc_Btns)
        self.multiply_calc_BTN.setObjectName(u"multiply_calc_BTN")
        sizePolicy2.setHeightForWidth(self.multiply_calc_BTN.sizePolicy().hasHeightForWidth())
        self.multiply_calc_BTN.setSizePolicy(sizePolicy2)
        self.multiply_calc_BTN.setMinimumSize(QSize(50, 50))
        self.multiply_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.multiply_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	image: url(:/images/multiply.png);\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.multiply_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.multiply_calc_BTN, 1, 3, 1, 1)

        self.division_calc_BTN = QPushButton(self.calc_Btns)
        self.division_calc_BTN.setObjectName(u"division_calc_BTN")
        sizePolicy2.setHeightForWidth(self.division_calc_BTN.sizePolicy().hasHeightForWidth())
        self.division_calc_BTN.setSizePolicy(sizePolicy2)
        self.division_calc_BTN.setMinimumSize(QSize(50, 50))
        self.division_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.division_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	image: url(:/images/divide.png);\n"
"	padding: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.division_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.division_calc_BTN, 0, 3, 1, 1)

        self.five_calc_BTN = QPushButton(self.calc_Btns)
        self.five_calc_BTN.setObjectName(u"five_calc_BTN")
        sizePolicy2.setHeightForWidth(self.five_calc_BTN.sizePolicy().hasHeightForWidth())
        self.five_calc_BTN.setSizePolicy(sizePolicy2)
        self.five_calc_BTN.setMinimumSize(QSize(50, 50))
        self.five_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.five_calc_BTN.setStyleSheet(u"QPushButton{\n"
"padding: 2px;\n"
"color: rgb(232, 240, 242);\n"
"font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.five_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.five_calc_BTN, 2, 1, 1, 1)

        self.addition_calc_BTN = QPushButton(self.calc_Btns)
        self.addition_calc_BTN.setObjectName(u"addition_calc_BTN")
        sizePolicy2.setHeightForWidth(self.addition_calc_BTN.sizePolicy().hasHeightForWidth())
        self.addition_calc_BTN.setSizePolicy(sizePolicy2)
        self.addition_calc_BTN.setMinimumSize(QSize(50, 50))
        self.addition_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.addition_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	image: url(:/images/addition.png);\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.addition_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.addition_calc_BTN, 3, 3, 1, 1)

        self.nine_calc_BTN = QPushButton(self.calc_Btns)
        self.nine_calc_BTN.setObjectName(u"nine_calc_BTN")
        sizePolicy2.setHeightForWidth(self.nine_calc_BTN.sizePolicy().hasHeightForWidth())
        self.nine_calc_BTN.setSizePolicy(sizePolicy2)
        self.nine_calc_BTN.setMinimumSize(QSize(50, 50))
        self.nine_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.nine_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.nine_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.nine_calc_BTN, 1, 2, 1, 1)

        self.percent_calc_BTN = QPushButton(self.calc_Btns)
        self.percent_calc_BTN.setObjectName(u"percent_calc_BTN")
        sizePolicy2.setHeightForWidth(self.percent_calc_BTN.sizePolicy().hasHeightForWidth())
        self.percent_calc_BTN.setSizePolicy(sizePolicy2)
        self.percent_calc_BTN.setMinimumSize(QSize(50, 50))
        self.percent_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.percent_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	image: url(:/images/percent.png);\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.percent_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.percent_calc_BTN, 4, 0, 1, 1)

        self.subtraction_calc_BTN = QPushButton(self.calc_Btns)
        self.subtraction_calc_BTN.setObjectName(u"subtraction_calc_BTN")
        sizePolicy2.setHeightForWidth(self.subtraction_calc_BTN.sizePolicy().hasHeightForWidth())
        self.subtraction_calc_BTN.setSizePolicy(sizePolicy2)
        self.subtraction_calc_BTN.setMinimumSize(QSize(50, 50))
        self.subtraction_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.subtraction_calc_BTN.setStyleSheet(u"QPushButton{\n"
"padding: 2px;\n"
"image: url(:/images/subraction.png)\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.subtraction_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.subtraction_calc_BTN, 2, 3, 1, 1)

        self.clear_mem_calc_BTN = QPushButton(self.calc_Btns)
        self.clear_mem_calc_BTN.setObjectName(u"clear_mem_calc_BTN")
        sizePolicy2.setHeightForWidth(self.clear_mem_calc_BTN.sizePolicy().hasHeightForWidth())
        self.clear_mem_calc_BTN.setSizePolicy(sizePolicy2)
        self.clear_mem_calc_BTN.setMinimumSize(QSize(50, 50))
        self.clear_mem_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_mem_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"	padding: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.clear_mem_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.clear_mem_calc_BTN, 0, 1, 1, 1)

        self.eight_calc_BTN = QPushButton(self.calc_Btns)
        self.eight_calc_BTN.setObjectName(u"eight_calc_BTN")
        sizePolicy2.setHeightForWidth(self.eight_calc_BTN.sizePolicy().hasHeightForWidth())
        self.eight_calc_BTN.setSizePolicy(sizePolicy2)
        self.eight_calc_BTN.setMinimumSize(QSize(50, 50))
        self.eight_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.eight_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.eight_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.eight_calc_BTN, 1, 1, 1, 1)

        self.six_calc_BTN = QPushButton(self.calc_Btns)
        self.six_calc_BTN.setObjectName(u"six_calc_BTN")
        sizePolicy2.setHeightForWidth(self.six_calc_BTN.sizePolicy().hasHeightForWidth())
        self.six_calc_BTN.setSizePolicy(sizePolicy2)
        self.six_calc_BTN.setMinimumSize(QSize(50, 50))
        self.six_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.six_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.six_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.six_calc_BTN, 2, 2, 1, 1)

        self.pos_neg_calc_BTN = QPushButton(self.calc_Btns)
        self.pos_neg_calc_BTN.setObjectName(u"pos_neg_calc_BTN")
        sizePolicy2.setHeightForWidth(self.pos_neg_calc_BTN.sizePolicy().hasHeightForWidth())
        self.pos_neg_calc_BTN.setSizePolicy(sizePolicy2)
        self.pos_neg_calc_BTN.setMinimumSize(QSize(50, 50))
        self.pos_neg_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.pos_neg_calc_BTN.setStyleSheet(u"QPushButton{\n"
"image:url(:/images/pos_neg.png);\n"
"padding: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.pos_neg_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.pos_neg_calc_BTN, 0, 2, 1, 1)

        self.clear_calc_BTN = QPushButton(self.calc_Btns)
        self.clear_calc_BTN.setObjectName(u"clear_calc_BTN")
        sizePolicy2.setHeightForWidth(self.clear_calc_BTN.sizePolicy().hasHeightForWidth())
        self.clear_calc_BTN.setSizePolicy(sizePolicy2)
        self.clear_calc_BTN.setMinimumSize(QSize(50, 50))
        self.clear_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	image: url(:/images/clear.png);\n"
"	padding: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.clear_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.clear_calc_BTN, 0, 0, 1, 1)

        self.one_calc_BTN = QPushButton(self.calc_Btns)
        self.one_calc_BTN.setObjectName(u"one_calc_BTN")
        sizePolicy2.setHeightForWidth(self.one_calc_BTN.sizePolicy().hasHeightForWidth())
        self.one_calc_BTN.setSizePolicy(sizePolicy2)
        self.one_calc_BTN.setMinimumSize(QSize(50, 50))
        self.one_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.one_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.one_calc_BTN, 3, 2, 1, 1)

        self.four_calc_BTN = QPushButton(self.calc_Btns)
        self.four_calc_BTN.setObjectName(u"four_calc_BTN")
        sizePolicy2.setHeightForWidth(self.four_calc_BTN.sizePolicy().hasHeightForWidth())
        self.four_calc_BTN.setSizePolicy(sizePolicy2)
        self.four_calc_BTN.setMinimumSize(QSize(50, 50))
        self.four_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.four_calc_BTN.setStyleSheet(u"QPushButton{\n"
"padding: 2px;\n"
"color: rgb(232, 240, 242);\n"
"font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.four_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.four_calc_BTN, 2, 0, 1, 1)

        self.three_calc_BTN = QPushButton(self.calc_Btns)
        self.three_calc_BTN.setObjectName(u"three_calc_BTN")
        sizePolicy2.setHeightForWidth(self.three_calc_BTN.sizePolicy().hasHeightForWidth())
        self.three_calc_BTN.setSizePolicy(sizePolicy2)
        self.three_calc_BTN.setMinimumSize(QSize(50, 50))
        self.three_calc_BTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.three_calc_BTN.setStyleSheet(u"QPushButton{\n"
"	padding: 2px;\n"
"	color: rgb(232, 240, 242);\n"
"	font:  19pt \"assets/font/monda.ttf\";\n"
"}\n"
"QPushButton:hover{\n"
"	padding: 7px;\n"
"	border: rgb(232, 240, 242);\n"
"	border-radius:5px;\n"
"	background-color:rgb(57, 162, 219) ;\n"
"}")
        self.three_calc_BTN.setFlat(True)

        self.gridLayout.addWidget(self.three_calc_BTN, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.calc_Btns)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.calculator)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.emp_SW.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mugna", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EMPLOYEE INFORMATION", None))
        self.clear_BTN.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.add_BTN.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.report_BTN.setText(QCoreApplication.translate("MainWindow", u"REPORT", None))
        self.delete_BTN.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.back_BTN.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.company_name_LBL.setText(QCoreApplication.translate("MainWindow", u"Company Name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.total_deduction_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.00", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Net Pay", None))
        self.net_pay_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.00", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total Deduction", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Gross Pay", None))
        self.gross_pay_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.00", None))
        self.night_worked_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Hour Worked", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Day Shift Hourly Rate", None))
        self.total_day_pay_LE.setInputMask("")
        self.total_day_pay_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.00", None))
        self.total_night_pay_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.00", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Hour Worked", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Overtime Rate", None))
        self.day_worked_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.ot_hours_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total Night Shift Pay", None))
        self.day_rate_LE.setInputMask("")
        self.day_rate_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.0", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Hour Worked", None))
        self.ot_rate_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.0", None))
        self.night_rate_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Total Day Shift Pay", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Night Shift Hourly Rate", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Holiday Hourly Rate", None))
        self.holiday_rate_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.0", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Total OT Pay", None))
        self.total_ot_pay_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.00", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Total Holiday Pay", None))
        self.total_holiday_pay_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000.00", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Hour Worked", None))
        self.holiday_worked_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.add_deduction_BTN.setText("")
        self.remove_deduction_BTN.setText("")
        ___qtablewidgetitem = self.deductions_TBL.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Deductions", None));
        ___qtablewidgetitem1 = self.deductions_TBL.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SUMMARY REPORT", None))
        ___qtablewidgetitem2 = self.report_TBL.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem3 = self.report_TBL.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem4 = self.report_TBL.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None));
        ___qtablewidgetitem5 = self.report_TBL.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem6 = self.report_TBL.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Day Shift Hourly Rate", None));
        ___qtablewidgetitem7 = self.report_TBL.horizontalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Night Shift Hourly Rate", None));
        ___qtablewidgetitem8 = self.report_TBL.horizontalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Holiday Hourly Rate", None));
        ___qtablewidgetitem9 = self.report_TBL.horizontalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"OT Rate", None));
        ___qtablewidgetitem10 = self.report_TBL.horizontalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Day Shift Hour(s) Worked", None));
        ___qtablewidgetitem11 = self.report_TBL.horizontalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Night Shift Hour(s) Worked", None));
        ___qtablewidgetitem12 = self.report_TBL.horizontalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Holiday Hour(s) Worked", None));
        ___qtablewidgetitem13 = self.report_TBL.horizontalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"OT Hour(s) Worked", None));
        ___qtablewidgetitem14 = self.report_TBL.horizontalHeaderItem(12)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Total Day Shift Pay", None));
        ___qtablewidgetitem15 = self.report_TBL.horizontalHeaderItem(13)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Total Night Night Pay", None));
        ___qtablewidgetitem16 = self.report_TBL.horizontalHeaderItem(14)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Total Holiday Pay", None));
        ___qtablewidgetitem17 = self.report_TBL.horizontalHeaderItem(15)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Total OT Pay", None));
        ___qtablewidgetitem18 = self.report_TBL.horizontalHeaderItem(16)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Gross Pay", None));
        ___qtablewidgetitem19 = self.report_TBL.horizontalHeaderItem(17)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Total Deduction", None));
        ___qtablewidgetitem20 = self.report_TBL.horizontalHeaderItem(18)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Net Pay", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Prepared By: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Period:", None))
        self.period_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mm dd, yyyy - mm dd, yyyy", None))
        self.notification_LBL.setText("")
        self.export_BTN.setText(QCoreApplication.translate("MainWindow", u"EXPORT", None))
        self.open_calc_BTN.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"CALCULATOR", None))
        self.cache_calc_BTN.setText("")
        self.zero_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.zero_calc_BTN.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.two_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.two_calc_BTN.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.decimal_calc_BTN.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.decimal_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.equal_calc_BTN.setText("")
#if QT_CONFIG(shortcut)
        self.equal_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.seven_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.multiply_calc_BTN.setText("")
#if QT_CONFIG(shortcut)
        self.multiply_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.division_calc_BTN.setText("")
#if QT_CONFIG(shortcut)
        self.division_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.five_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.five_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.addition_calc_BTN.setText("")
        self.nine_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.percent_calc_BTN.setText("")
#if QT_CONFIG(shortcut)
        self.percent_calc_BTN.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.subtraction_calc_BTN.setText("")
#if QT_CONFIG(shortcut)
        self.subtraction_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.clear_mem_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.clear_mem_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.eight_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.eight_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.six_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.six_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.pos_neg_calc_BTN.setText("")
        self.clear_calc_BTN.setText("")
#if QT_CONFIG(shortcut)
        self.clear_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.one_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.four_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.four_calc_BTN.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.three_calc_BTN.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.three_calc_BTN.setShortcut("")
#endif // QT_CONFIG(shortcut)
    # retranslateUi

