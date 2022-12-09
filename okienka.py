from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QMenu, \
    QAction
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja aplikacja')
        # self.button = QPushButton("Wcisnij mnie!")
        self.setFixedSize(QSize(400, 300))
        # self.setCentralWidget(self.button)
        # self.button.clicked.connect(self.button_was_clicked)
        # self.button.clicked.connect(self.button_was_toggled)
        # self.button.setCheckable(True)
        # self.label = QLabel()
        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)
        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)
        # container = QWidget()
        # container.setLayout(layout)
        # self.setCentralWidget(container)

    def contextMenuEvent(self, e):
        context = QMenu()
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())
    #
    # def button_was_clicked(self):
    #     print('Kliknięto!')
    #     self.button.setText('Już mnie kliknąłeś!!!')
    #     self.setWindowTitle('Super apka!')
    #
    # def button_was_toggled(self, checked):
    #     print("Checked?", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
