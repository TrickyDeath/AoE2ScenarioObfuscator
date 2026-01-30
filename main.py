import sys
from importlib.metadata import version

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import UIMainWindow

VERSION = "0.0.3"
ASP_VERSION = version("AoE2ScenarioParser")

if __name__ == "__main__":
    # UI测试用
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = UIMainWindow()
    ui.setupUi(main_window)
    ui.setStatement(version=VERSION, asp_version=ASP_VERSION)
    main_window.show()
    app.exec_()
