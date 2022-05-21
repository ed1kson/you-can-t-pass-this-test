from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QButtonGroup
from random import  shuffle
app = QApplication([]) 
window = QWidget() 
window.resize(250, 200)
window.setWindowTitle('Memory Card')
mainline = QVBoxLayout() 
mainline.setSpacing(1)  
line1 = QHBoxLayout() 
line2 = QHBoxLayout() 
line3 = QHBoxLayout()

#коробка для вопроса
box = QGroupBox('Варианты') 
boxline = QHBoxLayout() 
boxline.setSpacing(20)
class Specbutton(QRadioButton):
    def __init__(self):
        super().__init__()
        text = 'text'
a = 2

answerlabel = QLabel('answerLabel')

lineinbox1 = QVBoxLayout() 
lineinbox2 = QVBoxLayout() 
lineinbox1.setSpacing(8)
lineinbox2.setSpacing(8)

button1 = Specbutton()
button2 = Specbutton()
button3 = Specbutton()
button4 = Specbutton()
buttons = [button1, button2, button3, button4]
answerbutton = QPushButton('Ответить') 

#создание класса

class Question():
    def __init__(self, answer, rightanswer, wrong1, wrong2, wrong3):
        self.answer = str(answer)
        self.rightanswer = str(rightanswer)
        self.wrong1 = str(wrong1)
        self.wrong2 = str(wrong2)
        self.wrong3 = str(wrong3)

themes = []
themes.append(Question('Cколько лет мне?', 14, 15, 13, 12))
themes.append(Question('Какой сейчас год?', 2021, 2015, 2018, 2022))
themes.append(Question('Какого цвета дуб?','коричневый', 'синий', 'ультрамариновый', 'зеленый'))
theme = themes[a]
answersnumber = len(themes) - 1
#добавление виджетов в бокс

lineinbox1.addWidget(button1, alignment = Qt.AlignLeft)
lineinbox1.addStretch(1)
lineinbox1.addWidget(button2, alignment = Qt.AlignLeft) 
lineinbox1.addStretch(2)


lineinbox2.addWidget(button3, alignment = Qt.AlignLeft)
lineinbox2.addStretch(1) 
lineinbox2.addWidget(button4, alignment = Qt.AlignLeft)
lineinbox2.addStretch(2)

boxline.addWidget(answerlabel, alignment = Qt.AlignCenter)
boxline.addLayout(lineinbox1) 
boxline.addLayout(lineinbox2) 
box.setLayout(boxline) 

RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)

mainline.addStretch(1)
mainline.addWidget(answerlabel, alignment =( Qt.AlignHCenter | Qt.AlignVCenter)) 

mainline.addWidget(box,stretch = 1) 

#Коробка для проверки ответа/создание виджетов
box2 = QGroupBox('Результат теста')
torf = QLabel('Неправильно')
labelanswer = QLabel('labelanswer')
box2line = QVBoxLayout()
box2line.setSpacing(20)
lineinbox2 = QHBoxLayout()
line2inbox2 = QHBoxLayout()

lineinbox2.addWidget(torf, stretch= 1)
line2inbox2.addWidget(labelanswer, alignment = Qt.AlignCenter)
box2line.addLayout(lineinbox2)
box2line.addLayout(line2inbox2)
box2.setLayout(box2line)
mainline.addStretch(1)
mainline.addWidget(box2)


def next_question():

    
    global theme
    theme = themes[a]
    answers = [theme.rightanswer, theme.wrong1, theme.wrong2, theme.wrong3]
    shuffle(answers)
    answerlabel.setText(theme.answer)
    button1.setText(str(answers[0]))
    button2.setText(str(answers[1]))
    button3.setText(str(answers[2]))
    button4.setText(str(answers[3]))
    answerbutton.setText('Ответить')
    box2.hide()
    answerbutton.hide()
    box.show()
    answerbutton.show()


def checkanswer():
    for i in buttons:
        checked = i.isChecked()
        if checked == True:
            text = i.text()
            RadioGroup.setExclusive(False)
            i.setChecked(False)
            RadioGroup.setExclusive(True)
            if text == theme.rightanswer:
                torf.setText('Правильно')
            else:
                torf.setText('Неправильно')
    labelanswer.setText(theme.rightanswer)
    answerbutton.setText('Следующий вопрос')
    box.hide()
    answerbutton.hide()
    box2.show()
    answerbutton.show()
    

def presscontinue():
    
    text = answerbutton.text()
    if text == 'Ответить':
        global a
        a += 1
        if a > answersnumber:
            a = 0
        checkanswer()
    else:
        next_question()



answerbutton.clicked.connect(presscontinue)

mainline.addStretch(1)
mainline.addWidget(answerbutton,stretch = 2) 
mainline.addStretch(1)
window.setLayout(mainline) 
window.show()
next_question()
app.exec_()
