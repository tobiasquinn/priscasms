#!/usr/bin/env python3.1

from PyQt4 import QtGui, QtCore
from .PreferencesDialogUI import Ui_PreferencesDialog

class PreferencesDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    prefsd = PreferencesDialog(None)
    prefsd.show()
    app.exec()

