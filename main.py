from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QFileDialog, QMainWindow
import sys

from PyQt5.uic import loadUi
import Mail
import MessageParser




class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"src\GUI\mainWindow.ui", self)

        self.logText = ""

        # Connections to GUI events
        self.selectContactList.clicked.connect(self.browseExcelFile)
        self.selectMailTemplate.clicked.connect(self.browseTextFile)
        self.Login.clicked.connect(self.loginDialogueBox)
        self.Send.clicked.connect(self.sendMails)


    def browseExcelFile(self):
        self.contactFilePath = QFileDialog.getOpenFileName(self, "Open File", r"D:\Code\Mail", "Microsoft Excel Worksheet (*.xlsx)")
        self.ContactList.setText(self.contactFilePath[0].split('/')[-1])

    def browseTextFile(self):
        self.mailTemplatePath = QFileDialog.getOpenFileName(self, "Open File", r"C:\Code\Mail", "Text Document (*.txt)")
        self.MailTemplate.setText(self.mailTemplatePath[0].split('/')[-1])
    
    def loginDialogueBox(self):
        loginBox = LoginDialog()
        loginBox.show()
        loginBox.exec_()

        try:
            self.mailID = loginBox.MailID
            self.password = loginBox.password
            # print(self.mailID + "\n" + self.password)
        except:
            pass

    def sendMails(self):
        Mailer = Mail.Mail(self.mailID,self.password)
        
        self.logText += "Login Success!\n"
        print(self.contactFilePath)
        excelReader = MessageParser.ExcelReader(self.contactFilePath[0])
        Headers = excelReader.createHeaders()

        textReader = MessageParser.MailTemplate(self.mailTemplatePath[0], Headers)


        # sending mails 

        for number in range(excelReader.rows):
            details = excelReader.retContact(number)
            result = Mailer.sendMail(textReader.createMessage(details),details[0]) + "\n"
            self.logText += result
            print(result)
            self.logScreen.setText(self.logText)

        





class LoginDialog(QDialog):

    def __init__(self):
        super(LoginDialog,self).__init__()
        loadUi(r"src\GUI\Login.ui", self)

        self.Password.setEchoMode(QLineEdit.Password)
        # Connecting push buttons 
        self.LoginButton.clicked.connect(self.validateLoginInfo)
        self.Cancel.clicked.connect(self.cancelOperation)
        

    def validateLoginInfo(self):
        self.MailID = self.Email.text()
        self.password = self.Password.text()
        self.close()

    def cancelOperation(self):
        self.close()




app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
