# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:15:21 2021

@author: Krzysztof Dziarmaga
"""
import sys, datetime, smtplib
from PySide2 import QtCore, QtGui, QtWidgets, QtXml
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QTimer
import requests
from ui_main import Ui_MainWindow
from cryptography.fernet import Fernet
from ui_functions import *

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class MainWindow(QMainWindow):
    def __init__(self):
        # QMainWindow.__init__(self)
        # designer_file = QFile('ui_main.ui')
        # designer_file.open(QFile.ReadOnly)
        # loader = QUiLoader()
        # self.ui = loader.load(designer_file,self)
        # designer_file.close()

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.interface()
        self.read_settings_file()
        UIFunctions.uiDefinitions(self)
        self.show()
        self.init_table()
        self.alerts = []
        

        ## MOVE
        def moveWindow(event):
            """
            Function handling window dragging
            :param event: Event triggered
            :return:
            """
            #RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)
            #If leftclick Move Window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.title_bar.mouseMoveEvent = moveWindow

        

    def mousePressEvent(self, event):
        """
        Function handling moise click events
        :param event:
        :return:
        """
        self.dragPos = event.globalPos()
        
    def interface(self):
        """
        Connecting user's interactions with GUI with corresponding functions
        :return:
        """
        self.ui.btn_start.clicked.connect(lambda: self.startScraping())
        self.ui.btn_ETH.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ETH))
        self.ui.btn_BTC.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_BTC))
        self.ui.btn_XLM.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_XLM))
        self.ui.btn_XRP.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_XRP))
        self.ui.btn_custom.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_custom))
        self.ui.btn_add_alert.clicked.connect(lambda: self.add_alert())
        self.ui.btn_del_alert.clicked.connect(lambda: self.remove_row_click())
        self.ui.btn_add_alert_low.clicked.connect(lambda: self.btn_add_alert_low_high(state='low'))
        self.ui.btn_add_alert_high.clicked.connect(lambda: self.btn_add_alert_low_high(state='high'))
        
    def startScraping(self):
        """
        Function responsible for starting of scraping BitBay prices through rest API
        :return:
        """
        self.ui.btn_start.setEnabled(False)
        self.ui.btn_add_alert.setEnabled(True)
        self.ui.btn_add_alert_low.setEnabled(True)
        self.ui.btn_add_alert_high.setEnabled(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_prices)
        self.get_prices()
        self.timer.start(float(self.time_interval)*1000)
            


    def get_prices(self):
        """
        Exact function scraping BitBay prices through rest API
        :return:
        """
        URL = 'https://api.bitbay.net/rest/trading/ticker'
        Waluty = ['ETH', 'BTC', 'XLM', 'XRP']
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
        page = requests.get(URL).json()

        self.ask_ETH = float(page['items']['ETH-PLN']['lowestAsk'])
        self.bid_ETH = float(page['items']['ETH-PLN']['highestBid'])
        self.last_ETH = float(page['items']['ETH-PLN']['rate'])
        self.ask_BTC = float(page['items']['BTC-PLN']['lowestAsk'])
        self.bid_BTC = float(page['items']['BTC-PLN']['highestBid'])
        self.last_BTC = float(page['items']['BTC-PLN']['rate'])
        self.ask_XLM = float(page['items']['XLM-PLN']['lowestAsk'])
        self.bid_XLM = float(page['items']['XLM-PLN']['highestBid'])
        self.last_XLM = float(page['items']['XLM-PLN']['rate'])
        self.ask_XRP = float(page['items']['XRP-PLN']['lowestAsk'])
        self.bid_XRP = float(page['items']['XRP-PLN']['highestBid'])
        self.last_XRP = float(page['items']['XRP-PLN']['rate'])

        self.ui.label_bid_ETH.setText(str(self.bid_ETH))
        self.ui.label_ask_ETH.setText(str(self.ask_ETH))
        self.ui.label_last_ETH.setText(str(self.last_ETH))
        self.ui.label_bid_BTC.setText(str(self.bid_BTC))
        self.ui.label_ask_BTC.setText(str(self.ask_BTC))
        self.ui.label_last_BTC.setText(str(self.last_BTC))
        self.ui.label_bid_XLM.setText(str(self.bid_XLM))
        self.ui.label_ask_XLM.setText(str(self.ask_XLM))
        self.ui.label_last_XLM.setText(str(self.last_XLM))
        self.ui.label_bid_XRP.setText(str(self.bid_XRP))
        self.ui.label_ask_XRP.setText(str(self.ask_XRP))
        self.ui.label_last_XRP.setText(str(self.last_XRP))
        self.ui.label_status.setText('Working...')
        self.ui.label_status_time.setText('Last reading: ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        self.check_alerts()

    def init_table(self):
        """
        Initiate alerts table in GUI
        :return:
        """
        columns =  ["Name", "Price"]
        self.ui.table_alerts.setColumnCount(len(columns))
        self.ui.table_alerts.setHorizontalHeaderLabels(columns)
        self.ui.table_alerts.setColumnWidth(0,100)
        self.ui.table_alerts.setColumnWidth(1,100)
        delegate = AlignDelegate(self.ui.table_alerts)
        self.ui.table_alerts.setItemDelegateForColumn(0, delegate)
        self.ui.table_alerts.setItemDelegateForColumn(1, delegate)

        columns_2 =  ["Name", "Price",'Time']
        self.ui.table_alerts_send.setColumnCount(len(columns_2))
        self.ui.table_alerts_send.setHorizontalHeaderLabels(columns_2)
        self.ui.table_alerts_send.setColumnWidth(0,50)
        self.ui.table_alerts_send.setColumnWidth(1,50)
        self.ui.table_alerts_send.setColumnWidth(2,100)
        delegate = AlignDelegate(self.ui.table_alerts_send)
        self.ui.table_alerts_send.setItemDelegateForColumn(0, delegate)
        self.ui.table_alerts_send.setItemDelegateForColumn(1, delegate)
        

    def add_alert(self, cena=False):
        """
        Adding notification alert to the table
        :param cena: Price that we want to be alerted about
        :return:
        """
        row_position = self.ui.table_alerts.rowCount()
        nazwa = self.ui.stackedWidget.currentWidget().objectName()[-3:]
        if cena == False:
            cena=round(self.ui.spinbox_alert_price.value(),2)
        
        
        if nazwa == 'ETH':
            if cena < float(self.last_ETH):
                znak = 'less'
                self.ui.table_alerts.insertRow(row_position)
                self.ui.table_alerts.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nazwa))
                self.ui.table_alerts.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(cena)))
                self.alerts.append([nazwa, cena, znak])
            elif cena > float(self.last_ETH):
                znak = 'greater'
                self.ui.table_alerts.insertRow(row_position)
                self.ui.table_alerts.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nazwa))
                self.ui.table_alerts.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(cena)))
                self.alerts.append([nazwa, cena, znak])
        elif nazwa == 'BTC':
            if cena < float(self.last_BTC):
                znak = 'less'
                self.ui.table_alerts.insertRow(row_position)
                self.ui.table_alerts.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nazwa))
                self.ui.table_alerts.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(cena)))
                self.alerts.append([nazwa, cena, znak])
            elif cena > float(self.last_BTC):
                znak = 'greater'
                self.ui.table_alerts.insertRow(row_position)
                self.ui.table_alerts.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nazwa))
                self.ui.table_alerts.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(cena)))
                self.alerts.append([nazwa, cena, znak])
        elif nazwa == 'XLM':
            if cena < float(self.last_XLM):
                znak = 'less'
                self.ui.table_alerts.insertRow(row_position)
                self.ui.table_alerts.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nazwa))
                self.ui.table_alerts.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(cena)))
                self.alerts.append([nazwa, cena, znak])
            elif cena > float(self.last_XLM):
                znak = 'greater'
                self.ui.table_alerts.insertRow(row_position)
                self.ui.table_alerts.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nazwa))
                self.ui.table_alerts.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(cena)))
                self.alerts.append([nazwa, cena, znak])
        elif nazwa == 'XRP':
            if cena < float(self.last_XRP):
                znak = 'less'
                self.ui.table_alerts.insertRow(row_position)
                self.ui.table_alerts.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nazwa))
                self.ui.table_alerts.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(cena)))
                self.alerts.append([nazwa, cena, znak])
            elif cena > float(self.last_XRP):
                znak = 'greater'
                self.ui.table_alerts.insertRow(row_position)
                self.ui.table_alerts.setItem(row_position, 0, QtWidgets.QTableWidgetItem(nazwa))
                self.ui.table_alerts.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(cena)))
                self.alerts.append([nazwa, cena, znak])
        
        # print(self.alerts)


    def remove_row_click(self):
        """
        Removing selected alert from alerts table
        :return:
        """
        try:
            self.ui.table_alerts.removeRow(self.ui.table_alerts.currentRow())
            self.alerts.pop(self.ui.table_alerts.currentRow())
        except IndexError:
            msg = QtWidgets.QMessageBox().information(self, "Error", "Najpierw dodaj aletr!")
        # print(self.alerts)

    def check_alerts(self):
        """
        Checking if price alert shall be triggered for every price notification added to alerts table
        :return:
        """
        rows_to_delete = []
        for i in range(len(self.alerts)):
            if self.alerts[i][0] == 'ETH':
                if self.alerts[i][2] == 'less':
                    if self.last_ETH <= self.alerts[i][1]:
                        self.send_email_alert('ETH', self.alerts[i][1])
                        self.add_notif_to_table('ETH', self.alerts[i][1], str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        rows_to_delete.append(i)
                else:
                    if self.last_ETH >= self.alerts[i][1]:
                        self.send_email_alert('ETH', self.alerts[i][1])
                        self.add_notif_to_table('ETH', self.alerts[i][1], str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        rows_to_delete.append(i)
            elif self.alerts[i][0] == 'BTC':
                if self.alerts[i][2] == 'less':
                    if self.last_BTC <= self.alerts[i][1]:
                        self.send_email_alert('BTC', self.alerts[i][1])
                        self.add_notif_to_table('BTC', self.alerts[i][1], str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        rows_to_delete.append(i)
                else:
                    if self.last_BTC >= self.alerts[i][1]:
                        self.send_email_alert('BTC', self.alerts[i][1])
                        self.add_notif_to_table('BTC', self.alerts[i][1], str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        rows_to_delete.append(i)
            elif self.alerts[i][0] == 'XLM':
                if self.alerts[i][2] == 'less':
                    if self.last_XLM <= self.alerts[i][1]:
                        self.send_email_alert('XLM', self.alerts[i][1])
                        self.add_notif_to_table('XLM', self.alerts[i][1], str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        rows_to_delete.append(i)
                else:
                    if self.last_XLM >= self.alerts[i][1]:
                        self.send_email_alert('XLM', self.alerts[i][1])
                        self.add_notif_to_table('XLM', self.alerts[i][1], str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        rows_to_delete.append(i)
            elif self.alerts[i][0] == 'XRP':
                if self.alerts[i][2] == 'less':
                    if self.last_XRP <= self.alerts[i][1]:
                        self.send_email_alert('XRP', self.alerts[i][1])
                        self.add_notif_to_table('XRP', self.alerts[i][1], str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        rows_to_delete.append(i)
                else:
                    if self.last_XRP >= self.alerts[i][1]:
                        self.send_email_alert('XRP', self.alerts[i][1])
                        self.add_notif_to_table('XRP', self.alerts[i][1], str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                        rows_to_delete.append(i)
        for i in rows_to_delete:
            self.alerts.pop(i)
            self.ui.table_alerts.removeRow(i)
    
    def add_notif_to_table(self, name, price, time):
        row_position_2 = 0
        self.ui.table_alerts_send.insertRow(row_position_2)
        self.ui.table_alerts_send.setItem(row_position_2, 0, QtWidgets.QTableWidgetItem(name))
        self.ui.table_alerts_send.setItem(row_position_2, 1, QtWidgets.QTableWidgetItem(str(price)))
        self.ui.table_alerts_send.setItem(row_position_2, 2, QtWidgets.QTableWidgetItem(time))

    def send_email_alert(self,waluta,kurs):
        """
        Function sending email notification
        :param waluta: Name of CryptoCurrency
        :param kurs: Price of crypto
        :return:
        """
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(self.sender, self.password)
        subject = 'Alert ' + waluta + ' = ' + str(kurs)
        msg = 'Waluta ' + waluta + ' osiagnela kurs ' + str(kurs)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(str(self.sender), str(self.recevier), message)
        server.quit()
        print('Mail sent')


    def btn_add_alert_low_high(self, state='low'):
        """
        Additional function which allows to add special (percentage high or low) notification
        :param state: Percentage 'high' or 'low'
        :return:
        """
        if state == 'low':
            percent = 1 - self.ui.spinbox_percent_price.value()*0.01
        elif state == 'high':
            percent = 1 + self.ui.spinbox_percent_price.value()*0.01
        name = self.ui.stackedWidget.currentWidget().objectName()[-3:]
        if name == 'ETH':
            cena = round(self.last_ETH * percent,2)
        elif name == 'BTC':
            cena = round(self.last_BTC * percent,2)
        elif name == 'XLM':
            cena = round(self.last_XLM * percent,2)
        elif name == 'XRP':
            cena = round(self.last_XRP * percent,2)
        
        self.add_alert(cena=cena)
        print(name)



    def read_settings_file(self):
        """
        Reading 'Settings.txt' file which contains email basic info, updating time interval etc.
        :return:
        """
        settings_file = open('Settings.txt','r')
        lines=[]
        for line in settings_file:
            if not line.strip().startswith('#') and line.strip('\n').strip() != '':
                lines.append(line.strip('\n').strip())
        settings_file.close()
        self.sender = lines[0]
        self.password = self.decrypt(lines[1])
        self.recevier = lines[2]
        self.time_interval = lines[3]

    def decrypt(self, token) -> bytes:
        """
        Decrypting the email password
        :param token:
        :return: Decrypted password
        """
        key = 'Hc2rxZW5uRJrvOLi5SjzEUxyxH3miRfH-6HieUjI_24='
        token = token.encode('utf-8')
        pwd = Fernet(key).decrypt(token).decode('utf-8')
        return pwd

if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = MainWindow()
    sys.exit(app.exec_())