import sys
from custome_errors import *
sys.excepthook = my_excepthook
import update
import gui
import guiTools
from settings import *
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        self.files=[]
        layout=qt.QVBoxLayout()
        self.path=qt.QListWidget()
        layout.addWidget(self.path)
        self.browse=guiTools.QPushButton(_("Browse"))
        self.browse.clicked.connect(self.on_browse)
        layout.addWidget(self.browse)
        self.funName=qt.QLineEdit()
        layout.addWidget(qt.QLabel(_("define name")))
        layout.addWidget(self.funName)
        self.go=guiTools.QPushButton(_("go"))
        self.go.clicked.connect(self.on_go)
        layout.addWidget(self.go)
        self.setting=guiTools.QPushButton(_("settings"))
        self.setting.clicked.connect(lambda: settings(self).exec())
        layout.addWidget(self.setting)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        helpFile=qt1.QAction(_("help file"),self)
        help.addAction(helpFile)
        helpFile.triggered.connect(lambda:guiTools.HelpFile())
        helpFile.setShortcut("f1")
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/tprogrammers"))
        githup=qt1.QAction(_("Github"),self)
        cus.addAction(githup)
        githup.triggered.connect(lambda: guiTools.OpenLink(self,"https://Github.com/mesteranas"))
        X=qt1.QAction(_("x"),self)
        cus.addAction(X)
        X.triggered.connect(lambda:guiTools.OpenLink(self,"https://x.com/mesteranasm"))
        email=qt1.QAction(_("email"),self)
        cus.addAction(email)
        email.triggered.connect(lambda: guiTools.sendEmail("anasformohammed@gmail.com","project_type=GUI app={} version={}".format(app.name,app.version),""))
        Github_project=qt1.QAction(_("visite project on Github"),self)
        help.addAction(Github_project)
        Github_project.triggered.connect(lambda:guiTools.OpenLink(self,"https://Github.com/mesteranas/{}".format(settings_handler.appName)))
        Checkupdate=qt1.QAction(_("check for update"),self)
        help.addAction(Checkupdate)
        Checkupdate.triggered.connect(lambda:update.check(self))
        licence=qt1.QAction(_("license"),self)
        help.addAction(licence)
        licence.triggered.connect(lambda: Licence(self))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
        if settings_handler.get("update","autoCheck")=="True":
            update.check(self,message=False)
    def closeEvent(self, event):
        if settings_handler.get("g","exitDialog")=="True":
            m=guiTools.ExitApp(self)
            m.exec()
            if m:
                event.ignore()
        else:
            self.close()
    def xFind (self,text, first, last):
        list = {}
        x = 0
        y = 0
        size = text.count (first)
        for i in range(size):
            x = text.find(first ,y)+ len (first)
            y = text.find(last, x)
            list[text[x:y]]=""
        return list

    def on_browse(self):
        file=qt.QFileDialog(self)
        file.setFileMode(file.FileMode.ExistingFiles)
        if file.exec()==file.DialogCode.Accepted:
            self.path.addItems(file.selectedFiles())
            self.files.extend(file.selectedFiles())
    def on_go(self):
        list={}
        for file in self.files:
            with open(file,"r",encoding="utf-8") as file:
                text=file.read()
            for key,value in self.xFind(text,self.funName.text()+'("','")').items():
                list[key]=value
        gui.HandleTranslation(self,list).exec()

App=qt.QApplication([])
w=main()
w.show()
App.setStyle('fusion')
App.exec()