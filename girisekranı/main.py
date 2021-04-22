from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import Ui_giris_ekranı

class Pencere(QMainWindow, Ui_giris_ekranı.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.labe_kullaniciadi.show()
        #self.label_sifre.show()
        self.button_giris.clicked.connect(self.girisyap)
        

    def girisyap(self):
        kullaniciadi="admin"
        şifre="yarrak"
        if ((self.input_kullaniciadi == "admin") and (self.input_sifre == "yarrak")):
            #ne gelecek ?
        

app=QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())