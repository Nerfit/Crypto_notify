# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1113, 595)
        MainWindow.setMinimumSize(QSize(1113, 595))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QHBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame {\n"
"background-color: rgb(42, 44, 110);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.verticalLayout_15 = QVBoxLayout(self.frame_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 35))
        self.frame_6.setMaximumSize(QSize(16777215, 999))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"background-color: rgb(42, 44, 110);\n"
"border-top-left-radius: 10px;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 0, 0, 0)
        self.label_title_2 = QLabel(self.frame_6)
        self.label_title_2.setObjectName(u"label_title_2")
        font = QFont()
        font.setFamily(u"Gill Sans Nova")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet(u"color: #94ffbf;")
        self.label_title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_title_2)


        self.verticalLayout_15.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.575269 rgba(28, 29, 73, 255));\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 30)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.btn_ETH = QPushButton(self.frame_7)
        self.btn_ETH.setObjectName(u"btn_ETH")
        self.btn_ETH.setMinimumSize(QSize(50, 30))
        self.btn_ETH.setMaximumSize(QSize(50, 30))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_ETH.setFont(font1)
        self.btn_ETH.setStyleSheet(u"QPushButton{\n"
"	background-color: #59abf7;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #000\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #7bbcf9;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #2992f5;\n"
"	border: 1px solid #63b0f8;\n"
"}")
        self.btn_ETH.setFlat(False)

        self.verticalLayout_13.addWidget(self.btn_ETH, 0, Qt.AlignHCenter)

        self.btn_BTC = QPushButton(self.frame_7)
        self.btn_BTC.setObjectName(u"btn_BTC")
        self.btn_BTC.setMinimumSize(QSize(50, 30))
        self.btn_BTC.setMaximumSize(QSize(50, 30))
        self.btn_BTC.setFont(font1)
        self.btn_BTC.setStyleSheet(u"QPushButton{\n"
"	background-color: #59abf7;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #000\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #7bbcf9;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #2992f5;\n"
"	border: 1px solid #63b0f8;\n"
"}")
        self.btn_BTC.setFlat(False)

        self.verticalLayout_13.addWidget(self.btn_BTC, 0, Qt.AlignHCenter)

        self.btn_XLM = QPushButton(self.frame_7)
        self.btn_XLM.setObjectName(u"btn_XLM")
        self.btn_XLM.setMinimumSize(QSize(50, 30))
        self.btn_XLM.setMaximumSize(QSize(50, 30))
        self.btn_XLM.setFont(font1)
        self.btn_XLM.setStyleSheet(u"QPushButton{\n"
"	background-color: #59abf7;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #000\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #7bbcf9;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #2992f5;\n"
"	border: 1px solid #63b0f8;\n"
"}")
        self.btn_XLM.setFlat(False)

        self.verticalLayout_13.addWidget(self.btn_XLM, 0, Qt.AlignHCenter)

        self.btn_XRP = QPushButton(self.frame_7)
        self.btn_XRP.setObjectName(u"btn_XRP")
        self.btn_XRP.setMinimumSize(QSize(50, 30))
        self.btn_XRP.setMaximumSize(QSize(50, 30))
        self.btn_XRP.setFont(font1)
        self.btn_XRP.setStyleSheet(u"QPushButton{\n"
"	background-color: #59abf7;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #000\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #7bbcf9;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #2992f5;\n"
"	border: 1px solid #63b0f8;\n"
"}")
        self.btn_XRP.setFlat(False)

        self.verticalLayout_13.addWidget(self.btn_XRP, 0, Qt.AlignHCenter)

        self.btn_custom = QPushButton(self.frame_7)
        self.btn_custom.setObjectName(u"btn_custom")
        self.btn_custom.setMinimumSize(QSize(50, 30))
        self.btn_custom.setMaximumSize(QSize(50, 30))
        self.btn_custom.setFont(font1)
        self.btn_custom.setStyleSheet(u"QPushButton{\n"
"	background-color: #59abf7;\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #000\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #7bbcf9;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #2992f5;\n"
"	border: 1px solid #63b0f8;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/paczka/SVG/write.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_custom.setIcon(icon)
        self.btn_custom.setFlat(False)

        self.verticalLayout_13.addWidget(self.btn_custom, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)


        self.verticalLayout_15.addWidget(self.frame_7)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.drop_shadow_frame = QFrame(self.frame)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"QFrame {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.575269 rgba(28, 29, 73, 255));\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 35))
        self.title_bar.setStyleSheet(u"QFrame {\n"
"background-color: rgb(42, 44, 110);\n"
"\n"
"}\n"
"\n"
"")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 35))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: #94c6ff;")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(16, 16))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_minimize, 0, Qt.AlignVCenter)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(16, 16))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(85, 255, 127, 156);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_currency = QFrame(self.content_bar)
        self.frame_currency.setObjectName(u"frame_currency")
        self.frame_currency.setMaximumSize(QSize(16777215, 50))
        self.frame_currency.setFrameShape(QFrame.StyledPanel)
        self.frame_currency.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_currency)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_start = QPushButton(self.frame_currency)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(70, 30))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_start.setFont(font2)
        self.btn_start.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 207, 180);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #FFF\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(133, 224, 208);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(40, 159, 137);\n"
"	border: 1px solid #252660;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#64747d;\n"
"}")
        self.btn_start.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btn_start)

        self.horizontalSpacer_3 = QSpacerItem(50, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_34 = QLabel(self.frame_currency)
        self.label_34.setObjectName(u"label_34")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_34)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label_status = QLabel(self.frame_currency)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setFont(font3)
        self.label_status.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_status)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.label_status_time = QLabel(self.frame_currency)
        self.label_status_time.setObjectName(u"label_status_time")
        self.label_status_time.setFont(font3)
        self.label_status_time.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_status_time)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.spinbox_percent_price = QDoubleSpinBox(self.frame_currency)
        self.spinbox_percent_price.setObjectName(u"spinbox_percent_price")
        self.spinbox_percent_price.setMinimumSize(QSize(0, 30))
        self.spinbox_percent_price.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Gill Sans Nova Light")
        font4.setPointSize(10)
        self.spinbox_percent_price.setFont(font4)
        self.spinbox_percent_price.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 1px solid #757aff;\n"
"background : white;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 1px solid #75d1ff;\n"
"background : white;\n"
"}")
        self.spinbox_percent_price.setDecimals(2)
        self.spinbox_percent_price.setMaximum(1000.000000000000000)
        self.spinbox_percent_price.setSingleStep(0.500000000000000)

        self.horizontalLayout_6.addWidget(self.spinbox_percent_price)

        self.btn_add_alert_low = QPushButton(self.frame_currency)
        self.btn_add_alert_low.setObjectName(u"btn_add_alert_low")
        self.btn_add_alert_low.setEnabled(False)
        self.btn_add_alert_low.setMinimumSize(QSize(57, 30))
        self.btn_add_alert_low.setMaximumSize(QSize(57, 30))
        self.btn_add_alert_low.setFont(font1)
        self.btn_add_alert_low.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 207, 180);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #FFF\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(133, 224, 208);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(40, 159, 137);\n"
"	border: 1px solid #252660;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#64747d;\n"
"}")
        self.btn_add_alert_low.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btn_add_alert_low)

        self.btn_add_alert_high = QPushButton(self.frame_currency)
        self.btn_add_alert_high.setObjectName(u"btn_add_alert_high")
        self.btn_add_alert_high.setEnabled(False)
        self.btn_add_alert_high.setMinimumSize(QSize(57, 30))
        self.btn_add_alert_high.setMaximumSize(QSize(57, 30))
        self.btn_add_alert_high.setFont(font1)
        self.btn_add_alert_high.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 207, 180);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #FFF\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(133, 224, 208);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(40, 159, 137);\n"
"	border: 1px solid #252660;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#64747d;\n"
"}")
        self.btn_add_alert_high.setFlat(False)

        self.horizontalLayout_6.addWidget(self.btn_add_alert_high)


        self.verticalLayout_4.addWidget(self.frame_currency)

        self.frame_2 = QFrame(self.content_bar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(30, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(11, 10, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget{\n"
"background-color: none;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.page_ETH = QWidget()
        self.page_ETH.setObjectName(u"page_ETH")
        self.verticalLayout_5 = QVBoxLayout(self.page_ETH)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_ETH)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_33 = QLabel(self.frame_content_home)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 100))
        font5 = QFont()
        font5.setFamily(u"Gill Sans Nova Light")
        font5.setPointSize(16)
        self.label_33.setFont(font5)
        self.label_33.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_33)

        self.frame_infos = QFrame(self.frame_content_home)
        self.frame_infos.setObjectName(u"frame_infos")
        self.frame_infos.setFrameShape(QFrame.StyledPanel)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_infos)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_circle_1 = QFrame(self.frame_infos)
        self.frame_circle_1.setObjectName(u"frame_circle_1")
        self.frame_circle_1.setMinimumSize(QSize(200, 200))
        self.frame_circle_1.setMaximumSize(QSize(200, 200))
        self.frame_circle_1.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(63, 207, 180);\n"
"border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(118, 152, 146)\n"
"\n"
"}")
        self.frame_circle_1.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 35, 10, 35)
        self.label = QLabel(self.frame_circle_1)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Light")
        font6.setPointSize(11)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.label_bid_ETH = QLabel(self.frame_circle_1)
        self.label_bid_ETH.setObjectName(u"label_bid_ETH")
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Light")
        font7.setPointSize(30)
        self.label_bid_ETH.setFont(font7)
        self.label_bid_ETH.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_bid_ETH.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_bid_ETH)

        self.label_4 = QLabel(self.frame_circle_1)
        self.label_4.setObjectName(u"label_4")
        font8 = QFont()
        font8.setFamily(u"Bahnschrift Light")
        font8.setPointSize(10)
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_4.addWidget(self.frame_circle_1)

        self.frame_circle_2 = QFrame(self.frame_infos)
        self.frame_circle_2.setObjectName(u"frame_circle_2")
        self.frame_circle_2.setMinimumSize(QSize(250, 250))
        self.frame_circle_2.setMaximumSize(QSize(250, 250))
        self.frame_circle_2.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(255, 238, 0);\n"
"border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(105, 95, 148)\n"
"\n"
"}")
        self.frame_circle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_circle_2)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 35, 10, 35)
        self.label_5 = QLabel(self.frame_circle_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"border: none;\n"
"color: rgb(255, 238, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_last_ETH = QLabel(self.frame_circle_2)
        self.label_last_ETH.setObjectName(u"label_last_ETH")
        font9 = QFont()
        font9.setFamily(u"Bahnschrift Light")
        font9.setPointSize(40)
        self.label_last_ETH.setFont(font9)
        self.label_last_ETH.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_last_ETH.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_last_ETH)

        self.label_8 = QLabel(self.frame_circle_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.horizontalLayout_4.addWidget(self.frame_circle_2)

        self.frame_circle_3 = QFrame(self.frame_infos)
        self.frame_circle_3.setObjectName(u"frame_circle_3")
        self.frame_circle_3.setMinimumSize(QSize(200, 200))
        self.frame_circle_3.setMaximumSize(QSize(200, 200))
        self.frame_circle_3.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(253, 42, 71);\n"
"border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(170, 125, 131)\n"
"\n"
"}")
        self.frame_circle_3.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_circle_3)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 35, 10, 35)
        self.label_9 = QLabel(self.frame_circle_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"border: none;\n"
"color: rgb(253, 42, 71);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.label_ask_ETH = QLabel(self.frame_circle_3)
        self.label_ask_ETH.setObjectName(u"label_ask_ETH")
        self.label_ask_ETH.setFont(font7)
        self.label_ask_ETH.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_ask_ETH.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_ask_ETH)

        self.label_12 = QLabel(self.frame_circle_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_12)


        self.horizontalLayout_4.addWidget(self.frame_circle_3)


        self.verticalLayout_9.addWidget(self.frame_infos, 0, Qt.AlignVCenter)

        self.frame_text = QFrame(self.frame_content_home)
        self.frame_text.setObjectName(u"frame_text")
        self.frame_text.setMinimumSize(QSize(600, 0))
        self.frame_text.setMaximumSize(QSize(16777215, 100))
        self.frame_text.setFrameShape(QFrame.StyledPanel)
        self.frame_text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_text)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_13 = QLabel(self.frame_text)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 40))
        self.label_13.setMaximumSize(QSize(600, 50))
        font10 = QFont()
        font10.setFamily(u"Bahnschrift Light")
        font10.setPointSize(14)
        font10.setBold(False)
        font10.setWeight(50)
        self.label_13.setFont(font10)
        self.label_13.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(35, 33, 75);\n"
"border-radius: 10px;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addWidget(self.frame_text, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.page_ETH)
        self.page_BTC = QWidget()
        self.page_BTC.setObjectName(u"page_BTC")
        self.verticalLayout_11 = QVBoxLayout(self.page_BTC)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.page_BTC)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 100))
        font11 = QFont()
        font11.setFamily(u"Bahnschrift Light")
        font11.setPointSize(16)
        self.label_32.setFont(font11)
        self.label_32.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_32)

        self.frame_content_home_2 = QFrame(self.page_BTC)
        self.frame_content_home_2.setObjectName(u"frame_content_home_2")
        self.frame_content_home_2.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_content_home_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_infos_2 = QFrame(self.frame_content_home_2)
        self.frame_infos_2.setObjectName(u"frame_infos_2")
        self.frame_infos_2.setFrameShape(QFrame.StyledPanel)
        self.frame_infos_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_infos_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_circle_4 = QFrame(self.frame_infos_2)
        self.frame_circle_4.setObjectName(u"frame_circle_4")
        self.frame_circle_4.setMinimumSize(QSize(200, 200))
        self.frame_circle_4.setMaximumSize(QSize(200, 200))
        self.frame_circle_4.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(63, 207, 180);\n"
"border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(118, 152, 146)\n"
"\n"
"}")
        self.frame_circle_4.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_circle_4)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(10, 35, 10, 35)
        self.label_2 = QLabel(self.frame_circle_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_2)

        self.label_bid_BTC = QLabel(self.frame_circle_4)
        self.label_bid_BTC.setObjectName(u"label_bid_BTC")
        font12 = QFont()
        font12.setFamily(u"Bahnschrift Light")
        font12.setPointSize(25)
        self.label_bid_BTC.setFont(font12)
        self.label_bid_BTC.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_bid_BTC.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_bid_BTC)

        self.label_6 = QLabel(self.frame_circle_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_6)


        self.horizontalLayout_14.addWidget(self.frame_circle_4)

        self.frame_circle_5 = QFrame(self.frame_infos_2)
        self.frame_circle_5.setObjectName(u"frame_circle_5")
        self.frame_circle_5.setMinimumSize(QSize(250, 250))
        self.frame_circle_5.setMaximumSize(QSize(250, 250))
        self.frame_circle_5.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(255, 238, 0);\n"
"border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(105, 95, 148)\n"
"\n"
"}")
        self.frame_circle_5.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_circle_5)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(10, 35, 10, 35)
        self.label_7 = QLabel(self.frame_circle_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"border: none;\n"
"color: rgb(255, 238, 0);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_7)

        self.label_last_BTC = QLabel(self.frame_circle_5)
        self.label_last_BTC.setObjectName(u"label_last_BTC")
        font13 = QFont()
        font13.setFamily(u"Bahnschrift Light")
        font13.setPointSize(31)
        self.label_last_BTC.setFont(font13)
        self.label_last_BTC.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_last_BTC.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_last_BTC)

        self.label_10 = QLabel(self.frame_circle_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font8)
        self.label_10.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_10)


        self.horizontalLayout_14.addWidget(self.frame_circle_5)

        self.frame_circle_6 = QFrame(self.frame_infos_2)
        self.frame_circle_6.setObjectName(u"frame_circle_6")
        self.frame_circle_6.setMinimumSize(QSize(200, 200))
        self.frame_circle_6.setMaximumSize(QSize(200, 200))
        self.frame_circle_6.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(253, 42, 71);\n"
"border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(170, 125, 131)\n"
"\n"
"}")
        self.frame_circle_6.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_circle_6)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 35, 10, 35)
        self.label_11 = QLabel(self.frame_circle_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"border: none;\n"
"color: rgb(253, 42, 71);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_11)

        self.label_ask_BTC = QLabel(self.frame_circle_6)
        self.label_ask_BTC.setObjectName(u"label_ask_BTC")
        self.label_ask_BTC.setFont(font12)
        self.label_ask_BTC.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_ask_BTC.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_ask_BTC)

        self.label_14 = QLabel(self.frame_circle_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font8)
        self.label_14.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_14)


        self.horizontalLayout_14.addWidget(self.frame_circle_6)


        self.verticalLayout_22.addWidget(self.frame_infos_2, 0, Qt.AlignVCenter)

        self.frame_text_2 = QFrame(self.frame_content_home_2)
        self.frame_text_2.setObjectName(u"frame_text_2")
        self.frame_text_2.setMinimumSize(QSize(600, 0))
        self.frame_text_2.setMaximumSize(QSize(16777215, 100))
        self.frame_text_2.setFrameShape(QFrame.StyledPanel)
        self.frame_text_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_text_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_15 = QLabel(self.frame_text_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 40))
        self.label_15.setMaximumSize(QSize(600, 50))
        font14 = QFont()
        font14.setFamily(u"Bahnschrift Light")
        font14.setPointSize(14)
        self.label_15.setFont(font14)
        self.label_15.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(35, 33, 75);\n"
"border-radius: 10px;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_15)


        self.verticalLayout_22.addWidget(self.frame_text_2, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_content_home_2)

        self.stackedWidget.addWidget(self.page_BTC)
        self.page_XLM = QWidget()
        self.page_XLM.setObjectName(u"page_XLM")
        self.verticalLayout_37 = QVBoxLayout(self.page_XLM)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.page_XLM)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 100))
        self.label_31.setFont(font11)
        self.label_31.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_31)

        self.frame_content_home_3 = QFrame(self.page_XLM)
        self.frame_content_home_3.setObjectName(u"frame_content_home_3")
        self.frame_content_home_3.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_content_home_3)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_infos_3 = QFrame(self.frame_content_home_3)
        self.frame_infos_3.setObjectName(u"frame_infos_3")
        self.frame_infos_3.setFrameShape(QFrame.StyledPanel)
        self.frame_infos_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_infos_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_circle_7 = QFrame(self.frame_infos_3)
        self.frame_circle_7.setObjectName(u"frame_circle_7")
        self.frame_circle_7.setMinimumSize(QSize(200, 200))
        self.frame_circle_7.setMaximumSize(QSize(200, 200))
        self.frame_circle_7.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(63, 207, 180);\n"
"border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(118, 152, 146)\n"
"\n"
"}")
        self.frame_circle_7.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_circle_7)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(10, 35, 10, 35)
        self.label_3 = QLabel(self.frame_circle_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_3)

        self.label_bid_XLM = QLabel(self.frame_circle_7)
        self.label_bid_XLM.setObjectName(u"label_bid_XLM")
        font15 = QFont()
        font15.setFamily(u"Bahnschrift Light")
        font15.setPointSize(45)
        self.label_bid_XLM.setFont(font15)
        self.label_bid_XLM.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_bid_XLM.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_bid_XLM)

        self.label_16 = QLabel(self.frame_circle_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_16)


        self.horizontalLayout_15.addWidget(self.frame_circle_7)

        self.frame_circle_8 = QFrame(self.frame_infos_3)
        self.frame_circle_8.setObjectName(u"frame_circle_8")
        self.frame_circle_8.setMinimumSize(QSize(250, 250))
        self.frame_circle_8.setMaximumSize(QSize(250, 250))
        self.frame_circle_8.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(255, 238, 0);\n"
"border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(105, 95, 148)\n"
"\n"
"}")
        self.frame_circle_8.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_circle_8)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, 35, 10, 35)
        self.label_17 = QLabel(self.frame_circle_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font6)
        self.label_17.setStyleSheet(u"border: none;\n"
"color: rgb(255, 238, 0);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_17)

        self.label_last_XLM = QLabel(self.frame_circle_8)
        self.label_last_XLM.setObjectName(u"label_last_XLM")
        font16 = QFont()
        font16.setFamily(u"Bahnschrift Light")
        font16.setPointSize(60)
        self.label_last_XLM.setFont(font16)
        self.label_last_XLM.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_last_XLM.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_last_XLM)

        self.label_18 = QLabel(self.frame_circle_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_18)


        self.horizontalLayout_15.addWidget(self.frame_circle_8)

        self.frame_circle_9 = QFrame(self.frame_infos_3)
        self.frame_circle_9.setObjectName(u"frame_circle_9")
        self.frame_circle_9.setMinimumSize(QSize(200, 200))
        self.frame_circle_9.setMaximumSize(QSize(200, 200))
        self.frame_circle_9.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(253, 42, 71);\n"
"border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(170, 125, 131)\n"
"\n"
"}")
        self.frame_circle_9.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_circle_9)
        self.verticalLayout_30.setSpacing(10)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(10, 35, 10, 35)
        self.label_19 = QLabel(self.frame_circle_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font6)
        self.label_19.setStyleSheet(u"border: none;\n"
"color: rgb(253, 42, 71);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_19)

        self.label_ask_XLM = QLabel(self.frame_circle_9)
        self.label_ask_XLM.setObjectName(u"label_ask_XLM")
        self.label_ask_XLM.setFont(font15)
        self.label_ask_XLM.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_ask_XLM.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_ask_XLM)

        self.label_20 = QLabel(self.frame_circle_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font8)
        self.label_20.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_20)


        self.horizontalLayout_15.addWidget(self.frame_circle_9)


        self.verticalLayout_27.addWidget(self.frame_infos_3, 0, Qt.AlignVCenter)

        self.frame_text_3 = QFrame(self.frame_content_home_3)
        self.frame_text_3.setObjectName(u"frame_text_3")
        self.frame_text_3.setMinimumSize(QSize(600, 0))
        self.frame_text_3.setMaximumSize(QSize(16777215, 100))
        self.frame_text_3.setFrameShape(QFrame.StyledPanel)
        self.frame_text_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_text_3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_21 = QLabel(self.frame_text_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 40))
        self.label_21.setMaximumSize(QSize(600, 50))
        self.label_21.setFont(font14)
        self.label_21.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(35, 33, 75);\n"
"border-radius: 10px;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_21)


        self.verticalLayout_27.addWidget(self.frame_text_3, 0, Qt.AlignHCenter)


        self.verticalLayout_37.addWidget(self.frame_content_home_3)

        self.stackedWidget.addWidget(self.page_XLM)
        self.page_XRP = QWidget()
        self.page_XRP.setObjectName(u"page_XRP")
        self.verticalLayout_38 = QVBoxLayout(self.page_XRP)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.page_XRP)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 100))
        self.label_30.setFont(font11)
        self.label_30.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_30)

        self.frame_content_home_4 = QFrame(self.page_XRP)
        self.frame_content_home_4.setObjectName(u"frame_content_home_4")
        self.frame_content_home_4.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_content_home_4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_infos_4 = QFrame(self.frame_content_home_4)
        self.frame_infos_4.setObjectName(u"frame_infos_4")
        self.frame_infos_4.setFrameShape(QFrame.StyledPanel)
        self.frame_infos_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_infos_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_circle_10 = QFrame(self.frame_infos_4)
        self.frame_circle_10.setObjectName(u"frame_circle_10")
        self.frame_circle_10.setMinimumSize(QSize(200, 200))
        self.frame_circle_10.setMaximumSize(QSize(200, 200))
        self.frame_circle_10.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(63, 207, 180);\n"
"border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(118, 152, 146)\n"
"\n"
"}")
        self.frame_circle_10.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_circle_10)
        self.verticalLayout_33.setSpacing(10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(10, 35, 10, 35)
        self.label_22 = QLabel(self.frame_circle_10)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_22)

        self.label_bid_XRP = QLabel(self.frame_circle_10)
        self.label_bid_XRP.setObjectName(u"label_bid_XRP")
        font17 = QFont()
        font17.setFamily(u"Bahnschrift Light")
        font17.setPointSize(35)
        self.label_bid_XRP.setFont(font17)
        self.label_bid_XRP.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_bid_XRP.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_bid_XRP)

        self.label_23 = QLabel(self.frame_circle_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font8)
        self.label_23.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_23)


        self.horizontalLayout_16.addWidget(self.frame_circle_10)

        self.frame_circle_11 = QFrame(self.frame_infos_4)
        self.frame_circle_11.setObjectName(u"frame_circle_11")
        self.frame_circle_11.setMinimumSize(QSize(250, 250))
        self.frame_circle_11.setMaximumSize(QSize(250, 250))
        self.frame_circle_11.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(255, 238, 0);\n"
"border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(105, 95, 148)\n"
"\n"
"}")
        self.frame_circle_11.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_circle_11)
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(10, 35, 10, 35)
        self.label_24 = QLabel(self.frame_circle_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"border: none;\n"
"color: rgb(255, 238, 0);")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_24)

        self.label_last_XRP = QLabel(self.frame_circle_11)
        self.label_last_XRP.setObjectName(u"label_last_XRP")
        font18 = QFont()
        font18.setFamily(u"Bahnschrift Light")
        font18.setPointSize(50)
        self.label_last_XRP.setFont(font18)
        self.label_last_XRP.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_last_XRP.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_last_XRP)

        self.label_25 = QLabel(self.frame_circle_11)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font8)
        self.label_25.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_25)


        self.horizontalLayout_16.addWidget(self.frame_circle_11)

        self.frame_circle_12 = QFrame(self.frame_infos_4)
        self.frame_circle_12.setObjectName(u"frame_circle_12")
        self.frame_circle_12.setMinimumSize(QSize(200, 200))
        self.frame_circle_12.setMaximumSize(QSize(200, 200))
        self.frame_circle_12.setStyleSheet(u"QFrame{\n"
"border: 5px solid rgb(253, 42, 71);\n"
"border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"border: 5px solid rgb(170, 125, 131)\n"
"\n"
"}")
        self.frame_circle_12.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_circle_12)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(10, 35, 10, 35)
        self.label_26 = QLabel(self.frame_circle_12)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font6)
        self.label_26.setStyleSheet(u"border: none;\n"
"color: rgb(253, 42, 71);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_26)

        self.label_ask_XRP = QLabel(self.frame_circle_12)
        self.label_ask_XRP.setObjectName(u"label_ask_XRP")
        self.label_ask_XRP.setFont(font17)
        self.label_ask_XRP.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_ask_XRP.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_ask_XRP)

        self.label_27 = QLabel(self.frame_circle_12)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font8)
        self.label_27.setStyleSheet(u"border: none;\n"
"color: rgb(220,220,220);")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_27)


        self.horizontalLayout_16.addWidget(self.frame_circle_12)


        self.verticalLayout_32.addWidget(self.frame_infos_4, 0, Qt.AlignVCenter)

        self.frame_text_4 = QFrame(self.frame_content_home_4)
        self.frame_text_4.setObjectName(u"frame_text_4")
        self.frame_text_4.setMinimumSize(QSize(600, 0))
        self.frame_text_4.setMaximumSize(QSize(16777215, 100))
        self.frame_text_4.setFrameShape(QFrame.StyledPanel)
        self.frame_text_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_text_4)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_28 = QLabel(self.frame_text_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 40))
        self.label_28.setMaximumSize(QSize(600, 50))
        self.label_28.setFont(font14)
        self.label_28.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(35, 33, 75);\n"
"border-radius: 10px;")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_28)


        self.verticalLayout_32.addWidget(self.frame_text_4, 0, Qt.AlignHCenter)


        self.verticalLayout_38.addWidget(self.frame_content_home_4)

        self.stackedWidget.addWidget(self.page_XRP)
        self.page_custom = QWidget()
        self.page_custom.setObjectName(u"page_custom")
        self.verticalLayout_39 = QVBoxLayout(self.page_custom)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_14 = QFrame(self.page_custom)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_14)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_35 = QLabel(self.frame_14)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font5)
        self.label_35.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_35)

        self.label_29 = QLabel(self.frame_14)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font5)
        self.label_29.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_29)


        self.verticalLayout_39.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.page_custom)

        self.horizontalLayout_5.addWidget(self.stackedWidget)

        self.frame_alerts = QFrame(self.frame_2)
        self.frame_alerts.setObjectName(u"frame_alerts")
        self.frame_alerts.setMinimumSize(QSize(250, 0))
        self.frame_alerts.setMaximumSize(QSize(250, 16777215))
        self.frame_alerts.setFrameShape(QFrame.StyledPanel)
        self.frame_alerts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_alerts)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_alerts)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 0, 5, 0)
        self.spinbox_alert_price = QDoubleSpinBox(self.frame_12)
        self.spinbox_alert_price.setObjectName(u"spinbox_alert_price")
        self.spinbox_alert_price.setMinimumSize(QSize(0, 30))
        self.spinbox_alert_price.setMaximumSize(QSize(16777215, 30))
        self.spinbox_alert_price.setFont(font4)
        self.spinbox_alert_price.setStyleSheet(u"QDoubleSpinBox\n"
"{\n"
"border : 1px solid #757aff;\n"
"background : white;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"\n"
"}\n"
"QDoubleSpinBox::hover\n"
"{\n"
"border : 1px solid #75d1ff;\n"
"background : white;\n"
"}")
        self.spinbox_alert_price.setDecimals(2)
        self.spinbox_alert_price.setMaximum(1000000.000000000000000)
        self.spinbox_alert_price.setSingleStep(0.010000000000000)

        self.horizontalLayout_13.addWidget(self.spinbox_alert_price)

        self.btn_add_alert = QPushButton(self.frame_12)
        self.btn_add_alert.setObjectName(u"btn_add_alert")
        self.btn_add_alert.setEnabled(False)
        self.btn_add_alert.setMinimumSize(QSize(120, 30))
        self.btn_add_alert.setMaximumSize(QSize(200, 30))
        self.btn_add_alert.setFont(font2)
        self.btn_add_alert.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(63, 207, 180);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #FFF\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(133, 224, 208);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(40, 159, 137);\n"
"	border: 1px solid #252660;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#64747d;\n"
"}")
        self.btn_add_alert.setFlat(False)

        self.horizontalLayout_13.addWidget(self.btn_add_alert)

        self.horizontalSpacer_6 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_20.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_alerts)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_13)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 0)
        self.btn_del_alert = QPushButton(self.frame_13)
        self.btn_del_alert.setObjectName(u"btn_del_alert")
        self.btn_del_alert.setMinimumSize(QSize(200, 30))
        self.btn_del_alert.setFont(font2)
        self.btn_del_alert.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(253, 42, 71);\n"
"	border: none;\n"
"	border-radius: 7px;\n"
"	color: #FFF\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(253, 73, 97);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(213, 83, 100);\n"
"	border: 1px solid #252660;\n"
"}")
        self.btn_del_alert.setFlat(False)

        self.verticalLayout_21.addWidget(self.btn_del_alert)

        self.table_alerts = QTableWidget(self.frame_13)
        self.table_alerts.setObjectName(u"table_alerts")
        self.table_alerts.setStyleSheet(u"QTableWidget QHeaderView::section{\n"
"background-color: #6ca5da;\n"
"}\n"
"")
        self.table_alerts.setShowGrid(True)
        self.table_alerts.setColumnCount(0)

        self.verticalLayout_21.addWidget(self.table_alerts)

        self.label_36 = QLabel(self.frame_13)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_21.addWidget(self.label_36)

        self.table_alerts_send = QTableWidget(self.frame_13)
        self.table_alerts_send.setObjectName(u"table_alerts_send")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.table_alerts_send.sizePolicy().hasHeightForWidth())
        self.table_alerts_send.setSizePolicy(sizePolicy)
        self.table_alerts_send.setMinimumSize(QSize(0, 100))
        self.table_alerts_send.setMaximumSize(QSize(16777215, 200))
        font19 = QFont()
        font19.setPointSize(7)
        self.table_alerts_send.setFont(font19)
        self.table_alerts_send.setStyleSheet(u"QTableWidget QHeaderView::section{\n"
"background-color: #6ca5da;\n"
"}\n"
"")
        self.table_alerts_send.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table_alerts_send.setShowGrid(True)
        self.table_alerts_send.setColumnCount(0)

        self.verticalLayout_21.addWidget(self.table_alerts_send)


        self.verticalLayout_20.addWidget(self.frame_13)


        self.horizontalLayout_5.addWidget(self.frame_alerts)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: none;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font20 = QFont()
        font20.setFamily(u"Gill Sans Nova")
        font20.setPointSize(8)
        self.label_credits.setFont(font20)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_3.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.horizontalLayout_8.addWidget(self.drop_shadow_frame)


        self.drop_shadow_layout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_add_alert_low.setDefault(True)
        self.btn_add_alert_high.setDefault(True)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_add_alert.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"Crypto", None))
        self.btn_ETH.setText(QCoreApplication.translate("MainWindow", u"ETH", None))
        self.btn_BTC.setText(QCoreApplication.translate("MainWindow", u"BTC", None))
        self.btn_XLM.setText(QCoreApplication.translate("MainWindow", u"XLM", None))
        self.btn_XRP.setText(QCoreApplication.translate("MainWindow", u"XRP", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Alert", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_status_time.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.btn_add_alert_low.setToolTip(QCoreApplication.translate("MainWindow", u"Dodaj alert", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_alert_low.setText(QCoreApplication.translate("MainWindow", u"%Low", None))
#if QT_CONFIG(tooltip)
        self.btn_add_alert_high.setToolTip(QCoreApplication.translate("MainWindow", u"Dodaj alert", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_alert_high.setText(QCoreApplication.translate("MainWindow", u"%High", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"ETH", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BID", None))
        self.label_bid_ETH.setText(QCoreApplication.translate("MainWindow", u"xxxx.xx", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LAST", None))
        self.label_last_ETH.setText(QCoreApplication.translate("MainWindow", u"xxxx.xx", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ASK", None))
        self.label_ask_ETH.setText(QCoreApplication.translate("MainWindow", u"xxxx.xx", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("MainWindow", u"\"Kiedy pada z\u0142oto, si\u0119bgnij po wiadro, a nie po naparstek...\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\"When it's raining gold, reach for a bucket, not a thimble...\"", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"BTC", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"BID", None))
        self.label_bid_BTC.setText(QCoreApplication.translate("MainWindow", u"xxxxxx.xx", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"LAST", None))
        self.label_last_BTC.setText(QCoreApplication.translate("MainWindow", u"xxxxxx.xx", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ASK", None))
        self.label_ask_BTC.setText(QCoreApplication.translate("MainWindow", u"xxxxxx.xx", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("MainWindow", u"\"Kiedy pada z\u0142oto, wyjmij wiadro, a nie naparstek...\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\"When it's raining gold, reach for a bucket, not a thimble...\"", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"XLM", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"BID", None))
        self.label_bid_XLM.setText(QCoreApplication.translate("MainWindow", u"x.xx", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"LAST", None))
        self.label_last_XLM.setText(QCoreApplication.translate("MainWindow", u"x.xx", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"ASK", None))
        self.label_ask_XLM.setText(QCoreApplication.translate("MainWindow", u"x.xx", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
#if QT_CONFIG(tooltip)
        self.label_21.setToolTip(QCoreApplication.translate("MainWindow", u"\"Kiedy pada z\u0142oto, wyjmij wiadro, a nie naparstek...\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\"When it's raining gold, reach for a bucket, not a thimble...\"", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"XRP", None))
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip(QCoreApplication.translate("MainWindow", u"Kupno", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"BID", None))
        self.label_bid_XRP.setText(QCoreApplication.translate("MainWindow", u"x.xx", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("MainWindow", u"Ostatnia", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"LAST", None))
        self.label_last_XRP.setText(QCoreApplication.translate("MainWindow", u"x.xx", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
#if QT_CONFIG(tooltip)
        self.label_26.setToolTip(QCoreApplication.translate("MainWindow", u"Sprzeda\u017c", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"ASK", None))
        self.label_ask_XRP.setText(QCoreApplication.translate("MainWindow", u"x.xx", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"PLN", None))
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("MainWindow", u"\"Kiedy pada z\u0142oto, wyjmij wiadro, a nie naparstek...\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\"When it's raining gold, reach for a bucket, not a thimble...\"", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Wpisz nazw\u0119 waluty:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Do zrobienia w przysz\u0142o\u015bci...", None))
#if QT_CONFIG(tooltip)
        self.btn_add_alert.setToolTip(QCoreApplication.translate("MainWindow", u"Dodaj alert", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_alert.setText(QCoreApplication.translate("MainWindow", u"Add alert", None))
#if QT_CONFIG(tooltip)
        self.btn_del_alert.setToolTip(QCoreApplication.translate("MainWindow", u"Usu\u0144 wybrany alert", None))
#endif // QT_CONFIG(tooltip)
        self.btn_del_alert.setText(QCoreApplication.translate("MainWindow", u"Delete selected alert", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Notifications send:", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"By: Krzysztof Dziarmaga", None))
    # retranslateUi

