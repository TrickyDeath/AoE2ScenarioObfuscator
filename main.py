import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import UIMainWindow

VERSION = "0.0.3"
UPDATE_TIME = "2024-11-06"

if __name__ == "__main__":
    # UI测试用
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = UIMainWindow()
    ui.setupUi(main_window)
    ui.setStatement(version=VERSION, update_time=UPDATE_TIME)
    main_window.show()
    app.exec_()
