##Taha Kubilay##

from Ui_takeditor import Ui_takeditor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QFontDialog, QColorDialog
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo, Qt, QTime, QDate
from PyQt5.QtGui import QFont


class EditorWindow(QtWidgets.QMainWindow, Ui_takeditor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionPrint.triggered.connect(self.filePrint)
        self.actionPrint_PDF.triggered.connect(self.filePreview)
        self.actionPrint_Export.triggered.connect(self.fileExportPDF)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionCopy.triggered.connect(self.editCopy)
        self.actionPaste.triggered.connect(self.editPaste)
        self.actionCut.triggered.connect(self.editCut)
        self.actionUndo.triggered.connect(self.textBrowser.undo)
        self.actionRedo.triggered.connect(self.textBrowser.redo)
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionColor.triggered.connect(self.colorDialog)
        self.actionBold.triggered.connect(self.textBold)
        self.actionItalic.triggered.connect(self.textItalic)
        self.actionUnderline.triggered.connect(self.textUnderline)
        self.actionLeft_Align.triggered.connect(self.alignLeft)
        self.actionCenter_Align.triggered.connect(self.alignCenter)
        self.actionRight_Align.triggered.connect(self.alignRight)
        self.actionJustify.triggered.connect(self.alignJustify)
        self.actionTime.triggered.connect(self.ShowTime)
        self.actionDate.triggered.connect(self.ShowDate)

        self.show()

    
    def fileNew(self):                              #yeni dosya fonksiyonu 
        self.textBrowser.clear()                    # kullanılan widget textbroser olduğu için bu

    def fileOpen(self): 
        filename = QFileDialog.getOpenFileName(self, "Open File", "/home")
        
        if filename[0]:
            f = open(filename[0], "r")              #okuma modunda açıp f değişkenine atadım

            with f:
                data = f.read()                     #f değişkenin içindeki veriyi okuttum
                self.textBrowser.setText(data)      #widget textbrowser olduğu için setText ayarlayarak datayı boş alana yazdırdım
        
    def  fileSave(self):
        filename = QFileDialog.getSaveFileName(self, "Save File")  #farklı kaydet gibi çalışıyor !!
        if filename[0]:
            f = open(filename[0], "w")

            with f:
                text=self.textBrowser.toPlainText()
                f.write(text)
                QMessageBox.about(self, "Save File", "File Saved Succesfully") 

    def filePrint(self):                                #print fonksiyonu
        printer = QPrinter(QPrinter.HighResolution)     #yüksek kalite print
        dialog = QPrintDialog(printer,self)             #diyalog penceresi

        if dialog.exec_() == QPrintDialog.Accepted: # yazdırma işlemini onaylayınca eğer hata gelmediyse printer 
            self.textBrowser.print_(printer)        #kullanılabildiyse pencereyi kapatacak 

    def filePreview(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.filePreview)          #print önizleme için gerekli 
        previewDialog.exec_()

    def printPreview(self,printer):
        self.textBrowser.print_(printer)                                #bu da print önizlemenin bir parçası
    
    def fileExportPDF(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf) ;; All Files")
        
        if fn != "":
            if QFileInfo(fn).suffix()  == "":fn += ".pdf"
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textBrowser.document().print_(printer)
    
    def exitApp(self):
        self.close()

    def editCopy(self):
        cursor = self.textBrowser.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected

    def editPaste(self):
        self.textBrowser.append(self.copiedText)

    def editCut(self):
        cursor = self.textBrowser.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
        self.textBrowser.cut()

    def fontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textBrowser.setFont(font)

    def colorDialog(self):
        color =QColorDialog.getColor()
        self.textBrowser.setTextColor(color)

    def textBold(self):
        font = QFont()
        font.setBold(True)
        self.textBrowser.setFont(font)

    def textItalic(self):
        font = QFont()
        font.setItalic(True)
        self.textBrowser.setFont(font)
    
    def textUnderline(self):
        font = QFont()
        font.setUnderline(True)
        self.textBrowser.setFont(font)

    def alignLeft(self):
        self.textBrowser.setAlignment(Qt.AlignLeft)

    def alignCenter(self):
        self.textBrowser.setAlignment(Qt.AlignCenter)

    def alignRight(self):
        self.textBrowser.setAlignment(Qt.AlignRight)

    def alignJustify(self):
        self.textBrowser.setAlignment(Qt.AlignJustify)

    def ShowTime(self):
        time = QTime.currentTime()
        self.textBrowser.setText(time.toString(Qt.DefaultLocaleLongDate))

    def ShowDate(self):
        date = QDate.currentDate()
        self.textBrowser.setText(date.toString(Qt.DefaultLocaleLongDate))