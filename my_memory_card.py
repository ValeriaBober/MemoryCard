from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
class Question():
    def __init__ ( self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Какая страна самая большая?', 'Россия', 'Корея', 'Нигерия', 'Америка'))
question_list.append(Question('Со скольки лет начинается уголовная ответственность?', 'с 14', 'с 12', 'с 18', 'с рождения'))
question_list.append(Question('Сколько на планете материков?', '6', '7', '5', '10'))
question_list.append(Question('Какая страна самая населённая?', 'Китай', 'Россия', 'Япония', 'Корелия'))
question_list.append(Question('Как зовут президента России?', 'Владимир Владимирович Путин', 'Владимир', 'Владимирович', 'Путин'))
question_list.append(Question('Сколько камер в сердце у млекопитающих?', '4', '3', '2', '1'))
question_list.append(Question('Какая валюта используется в Японии?', 'иена', 'доллар', 'евро', 'юань'))
question_list.append(Question('127 градусов какой это угол?', 'тупой', 'прямой', 'острый', 'развёрнутый'))
question_list.append(Question('Сколько углов в квадрате?', '4', '2', '3', '5'))
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
question = QLabel('Какой национальности не существует?')
lineh1 = QHBoxLayout()
lineh1.addWidget(question)
RadioGroupBox=QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
lineh2 = QHBoxLayout()
lineh2.addWidget(RadioGroupBox)
btn = QPushButton('Ответить')
lineh3 = QHBoxLayout()
lineh3.addWidget(btn)
AnsGroupBox = QGroupBox('Результаты теста')
Ib_Result = QLabel('прав ты или нет?')
Ib_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(Ib_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Ib_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
lineh2.addWidget(AnsGroupBox)
line_card = QVBoxLayout()
line_card.addLayout(lineh1)
line_card.addLayout(lineh2)
line_card.addLayout(lineh3)
AnsGroupBox.hide()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if 'Ответить' == btn.text():
        show_result()
    else:
        show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.quest)
    Ib_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    Ib_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        main_win.score = main_win.score + 1
        print('Всего задано вопросов:', main_win.total)
        print('Всего правильных ответов:', main_win.score)
        print('% правильных ответов:', main_win.score/main_win.total*100)
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            print('Всего задано вопросов:', main_win.total)
            print('Всего правильных ответов:', main_win.score)
            print('% правильных ответов:', main_win.score/main_win.total*100, '%')
            show_correct('Неверно, вафла ')
def next_question():
    main_win.cur_question = main_win.cur_question + 1
    main_win.total = main_win.total + 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0 
    q = question_list[main_win.cur_question]
    ask(q)
def Click_OK():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
btn.clicked.connect(Click_OK) 
main_win.cur_question = -1
main_win.total = 0
main_win.score = 0   
main_win.setLayout(line_card)
next_question()
main_win.show()
app.exec_()