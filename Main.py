from GUI_Code import Ui_MainWindow                
import XML_to_JSON                                  
import file_formatting                               
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui(Ui_MainWindow):
    XML_contents=""                      
    def __init__(self):
        Ui_MainWindow.setupUi(self,MainWindow)
        Ui_MainWindow.retranslateUi(self, MainWindow)

        self.actionopen.triggered.connect(self.chooseFileClicked)   
        self.convertButton.clicked.connect(self.convert_XML_to_Json)     
        self.formattingButton.clicked.connect(self.formatting_XML_file)   

    def open_XML_file(self,filePath):         
        with open(filePath) as f:
            self.XML_contents=f.read()        

    def chooseFileClicked (self):       
        try :
            filePath=QtWidgets.QFileDialog.getOpenFileName(None,"choose file","","(*.xml)") 
            self.open_XML_file(filePath[0])
            self.inputPlain.setPlainText(self.XML_contents)
        except:
            pass

    def convert_XML_to_Json(self):       
        json_file=XML_to_JSON.convertToJson(self.XML_contents)
        self.outputPlain.setPlainText(json_file)

    def formatting_XML_file(self):         
        formatted=file_formatting.func_formatting(self.XML_contents)
        self.outputPlain.setPlainText(formatted)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    #ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())        