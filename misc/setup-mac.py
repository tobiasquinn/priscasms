from setuptools import setup

setup(
  app=["priscasms.py"],
  options={"py2app":
    {"argv_emulation": True, "includes": ["sip", "PyQt4._qt"]}
  },
  setup_requires=["py2app"]) 
