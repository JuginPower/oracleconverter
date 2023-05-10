# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_ConverterWindow(object):
    def setupUi(self, ConverterWindow):
        if not ConverterWindow.objectName():
            ConverterWindow.setObjectName(u"ConverterWindow")
        ConverterWindow.resize(489, 349)
        self.actionOpen_SQL = QAction(ConverterWindow)
        self.actionOpen_SQL.setObjectName(u"actionOpen_SQL")
        self.actionExit = QAction(ConverterWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(ConverterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonTranslate = QPushButton(self.centralwidget)
        self.pushButtonTranslate.setObjectName(u"pushButtonTranslate")

        self.gridLayout.addWidget(self.pushButtonTranslate, 3, 1, 1, 1)

        self.pushButtonDownload = QPushButton(self.centralwidget)
        self.pushButtonDownload.setObjectName(u"pushButtonDownload")

        self.gridLayout.addWidget(self.pushButtonDownload, 3, 2, 1, 1)

        self.pushButtonOpen = QPushButton(self.centralwidget)
        self.pushButtonOpen.setObjectName(u"pushButtonOpen")

        self.gridLayout.addWidget(self.pushButtonOpen, 3, 0, 1, 1)

        self.lineEditDownload = QLineEdit(self.centralwidget)
        self.lineEditDownload.setObjectName(u"lineEditDownload")

        self.gridLayout.addWidget(self.lineEditDownload, 2, 2, 1, 1)

        self.lineEditUpload = QLineEdit(self.centralwidget)
        self.lineEditUpload.setObjectName(u"lineEditUpload")

        self.gridLayout.addWidget(self.lineEditUpload, 2, 0, 1, 1)

        ConverterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ConverterWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        ConverterWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ConverterWindow)
        self.statusbar.setObjectName(u"statusbar")
        ConverterWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen_SQL)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(ConverterWindow)

        QMetaObject.connectSlotsByName(ConverterWindow)
    # setupUi

    def retranslateUi(self, ConverterWindow):
        ConverterWindow.setWindowTitle(QCoreApplication.translate("ConverterWindow", u"OracleConverter", None))
        self.actionOpen_SQL.setText(QCoreApplication.translate("ConverterWindow", u"Open SQL", None))
        self.actionExit.setText(QCoreApplication.translate("ConverterWindow", u"Exit", None))
        self.pushButtonTranslate.setText(QCoreApplication.translate("ConverterWindow", u"Translate", None))
        self.pushButtonDownload.setText(QCoreApplication.translate("ConverterWindow", u"Download SQL", None))
        self.pushButtonOpen.setText(QCoreApplication.translate("ConverterWindow", u"Open SQL", None))
        self.menuFile.setTitle(QCoreApplication.translate("ConverterWindow", u"File", None))
    # retranslateUi

