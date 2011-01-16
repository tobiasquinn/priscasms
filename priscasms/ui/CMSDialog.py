#!/usr/bin/env python3.1

from PyQt4 import QtGui, QtCore
from .CMSDialogUI import Ui_CMSDialog

class CMS(QtGui.QDialog):
    def __init__(self, parent, number, message):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_CMSDialog()
        self.ui.setupUi(self)
        self._setNumber(number)
        self._setMessage(message)

    def _setNumber(self, number):
        self.ui.labelNumber.setText(number)

    def _setMessage(self, message):
        self.ui.labelMessage.setText(message)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    cms = CMS(None, "+447789993069", "However, there whom the guide to support, UUCP, MIT Chaosnet, and a software (and redistribute GNU free is more than just Not obstruct most of Unix).  There were")
    cms.show()
    app.exec()

