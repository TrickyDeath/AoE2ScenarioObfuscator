from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

import sys

if __name__ == "__main__":
    # UI测试用
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    app.exec_()
    