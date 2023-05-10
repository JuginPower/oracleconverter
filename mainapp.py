import sys
from PySide6 import QtWidgets
from ui_converter import Ui_ConverterWindow
from constraint import ConstraintTranslator
from services import search_replace
import re


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_ConverterWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonOpen.clicked.connect(self.getFileName)
        self.ui.pushButtonTranslate.clicked.connect(self.openFileData)

    def getFileName(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(parent=self, filter="Text files (*.txt *.sql)")
        self.inputFile = filename[0]
        string_list = filename[0].split(".")
        self.ui.lineEditUpload.setText(string_list[0].split("/")[-1] + "." + string_list[-1])

    def _translateData(self, data):
        """
        Probleme mit Constraint ohne Primary Key aufgetaucht.
        """

        new_lines = []


        with open("testfile.sql", "w", encoding="utf-8") as writer:

            counter = 0

            for line in data:

                if re.search(r"--.+", line) or (counter<3 and re.search("ALTER", line)):
                    continue

                elif re.search(r"NUMBER\((\d+),([1-9]+)\)", line): 
                    matched_string = re.search(r"NUMBER\((\d+),([1-9]+)\)", line)
                    new_part = "DOUBLE(" + matched_string.group(1) + "," + matched_string.group(2) + ")"
                    new_line = re.sub(r"NUMBER\((\d+),([1-9]+)\)", new_part, line)
                    new_line = search_replace(new_line)
                    new_line = new_line.replace('"', '')
                    new_lines.append(new_line)
                
                elif re.search(r'CONSTRAINT', line) and counter > 3:
                    const_trans = ConstraintTranslator(line)
                    new_line = const_trans.from_oracle_to_mysql()
                    new_lines.append(new_line)

                else:
                    line = search_replace(line)
                    line = line.replace('"', '')
                    new_lines.append(line)

                counter += 1
            
            writer.writelines(new_lines)
            print("done!")
                

    def openFileData(self):
        with open(self.inputFile, 'r', encoding='utf-8') as txtFile:
            data = txtFile.readlines()
            translated_data = self._translateData(data)
        


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
