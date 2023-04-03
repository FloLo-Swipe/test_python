import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget

WIN_X = 100
WIN_Y = 100
WIDTH = 280
HEIGHT = 80
LABEL_X = 60
LABEL_Y = 15

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(WIN_X, WIN_Y, WIDTH, HEIGHT)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(LABEL_X, LABEL_Y)

window.show()

sys.exit(app.exec())
