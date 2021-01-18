import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QApplication
from PyQt5.QtCore import QSize

QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

working = "working"
not_working = f"not {working}"
working_color = "#FF1744"
not_working_color = "#1DE9B6"


class WorkingWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(500, 300))
        self.setMaximumSize(QSize(500, 300))
        self.setWindowTitle(not_working)
        self.setStyleSheet(f"background-color: {not_working_color}")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QGridLayout(self)
        central_widget.setLayout(layout)

        self.indicator_text = QLabel(not_working, self)
        self.indicator_text.setFont(QFont("sans-serif", 50))
        self.indicator_text.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.indicator_text, 0, 0)

        self.working_checkbox = QCheckBox(working)
        self.working_checkbox.stateChanged.connect(
            lambda: self.on_checkbox_update(self.working_checkbox)
        )
        layout.addWidget(self.working_checkbox)

    def on_checkbox_update(self, checkbox):
        is_checked = checkbox.isChecked()
        self.indicator_text.setText(working if is_checked else not_working)
        self.setStyleSheet(
            f"background-color: {working_color if is_checked else not_working_color}"
        )
        self.setWindowTitle(working if is_checked else not_working)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = WorkingWindow()
    mainWin.show()
    sys.exit(app.exec_())
