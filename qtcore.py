from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('First QT programm')
window.resize(300,70)
label = QtWidgets.QLabel("<center> Hello guys</center>")
btnQuit = QtWidgets.QPushButton("close")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
btnQuit.clicked.connect(app.quit)
window.setLayout(vbox)

window.show()
sys.exit(app.exec_())
