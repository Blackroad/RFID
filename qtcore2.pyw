from PyQt5 import QtCore, QtWidgets
import qtcore

class MyDialog(QtWidgets.QDialog):
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.myWiget = qtcore.MyWindow()
        self.myWiget.vbox.setContentsMargins(0,0,0,0)
        self.button = QtWidgets.QPushButton("Change label")
        mainbox = QtWidgets.QVBoxLayout()
        mainbox.addWidget(self.myWiget)
        mainbox.addWidget(self.button)
        self.setLayout(mainbox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
     if self.myWiget.label.text() == 'Hello World':
        self.myWiget.label.setText("New LAbel")
     elif self.myWiget.label.text() == 'New LAbel':
         self.myWiget.label.setText("Hello World!")
     self.button.setDisabled(False)

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle("Advantages of OOP stile")
    window.resize(300,100)
    window.show()
    sys.exit(app.exec_())