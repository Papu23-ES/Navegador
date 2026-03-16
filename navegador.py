
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Barra de navegación
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Atrás', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        home_btn = QAction('Inicio', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

app = QApplication(sys.argv)
QApplication.setApplicationName('Mi Navegador Pro')
window = MainWindow()
app.exec_()
