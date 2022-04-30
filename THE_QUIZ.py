from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)

class question():
        def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3


q1= question('when was the great fire of london?','1666','1999', '1062','666')
q2= question('when is chrismas?','25','24','20','31')
q3= question('what is always infront of you but can never be seen?','the future','air','a ghost?','glitter')
q4= question('what comes up but never comes down?','age','a ballon','the moon','intellegence')
q5= question('what has 4 legs, 2 then 3?','a human', 'a alien','a ghost','spiders?')

q_list = [q1,q2,q3,q4,q5]

def show_ans():
        gbox1.hide()
        gbox2.show()
        ab.setText('Next question')
        if answers[0].isChecked():
                lb2.setText('correct! :D')
                main_win.count_lb4 +=1
                lb4.setText('correct answers:'+ str(main_win.count_lb4))
        else:
                lb2.setText('wrong answer sorry. :(')

def show_qst():
        gbox1.show()
        gbox2.hide()
        ab.setText('Answer')
        RadioGroup.setExclusive(False)
        b1.setChecked(False)
        b2.setChecked(False)
        b3.setChecked(False)
        b4.setChecked(False)
        RadioGroup.setExclusive(True)

def test():
        if ab.text() == "Answer":
                show_ans()
        else:
                next_qst()

def ask(q:question):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        lb1.setText(q.question)
        lb3.setText(q.right_answer)
        show_qst()

def next_qst():
        shuffle(q_list)
        main_win.current_qst = main_win.current_qst + 1
        if main_win.current_qst >= len(q_list):
                main_win.current_qst = 0
        q = q_list[main_win.current_qst]
        ask(q)

app=QApplication([])
main_win = QWidget()
main_win.setWindowTitle("memory Card App")
main_win.move(400,300)
main_win.resize(400,300)
main_win.current_qst = -1
main_win.count_lb4= 0
lb1 = QLabel("a very intressting question.")
gbox1 = QGroupBox("answer options")
gbox2 = QGroupBox("test Result:")
lb2 =QLabel("correct/incorrect")
lb3 =QLabel("correct answer")
lb4= QLabel('correct answers:0')
lb5= QLabel('%:')
v4 = QVBoxLayout()
v4.addWidget(lb2, alignment=Qt.AlignLeft)
v4.addWidget(lb3, alignment = Qt.AlignCenter)
gbox2.setLayout(v4)

ab = QPushButton("answer")
RadioGroup = QButtonGroup()
b1=QRadioButton("option 1")
b2=QRadioButton("option 2")
b3=QRadioButton("option 3")
b4=QRadioButton("option 4")
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)
answers= [b1, b2, b3, b4]

v1=QVBoxLayout()
v2=QVBoxLayout()
v3=QVBoxLayout()
h1=QHBoxLayout()
h2=QHBoxLayout()

v1.addWidget(lb1)
v1.addWidget(gbox1)
v1.addWidget(gbox2)
v1.addWidget(ab, stretch=3)
v1.addLayout(h2)
v1.addWidget(lb4, alignment=Qt.AlignLeft)
h2.addWidget(lb5, alignment=Qt.AlignRight)
v2.addWidget(b1)
v2.addWidget(b2)
v3.addWidget(b3)
v3.addWidget(b4)
h1.addLayout(v2)
h1.addLayout(v3)
gbox1.setLayout(h1)

ab.clicked.connect(test)
next_qst()
main_win.setLayout(v1)
gbox2.hide()
main_win.show()
app.exec()