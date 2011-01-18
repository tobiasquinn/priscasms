#!/usr/bin/env python3.1

from PyQt4 import QtGui
from PyQt4.QtCore import QVariant, QSettings, SIGNAL
from .PreferencesDialogUI import Ui_PreferencesDialog

class PreferencesDialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)
        # call on accept or reject
        self.connect(self, SIGNAL("finished(int)"), self._result)
        # load preferences
        self._settings = QSettings()
        print(type(self._settings.value("sms/sshmode", False)))
        #self.ui.checkBoxSSH.setChecked(self._settings.value("sms/sshmode", False type=bool)))
        # Note this is a hack for pyqt4 version 4.8.2 which sould be fixed in 4.8.3
        # Is this cross platform???
        self.ui.checkBoxSSH.setChecked(self._settings.value("sms/sshmode", False) == "true")
        self.ui.lineEditSSHAddress.setText(self._settings.value("sms/sshaddress"))

    def _result(self, result):
        if result == self.Accepted:
            # save the selected preferences
            self._settings.setValue("sms/sshmode", self.ui.checkBoxSSH.isChecked())
            self._settings.setValue("sms/sshaddress", self.ui.lineEditSSHAddress.text())
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    prefsd = PreferencesDialog(None)
    prefsd.show()
    app.exec()

