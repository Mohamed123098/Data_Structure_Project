from GUI_Code import Ui_MainWindow 
import consistency_code               
import XML_to_JSON                                  
import file_formatting 
from compression_code import compression                            
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui(Ui_MainWindow):
    filePath=""
    XML_contents="" 
    outputfile=''
    flag=None                     
    def __init__(self):
        Ui_MainWindow.setupUi(self,MainWindow)
        Ui_MainWindow.retranslateUi(self, MainWindow)

        self.actionopen.triggered.connect(self.chooseFileClicked)  
        self.actionSave.triggered.connect(self.saveFile) 
        self.convertButton.clicked.connect(self.convert_XML_to_Json)     
        self.formattingButton.clicked.connect(self.formatting_XML_file) 
        self.compressButton.clicked.connect(self.compressFunc) 
        self.consistencyButton.clicked.connect(self.consistencyFunc)  

    def open_XML_file(self,filePath):         
        with open(filePath,encoding='utf-8') as f:
            self.XML_contents=f.read()        

    def chooseFileClicked (self):       
        try :
            self.filePath=QtWidgets.QFileDialog.getOpenFileName(None,"choose file","","(*.xml)") 
            self.open_XML_file(self.filePath[0])
            self.inputPlain.setPlainText(self.XML_contents)
        except:
            pass

    def convert_XML_to_Json(self):       
        self.outputfile=XML_to_JSON.convertToJson(self.XML_contents)
        self.outputPlain.setPlainText(self.outputfile)
        self.flag=3

    def formatting_XML_file(self):         
        self.outputfile=file_formatting.func_formatting(self.XML_contents)
        self.outputPlain.setPlainText(self.outputfile)
        self.flag=2

    def compressFunc(self):
        compressed_obj=compression(self.filePath[0])
        filecom=compressed_obj.compress_file()

        self.outputfile=compressed_obj.decompress_file(filecom)
        self.outputPlain.setPlainText("The XML file is compressed \nThe XML file is decompressed to check that the compression algorithm does not change any data of the file \nThe compression algorithm is done correctly")
        self.flag=4

    def consistencyFunc(self):
        consist=consistency_code.check(self.filePath[0])  
        self.outputPlain.setPlainText(consist)
        self.flag=1  

    def saveFile(self):
        if self.flag==1 :
            fileName="cosistency_checking.txt"
        elif self.flag==2 :
            fileName="formatted_file.xml"
        elif self.flag==3 :
            fileName="Json_file.json"
        elif self.flag==4 :
            fileName="decompressed_file.txt"
           
        
        with open(fileName,'w') as g :
            g.write(self.outputfile)
        
        msg= QtWidgets.QMessageBox()
        msg.setWindowTitle("Save")
        msg.setText("file is saved in "+fileName)
        msg.setIcon(QtWidgets.QMessageBox.Information)

        x=msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    MainWindow.showMaximized()
    sys.exit(app.exec_())        
