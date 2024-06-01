from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import datetime

import AI

stylesheet_main = """
    QWidget {
    background-color: #FFFFFF; /* Цвет фона контейнера-виджета */
    border: 2px solid #3498DB;
    border-radius: 5px
    }
    QPushButton {
        background-color: #E74C3C; /* Цвет фона кнопки */
        color: #FFFFFF;
        padding: 0px 0px;
        border: 1px solid black;
        border-radius: 3px;
        font-size: 20px
    }
    QPushButton:hover {
        background-color: #FFFFFF; /* Цвет фона кнопки */
        color: #E74C3C;
    }
    QPushButton#pushButton_ControlMajor {
        font-size: 10px
    }
    
    

    QLabel {
        color: #2C3E50;
        font-size: 16px;
        border: 0px solid #3498DB;
        border-radius: 0px;
    }
    
    QDateEdit {
        background-color: #3498DB; /* Цвет фона QDateEdit */
        color: #FFFFFF; /* Цвет текста в QDateEdit */
        border: 1px solid #2980B9; /* Граница QDateEdit */
        border-radius: 3px;
    }
"""

stylesheet_start = """
    /* Стиль для окна */
    QWidget {
        background-color: #2C3E50; /* Цвет фона окна */
        background-color: rgb(1,20,114); /* Цвет фона окна */
    }

    /* Стиль для кнопки */
    QPushButton {
        background-color: #E74C3C; /* Цвет фона кнопки */
        color: #FFFFFF;
        padding: 10px;
        border: 1px solid black;
        border-radius: 3px;
    }
    QPushButton:hover {
        background-color: #FFFFFF; /* Цвет фона кнопки */
        color: #E74C3C;
    }
    QPushButton{
        border: none; 
        padding: 0px; 
    }
    
    /* Стиль для текста */
    QLabel {
        color: #FFFFFF; /* Цвет текста */
        font-size: 24px;
       
    }
"""

class Ui_StartWindow(object):
    def setupUi_start(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 372)
        MainWindow.setStyleSheet(stylesheet_start)
        MainWindow.setMinimumSize(QtCore.QSize(390, 372))
        MainWindow.setMaximumSize(QtCore.QSize(390, 372))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pixmap_logo = QtWidgets.QLabel(self.centralwidget)
        self.pixmap_logo.setGeometry(QtCore.QRect(130, 30, 0, 0))
        pixmap = QtGui.QPixmap("date/icon_128.png")  # Укажите путь к вашему изображению
        self.pixmap_logo.setPixmap(pixmap)
        self.pixmap_logo.resize(pixmap.width(), pixmap.height())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 160, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 220, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pixmap_logo_AFKsystem = QtWidgets.QLabel(self.centralwidget)
        self.pixmap_logo_AFKsystem.setGeometry(QtCore.QRect(70, 300, 0, 0))
        pixmap = QtGui.QPixmap("date/logo_AFK.png")  # Укажите путь к вашему изображению
        self.pixmap_logo_AFKsystem.setPixmap(pixmap)
        self.pixmap_logo_AFKsystem.resize(pixmap.width(), pixmap.height())

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_start(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi_start(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AFK Система"))
        icon = QtGui.QIcon('date/icon_16.png')
        MainWindow.setWindowIcon(icon)
        self.label.setText(_translate("MainWindow", "Прогноз Акций"))
        self.pushButton.setText(_translate("MainWindow", "Начать"))
        self.pushButton.clicked.connect(lambda: self.setupUi_choice(MainWindow))

    def setupUi_choice(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 372)
        MainWindow.setStyleSheet(stylesheet_start)
        MainWindow.setMinimumSize(QtCore.QSize(390, 372))
        MainWindow.setMaximumSize(QtCore.QSize(390, 372))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 40, 128, 128))
        self.pushButton.setObjectName("pushButton_stock")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 40, 128, 128))
        self.pushButton_2.setObjectName("pushButton_stock")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 170, 128, 128))
        self.pushButton_3.setObjectName("pushButton_stock")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 170, 128, 128))
        self.pushButton_4.setObjectName("pushButton_stock")

        self.pixmap_logo_AFKsystem = QtWidgets.QLabel(self.centralwidget)
        self.pixmap_logo_AFKsystem.setGeometry(QtCore.QRect(70, 300, 0, 0))
        pixmap = QtGui.QPixmap("date/logo_AFK.png")  # Укажите путь к вашему изображению
        self.pixmap_logo_AFKsystem.setPixmap(pixmap)
        self.pixmap_logo_AFKsystem.resize(pixmap.width(), pixmap.height())

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_choice(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi_choice(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AFK Система - Выбор акций"))

        self.pushButton.clicked.connect(lambda: self.start_main_window("mts"))
        self.pushButton.setIcon(QtGui.QIcon("date/mts_logo_cmyk.png"))
        self.pushButton.setIconSize(QtCore.QSize(141, 121))

        self.pushButton_2.clicked.connect(lambda: self.start_main_window("sber"))
        self.pushButton_2.setIcon(QtGui.QIcon("date/sberbank.png"))
        self.pushButton_2.setIconSize(QtCore.QSize(141, 121))

        self.pushButton_3.clicked.connect(lambda: self.start_main_window("etlndr"))
        self.pushButton_3.setIcon(QtGui.QIcon("date/etanolgroup.png"))
        self.pushButton_3.setIconSize(QtCore.QSize(141, 121))

        self.pushButton_4.clicked.connect(lambda: self.start_main_window("yndx"))
        self.pushButton_4.setIcon(QtGui.QIcon("date/yandex.png"))
        self.pushButton_4.setIconSize(QtCore.QSize(141, 121))

    def start_main_window(self, model):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow, model)
        self.MainWindow.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, model):

        self.model = model

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 451)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("background-color: #ECF0F1")
        MainWindow.setMinimumSize(QtCore.QSize(680, 451))
        MainWindow.setMaximumSize(QtCore.QSize(680, 451))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget_figure = QtWidgets.QWidget(self.centralwidget)
        self.widget_figure.setGeometry(QtCore.QRect(-1, 10, 451, 421))
        self.widget_figure.setStyleSheet("""background-color: #FFFFFF; /* Цвет фона контейнера-виджета */
        border: 2px solid #3498DB;
        border-radius: 5px;
        padding: 10px;""")
        self.widget_figure.setObjectName("widget_figure")

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QtWidgets.QVBoxLayout(self.widget_figure)
        layout.addWidget(self.canvas)
        self.axes = self.figure.add_subplot(111)
        self.axes.xaxis.set_major_locator(mdates.MonthLocator())
        self.axes.xaxis.set_major_formatter(mdates.DateFormatter("%m"))
        self.axes.xaxis.set_minor_locator(mdates.DayLocator())
        title_axes = {"yndx": "Yandex", "mts": "MTS", "sber": "SberBank", "etlndr": "Etalon Group"}
        self.axes.set_title(f"Акции {title_axes[self.model]}")
        self.axes.yaxis.set_label_text("Цена (В Рублях)", size=6)
        self.axes.xaxis.set_label_text("Дата", size=6)
        self.line, = self.axes.plot([], [])
        self.line.set_label("Ценообразование")
        self.line.set_color("red")

        self.widget_control = QtWidgets.QWidget(self.centralwidget)
        self.widget_control.setGeometry(QtCore.QRect(450, 10, 221, 421))
        self.widget_control.setStyleSheet(stylesheet_main)
        self.widget_control.setObjectName("widget_control")


        self.widget_control_figure = QtWidgets.QWidget(self.widget_control)
        self.widget_control_figure.setGeometry(QtCore.QRect(0, 210, 221, 211))
        self.widget_control_figure.setObjectName("widget_control_figure")

        self.pushButton_update_figure = QtWidgets.QPushButton(self.widget_control_figure)
        self.pushButton_update_figure.setGeometry(QtCore.QRect(10, 160, 191, 41))
        self.pushButton_update_figure.setObjectName("pushButton_update_figure")

        self.label_end_price = QtWidgets.QLabel(self.widget_control_figure)
        self.label_end_price.setGeometry(QtCore.QRect(10, 100, 191, 16))
        self.label_end_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_end_price.setObjectName("label_end_price")

        self.dateEdit_start = QtWidgets.QDateEdit(self.widget_control_figure)
        self.dateEdit_start.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.dateEdit_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 4, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setMinimumDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_start.setObjectName("dateEdit_start")

        self.label_text_price = QtWidgets.QLabel(self.widget_control_figure)
        self.label_text_price.setGeometry(QtCore.QRect(10, 70, 191, 31))
        self.label_text_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_price.setObjectName("label_text_price")

        self.label_dt_end = QtWidgets.QLabel(self.widget_control_figure)
        self.label_dt_end.setGeometry(QtCore.QRect(110, 10, 91, 21))
        self.label_dt_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dt_end.setObjectName("label_dt_end")

        self.dateEdit_end = QtWidgets.QDateEdit(self.widget_control_figure)
        self.dateEdit_end.setGeometry(QtCore.QRect(110, 40, 91, 21))
        self.dateEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 5, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setMinimumDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_end.setObjectName("dateEdit_end")

        self.label_dt_start = QtWidgets.QLabel(self.widget_control_figure)
        self.label_dt_start.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_dt_start.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dt_start.setObjectName("label_dt_start")

        self.pushButton_ControlMajor_back_to_ten = QtWidgets.QPushButton(self.widget_control_figure)
        self.pushButton_ControlMajor_back_to_ten.setGeometry(QtCore.QRect(10, 130, 43, 27))
        self.pushButton_ControlMajor_back_to_ten.setObjectName("pushButton_ControlMajor")

        self.pushButton_ControlMajor_back_to_one = QtWidgets.QPushButton(self.widget_control_figure)
        self.pushButton_ControlMajor_back_to_one.setGeometry(QtCore.QRect(59, 130, 43, 27))
        self.pushButton_ControlMajor_back_to_one.setObjectName("pushButton_ControlMajor")

        self.pushButton_ControlMajor_forward_by_one = QtWidgets.QPushButton(self.widget_control_figure)
        self.pushButton_ControlMajor_forward_by_one.setGeometry(QtCore.QRect(110, 130, 43, 27))
        self.pushButton_ControlMajor_forward_by_one.setObjectName("pushButton_ControlMajor")

        self.pushButton_ControlMajor_forward_by_ten = QtWidgets.QPushButton(self.widget_control_figure)
        self.pushButton_ControlMajor_forward_by_ten.setGeometry(QtCore.QRect(159, 130, 43, 27))
        self.pushButton_ControlMajor_forward_by_ten.setObjectName("pushButton_ControlMajor")

        self.widget_OneDay = QtWidgets.QWidget(self.widget_control)
        self.widget_OneDay.setGeometry(QtCore.QRect(0, 0, 221, 211))
        self.widget_OneDay.setObjectName("widget_OneDay")

        self.dateEdit_priceoneday = QtWidgets.QDateEdit(self.widget_OneDay)
        self.dateEdit_priceoneday.setGeometry(QtCore.QRect(50, 30, 110, 22))
        self.dateEdit_priceoneday.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 6, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_priceoneday.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_priceoneday.setObjectName("dateEdit_priceoneday")

        self.label_oneday = QtWidgets.QLabel(self.widget_OneDay)
        self.label_oneday.setGeometry(QtCore.QRect(50, 10, 110, 18))
        self.label_oneday.setAlignment(QtCore.Qt.AlignCenter)
        self.label_oneday.setObjectName("label_oneday")

        self.label_text_price_OneDay = QtWidgets.QLabel(self.widget_OneDay)
        self.label_text_price_OneDay.setGeometry(QtCore.QRect(10, 60, 191, 31))
        self.label_text_price_OneDay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_price_OneDay.setObjectName("label_text_price_OneDay")

        self.label_price_OneDay = QtWidgets.QLabel(self.widget_OneDay)
        self.label_price_OneDay.setGeometry(QtCore.QRect(10, 90, 191, 16))
        self.label_price_OneDay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_price_OneDay.setObjectName("label_price_OneDay")

        self.pushButton_priceOneDay = QtWidgets.QPushButton(self.widget_OneDay)
        self.pushButton_priceOneDay.setGeometry(QtCore.QRect(10, 150, 191, 41))
        self.pushButton_priceOneDay.setObjectName("pushButton_priceOneDay")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        title_window = {"yndx": "Yandex", "mts": "MTS", "sber": "SberBank", "etlndr": "Etalon Group"}
        MainWindow.setWindowTitle(_translate("MainWindow", f"AFK Система - Прогноз Акций {title_window[self.model]}"))
        icon = QtGui.QIcon('date/icon_16.png')
        MainWindow.setWindowIcon(icon)

        self.pushButton_update_figure.setText(_translate("MainWindow", "Обновить График"))
        self.pushButton_update_figure.clicked.connect(self.button_update_figure)
        self.label_end_price.setText(_translate("MainWindow", "0 ₽"))
        self.label_text_price.setText(_translate("MainWindow", "Значение последнего дня"))
        self.label_dt_end.setText(_translate("MainWindow", "До"))
        self.label_dt_start.setText(_translate("MainWindow", "От"))

        self.xaxis_locater = 1

        self.pushButton_ControlMajor_back_to_ten.setText(_translate("MainWindow", "<<"))
        self.pushButton_ControlMajor_back_to_ten.clicked.connect(lambda: self.button_control_figure(1, 10))
        self.pushButton_ControlMajor_back_to_one.setText(_translate("MainWindow", "<"))
        self.pushButton_ControlMajor_back_to_one.clicked.connect(lambda: self.button_control_figure(1))

        self.pushButton_ControlMajor_forward_by_ten.setText(_translate("MainWindow", ">>"))
        self.pushButton_ControlMajor_forward_by_ten.clicked.connect(lambda: self.button_control_figure(2, 10))
        self.pushButton_ControlMajor_forward_by_one.setText(_translate("MainWindow", ">"))
        self.pushButton_ControlMajor_forward_by_one.clicked.connect(lambda: self.button_control_figure(2))

        self.label_oneday.setText(_translate("MainWindow", "Цена Дня"))
        self.label_text_price_OneDay.setText(_translate("MainWindow", "Значение дня"))
        self.label_price_OneDay.setText(_translate("MainWindow", "0 ₽"))
        self.pushButton_priceOneDay.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_priceOneDay.clicked.connect(self.button_PriceOneDay)

    def button_update_figure(self):
        if self.dateEdit_end.date().toPyDate() <= self.dateEdit_start.date().toPyDate():
            return
        self.Table = AI.start_model(self.model, self.dateEdit_start.date().toPyDate(), self.dateEdit_end.date().toPyDate())
        self.label_end_price.setText(f"{self.Table[1][-1]:.2f} ₽")
        self.line.set_data(self.Table[0], self.Table[1])
        self.axes.set_ylim(min(self.Table[1]), max(self.Table[1])+1)
        self.axes.set_xlim(self.Table[0][0], max(self.Table[0]))
        self.figure.canvas.draw()
        self.button_control_figure(event=3)

    def button_control_figure(self, event=False, days=1):
        if event is False:
            return
        elif event == 1 and hasattr(self, 'Table'):
            #Уменьшение диапозона графика
            date_end = self.Table[0][len(self.Table[0])-1]-datetime.timedelta(days=days)
            if date_end.date() > self.dateEdit_start.date().toPyDate():
                self.dateEdit_end.setDateTime(
                    QtCore.QDateTime(QtCore.QDate(date_end.year, date_end.month, date_end.day), QtCore.QTime(0, 0, 0)))
                self.button_update_figure()
            return
        elif event == 2 and hasattr(self, 'Table'):
            #Увеличение диапозона графика
            date_end = self.Table[0][len(self.Table[0]) - 1] + datetime.timedelta(days=days)
            self.dateEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(date_end.year, date_end.month, date_end.day), QtCore.QTime(0, 0, 0)))
            self.button_update_figure()
            return
        elif event == 3:
            if len(self.Table[0]) < 20:
                self.xaxis_locater = 0
            elif len(self.Table[0]) >= 20 and len(self.Table[0]) <= 31*12:
                self.xaxis_locater = 1
            elif len(self.Table[0]) > 31*12:
                self.xaxis_locater = 2
        self.xaxis_locater = self.xaxis_locater%3

        locators = [mdates.DayLocator(), mdates.MonthLocator(), mdates.YearLocator()]
        locators_name = [mdates.DateFormatter("%d"), mdates.DateFormatter("%m"), mdates.DateFormatter("%Y")]

        self.axes.xaxis.set_major_locator(locators[self.xaxis_locater])
        self.axes.xaxis.set_major_formatter(locators_name[self.xaxis_locater])
        self.axes.xaxis.set_minor_locator(locators[:2][(self.xaxis_locater-1)%2])

        self.figure.canvas.draw()

    def button_PriceOneDay(self):
        Table = AI.start_model(self.model, self.dateEdit_priceoneday.date().toPyDate())
        self.label_price_OneDay.setText(f"{Table[1][-1]:.2f} ₽")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi_start(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())