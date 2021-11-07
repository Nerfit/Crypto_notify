## GUI File
from Crypto_notifications import *

# GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):
    def maximize_restore(self):
        """
        Maximize/restore functionality
        :return:
        """
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # If not maximized
        if status == 0:
            self.showMaximized()

            #set global to 1
            GLOBAL_STATE = 1

            # if maximized remove margins and border radius
            self.ui.drop_shadow_layout.setContentsMargins(0,0,0,0)
            self.ui.drop_shadow_frame.setStyleSheet("""background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.575269 rgba(28, 29, 73, 255));
                                                        border-top-right-radius: 0px;
                                                        border-bottom-right-radius: 0px;
                                                        """)
            self.ui.btn_maximize.setToolTip('Restore')
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10,10,10,10)
            self.ui.drop_shadow_frame.setStyleSheet("""background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.575269 rgba(28, 29, 73, 255));
                                                        border-top-right-radius: 10px;
                                                        border-bottom-right-radius: 10px;
                                                        """)
            self.ui.btn_maximize.setToolTip('Maximize')

    ## UI DEFINITIONS
    def uiDefinitions(self):
        """
        Functions ensuring frameless window
        :return:
        """
        # REMOVE TITLEBAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        # Minimize
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        # Close
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet('QSizeGrip {width: 10px; height: 10px; margin: 5px} QSizeGrip:hover {background-color: rgb(50,42,94)}')
        self.sizegrip.setToolTip('Resize window')

## RETURN STATUS IF WINDOWS IS MAXIMIZED OR RESTORED
    def returnStatus():
        return GLOBAL_STATE





