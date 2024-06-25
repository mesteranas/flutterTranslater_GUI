import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class HandleTranslation(qt.QDialog):
    def __init__(self,p,texts):
        super().__init__(p)
        self.texts=texts
        layout=qt.QVBoxLayout(self)
        self.list=qt.QListWidget()
        self.list.currentTextChanged.connect(self.listChanged)
        self.list.addItems(self.texts.keys())
        layout.addWidget(self.list)
        self.translatedText=qt.QLineEdit()
        self.translatedText.textChanged.connect(self.onTranslatedTextChanged)
        self.list.setCurrentRow(0)
        self.listChanged(self.list.currentItem().text())
        layout.addWidget(self.translatedText)
        self.save=qt.QPushButton(_("save as json file"))
        self.save.clicked.connect(self.onSave)
        layout.addWidget(self.save)
    def listChanged(self,text):
        self.translatedText.setText(self.texts[text])
    def onTranslatedTextChanged(self,text):
        self.texts[self.list.currentItem().text()]=text
    def onSave(self):
        file=qt.QFileDialog(self)
        file.setAcceptMode(file.AcceptMode.AcceptSave)
        file.setDefaultSuffix("json")
        if file.exec()==file.DialogCode.Accepted:
            with open(file.selectedFiles()[0],"w",encoding="utf-8") as file:
                file.write(str(self.texts).replace("'",'"'))
                self.close()