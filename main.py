from PySide6 import QtWidgets
from calculator import Calculator
import sys
import stylesheets


def set_button(label: str, style: str):
    button = QtWidgets.QPushButton(label)
    button.setStyleSheet(style)
    return button


def button_action(button: QtWidgets.QPushButton, action: Calculator,
                  label=False):
    if label:
        button.clicked.connect(lambda: action(button.text()))
    else:
        button.clicked.connect(lambda: action())


app = QtWidgets.QApplication(sys.argv)  # starts the app

# created instance of calculator window
calc = Calculator()
calc.setStyleSheet(stylesheets.window)

# set buttons and its actions
clear = set_button("AC", stylesheets.misc)
button_action(clear, calc.all_clear)

equals = set_button("=", stylesheets.mathButtons)
button_action(equals, calc.evaluate)

posNeg = set_button("+/-", stylesheets.misc)
button_action(posNeg, calc.sign_change)

percent = set_button("%", stylesheets.misc)
button_action(percent, calc.percentage)

divide = set_button("/", stylesheets.mathButtons)
button_action(divide, calc.num_or_operator, True)

decimal = set_button(".", stylesheets.mainKey)
button_action(decimal, calc.num_or_operator, True)

add = set_button("+", stylesheets.mathButtons)
button_action(add, calc.num_or_operator, True)

subtract = set_button("-", stylesheets.mathButtons)
button_action(subtract, calc.num_or_operator, True)

multiply = set_button("*", stylesheets.mathButtons)
button_action(multiply, calc.num_or_operator, True)

# create number buttons
integers = []
for iter in range(10):
    integers.append(set_button(f"{iter}", stylesheets.mainKey))

integersClicked = []
for integer in integers:
    integersClicked.append(button_action(integer, calc.num_or_operator,
                                         True))

# create layout
layout = QtWidgets.QGridLayout(calc)

layout.addWidget(calc.operations, 0, 0, 1, 4)
layout.addWidget(clear, 1, 0)
layout.addWidget(posNeg, 1, 1)
layout.addWidget(percent, 1, 2)
layout.addWidget(divide, 1, 3)
layout.addWidget(integers[7], 2, 0)
layout.addWidget(integers[8], 2, 1)
layout.addWidget(integers[9], 2, 2)
layout.addWidget(multiply, 2, 3)
layout.addWidget(integers[4], 3, 0)
layout.addWidget(integers[5], 3, 1)
layout.addWidget(integers[6], 3, 2)
layout.addWidget(subtract, 3, 3)
layout.addWidget(integers[1], 4, 0)
layout.addWidget(integers[2], 4, 1)
layout.addWidget(integers[3], 4, 2)
layout.addWidget(add, 4, 3)
layout.addWidget(integers[0], 5, 0, 1, 2)
layout.addWidget(decimal, 5, 2)
layout.addWidget(equals, 5, 3)
calc.show()

app.exec()  # runs the app
