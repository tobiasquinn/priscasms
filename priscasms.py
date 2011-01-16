#!/usr/bin/env python3.1

# PriscaSMS (c) Tobias Quinn, <tobias@tobiasquinn.com>, GPLv3

# This will send an sms using gammu on a remote machine
# The remote machine must be set up to use passwordless ssh login and the remote
# user must be able to send SMS using gammu from the command line
# The phone to be used must be configured before hand to send SMS

import sys, re

from PyQt4 import QtCore, QtGui

from priscasms.ui.MainWindowUI import Ui_MainWindow
from priscasms.ui.CMSDialog import CMS

# out max message length
MML = 160

class ValidatePhoneNumber(QtGui.QValidator):
    def __init__(self):
        QtGui.QValidator.__init__(self)
        self.regexp = re.compile("^[\d+]\d*$")

    def validate(self, qstr, pos):
        # Blank is acceptable
        if qstr == '': return QtGui.QValidator.Acceptable, qstr, pos
        # match on a regexp
        if self.regexp.match(qstr):
            return QtGui.QValidator.Acceptable, qstr, pos
        else:
            return QtGui.QValidator.Invalid, qstr, pos

class Highlight160(QtGui.QSyntaxHighlighter):
    def highlightBlock(self, message):
        self.setFormat(MML, len(message), QtGui.QColor("red"))

class Main(QtGui.QMainWindow):
    def _getNumber(self):
        return self.ui.lineEditPhoneNumber.text()

    def _getMessage(self):
        return self.ui.textEditMessage.toPlainText()

    def _updateSendButton(self, s=None):
        # only allow send when more than 3 chars and a message is present
        if len(self._getNumber()) < 3 or len(self._getMessage()) == 0:
            self.ui.pushButtonSend.setEnabled(False)
        else:
            self.ui.pushButtonSend.setEnabled(True)

    def _updateClearButton(self):
        # update the text clear button and send button status
        self.ui.pushButtonClear.setEnabled(len(self._getMessage()) != 0)
        self._updateSendButton()

    def _messageChanged(self):
        # update the information about the message length and clear button
        self.ui.label_chars_left.setText("%d" % (160 - len(self._getMessage())))
        self._updateClearButton()

    def _sendMessage(self):
        cms = CMS(self, self._getNumber(), self._getMessage()[:MML])
        if cms.exec():
            print("  TO:%s\nMESS:%s" % (self._getNumber(), self._getMessage()[:MML]))

    def __init__(self):
        self.settings = QtCore.QSettings()
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEditPhoneNumber.setValidator(ValidatePhoneNumber())
#        self.setWindowFlags(Qt.Qt.Window | Qt.Qt.WindowMinimizeButtonHint)
        self.connect(self.ui.lineEditPhoneNumber, QtCore.SIGNAL('textChanged(QString)'), self._updateSendButton)
        self.connect(self.ui.textEditMessage, QtCore.SIGNAL('textChanged()'), self._messageChanged)
        self.connect(self.ui.pushButtonSend, QtCore.SIGNAL('clicked()'), self._sendMessage)
        # highlight text over 160 chars
        self.hl = Highlight160(self.ui.textEditMessage.document())
        # read our settings
        self.ui.lineEditPhoneNumber.setText(self.settings.value("gui/number"))

    def __del__(self):
        # write our settings
        self.settings.setValue("gui/number", self._getNumber())

def main():
    app  = QtGui.QApplication(sys.argv)
    app.setOrganizationName("tobiasquinn.com")
    app.setApplicationName("PriscaSMS")
    #ss.setValue("sms/gateway", "tobias-debian32.local")
    window = Main()
    window.show()
    # exit on window close
    app.exec()

if __name__ == "__main__":
    main()

