from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja aplikacja')
        self.button = QPushButton("Wcisnij mnie!")
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.button_was_clicked)
        self.button.clicked.connect(self.button_was_toggled)
        self.button.setCheckable(True)

    def button_was_clicked(self):
        print('Kliknięto!')
        self.button.setText('Już mnie kliknąłeś!!!')
        self.setWindowTitle('Super apka!')

    def button_was_toggled(self, checked):
        print("Checked?", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
