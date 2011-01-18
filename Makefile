# Makefile to build the user interface
UIDIR=priscasms/ui

all: $(UIDIR)/MainWindowUI.py $(UIDIR)/CMSDialogUI.py $(UIDIR)/PreferencesDialogUI.py

$(UIDIR)/MainWindowUI.py: $(UIDIR)/MainWindowUI.ui
	pyuic4 $(UIDIR)/MainWindowUI.ui -o $(UIDIR)/MainWindowUI.py

$(UIDIR)/CMSDialogUI.py: $(UIDIR)/CMSDialogUI.ui
	pyuic4 $(UIDIR)/CMSDialogUI.ui -o $(UIDIR)/CMSDialogUI.py

$(UIDIR)/PreferencesDialogUI.py: $(UIDIR)/PreferencesDialogUI.ui
	pyuic4 $(UIDIR)/PreferencesDialogUI.ui -o $(UIDIR)/PreferencesDialogUI.py

clean:
	rm $(UIDIR)/MainWindowUI.py
	rm $(UIDIR)/CMSDialogUI.py
	rm $(UIDIR)/PreferencesDialogUI.py
