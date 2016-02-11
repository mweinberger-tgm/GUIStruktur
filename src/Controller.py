import sys

from PySide.QtCore import *
from PySide.QtGui import *

from src import View

__author__ = 'Michael Weinberger'
__date__ = 20160211
__version__ = 1.0


class Controller(QWidget):

    """
        Anzeigen der GUI
    """
    def __init__(self, parent=None):

        super().__init__(parent)

        self.Out = View.Ui_MainWindow()
        self.Out.setupUi(self)

    """
        Beendet das Programm sauber
    """
    def kill(self):
        QCoreApplication.instance().quit()

"""
    Starten des Programms
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()
    sys.exit(app.exec_())
