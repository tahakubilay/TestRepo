import sys
from PyQt5.QtWidgets import QApplication
from takeditorWindow import EditorWindow #olmazsa olmaz

app = QApplication(sys.argv)
takeditor =  EditorWindow()          #klasik olaylar
sys.exit(app.exec_())