from PySide6 import QtCore, QtWidgets
from stylesheets import text


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # create label with nothing written
        self.operations = QtWidgets.QLabel('0')
        self.operations.setAlignment(QtCore.Qt.AlignRight)
        self.operations.setStyleSheet(text)

        self.operands = []

        self.setMinimumSize(300, 300)
        self.setWindowTitle("Calculator")

    # create actions for pushed button events:
    # if an integer is pressed, stack from left to right
    # update label as buttons are pushed (follow (pe)mdas).
    @QtCore.Slot()
    def num_or_operator(self, buttonLabel: str):
        self.operands.append(buttonLabel)
        self.operations.setText("".join(self.operands))

    @QtCore.Slot()
    def evaluate(self):
        self.operands = [str(eval("".join(self.operands)))]
        self.operations.setText(self.operands[0])

    @QtCore.Slot()
    def sign_change(self):
        # this is probably unecessary but keeping it for my own clarity
        parsedString = list(self.operands)
        for char in range(len(parsedString)-1, -1, -1):
            # checks list backward until it finds "-" or "+"
            # if negative sign
            if parsedString[char] == "-":
                # if character before negative is "(", then delete negative
                # (assumes negative value)
                if parsedString[char - 1] == "(":
                    del parsedString[char]
                    break
                # if not, then turn subtraction to addition
                # (assumes positive value)
                else:
                    parsedString[char] = "+"
                    break
            elif parsedString[char] == "+":
                # if adding, subtract instead
                parsedString[char] = "-"
                break
            elif char == 0:
                parsedString.insert(char, '-')
        self.operands = parsedString
        self.operations.setText("".join(self.operands))

    @QtCore.Slot()
    def percentage(self):
        self.operands = "".join(self.operands)
        parsedString = list(self.operands)
        catNum = []
        numStart = 0
        for char in range(len(parsedString)-1, -1, -1):
            # if decimal found, first check for integers before it, once no
            # integers are found anymore, concatenate
            if parsedString[char] == ".":
                numStart = char
                continue
            try:  # char-1
                checkInt = int(parsedString[char])
                if char == 0:
                    numStart = 0
                continue
            except:
                numStart = char + 1
                break
        for i in range(numStart, len(parsedString)):
            catNum.append(parsedString[i])
        # divide by 100
        catNum = "".join(str(float("".join(catNum))/100))
        catNum = list(catNum)
        # this is to supress scientiffic notation
        mag = '0'
        for i in range(len(catNum)):
            if catNum[i] == 'e':
                if catNum[i+1] == '-':
                    mag = catNum[i+2: len(catNum)]
                    break
                else:
                    mag = catNum[i+1: len(catNum)]
                    break
        mag = int("".join(mag))
        catNum = float("".join(catNum))
        if mag != 0:
            catNum = f'{catNum:.{mag}f}'
        else:
            pass
        del parsedString[numStart: len(parsedString)]
        parsedString.append(f"{catNum}")
        self.operands = parsedString
        self.operations.setText(str("".join(self.operands)))

    @QtCore.Slot()
    def all_clear(self):
        self.operands = []
        self.operations.setText('0')
