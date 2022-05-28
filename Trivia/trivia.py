#GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
widgets = {
    "logo":[],
    "button":[],
    "score":[],
    "question":[],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": []
}
#initiallize GUI application
app=QApplication(sys.argv)

#window and settings
window=QWidget()
window.setWindowTitle("Ready for Quiz?")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")


grid=QGridLayout()

def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()
def show_frame1():
    '''display frame 1'''
    clear_widgets()
    frame_1()


def start_game():
    '''display frame 2'''
    clear_widgets()
    frame_2()

def create_buttons(anwser,l_margin, r_margin):
    button=QPushButton(anwser)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "border: 4px solid '#BC006C';" +
        "margin-left: " + str(l_margin) +"px;"+
        "margin-right: " + str(r_margin) +"px;"+
        "color: white;" +
        "font-family: 'shanti'; " +
        "font-size: 16px;"+
        "border-radius: 25px;" +
        "padding: 15px 0; " +
        "margin-top: 20px}"+
        "*:hover{ background: '#BC006C'}"
    )
    button.clicked.connect(show_frame1)
    return button
def frame_1():
    #logo widget
    image=QPixmap("logo.png")
    logo=QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)
    #button widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 100px 200px;}" +
        "*:hover {background:'#BC006C';}"
        )
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

def frame_2():
    score=QLabel("80")
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        "padding: 15px 10px;" +
        "margin: 80px 200px;" +
        "border: 1px solid '#64A314';"  +
        "border-radius: 45px;"
        "font-size: 35px;" +
        "color: 'white';" +
        "background: '#64A314';"
    )
    widgets["score"].append(score)
    question=QLabel("Placeholder text will go here")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-size: 35px;" +
        "color: 'white';" +
        "padding:75px;" +
        "font-family Shanti;"
    )
    widgets["question"].append(question)

    #answer button widgets
    button1 = create_buttons("answer1",85,5)
    button2 = create_buttons("answer2",5,85)
    button3 = create_buttons("answer3",85,5)
    button4 = create_buttons("answer4",5,85)
    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)
    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)
frame_1()
window.setLayout(grid)

window.show()
#terminate the app
sys.exit(app.exec())
