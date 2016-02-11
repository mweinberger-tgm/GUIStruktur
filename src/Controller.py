from src import View
import sys
from PySide.QtCore import *
from PySide.QtGui import *

__author__ = 'Michael Weinberger'
__date__ = 20151220
__version__ = 1.0


class Controller(QWidget):

    """
        Erstellt das Spiel, verbindet die einzelnen Komponenten miteinander
    """
    def __init__(self, parent=None):

        super().__init__(parent)

        self.Dialog = View.Ui_Dialog()
        self.Dialog.setupUi(self)

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
