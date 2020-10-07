from PySide2.QtWidgets import QPushButton, QApplication
import sys


app = QApplication()

button = QPushButton('Prueba')

button.show()

sys.exit(app.exec_())