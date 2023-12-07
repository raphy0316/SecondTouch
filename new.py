# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'onehandkeyboard.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from operator import eq
import keyboard
import time
import sys

stopped = 0
shortShift = 0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("one_key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(240, 190, 80, 80))
        self.startButton.clicked.connect(self.start)

        self.stopButton = QtWidgets.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(360, 190, 80, 80))
        self.stopButton.clicked.connect(self.exit)

        self.resetButton = QtWidgets.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(480, 190, 80, 80))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 10, 450, 16))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 311, 16))
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(240, 50, 341, 16))
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 70, 341, 16))
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 90, 381, 81))

        self.keyboard_img = QtWidgets.QLabel(Dialog)
        self.keyboard_img.setGeometry(QtCore.QRect(20, 290, 761, 291))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Second Hand"))
        self.startButton.setText(_translate("Dialog", "시작"))
        self.stopButton.setText(_translate("Dialog", "종료"))
        self.resetButton.setText(_translate("Dialog", "리셋\n( ctrl + q )"))
        self.label.setText(_translate("Dialog", "c - ctrl + c"))
        self.label_2.setText(_translate("Dialog", "z - ctrl + z"))
        self.label_3.setText(_translate("Dialog", "t - shift 자동누름 활성화/해제"))
        self.label_4.setText(_translate("Dialog", "ㅍ - ctrl 자동누름 활성화/해제"))
        self.label_5.setText(_translate("Dialog", " 사용법 : \n""ㅂ-ㅛ, ㅅ-[, ㅁ-ㅓ, ㅎ-; , ㅋ-ㅡ, ㅍ-/ 이런식으로\n""매핑되어있습니다. 자동으로 자음과 모음이 변환\n""되며, 띄어쓰기하듯이 스페이스바를 누르시면 \n자연스럽게 재조합이 됩니다."))


        self.keyboard_img.setPixmap(QPixmap("./keyboard_800.jpg"))

    def start(self):
        print('press "ctrl + q" to restart. ')
        print('press "c" to ctrl+c. ')
        print('press "z" to ctrl+z. ')
        print('press "g" to change. ')
        print('press "t" to long ctrl. ')
        print('press "v" to long shift. ')
        self.myThread().start()

    def exit(self):
        global stopped
        stopped = 1
        sys.exit()

    class myThread(threading.Thread):  # threading.Thread 상속받음
        shortShift = 0

        def run(self):
            global shortShift
            DELAY_TIME = 0.15
            mode = 0  # 0 = ja // 1 = mo imput
            savedKey = []
            cKey = "g"

            shiftMod = 0
            ctrlMod = 0


            def key_pressed(key):
                global stopped
                global shortShift
                print("ss : "+str(shortShift))
                if eq(key, "space"):
                    asdf = 0
                    for i in savedKey:
                        if not(i is 'shift' or i is "space"):
                            keyboard.press_and_release("backspace")#지움
                            print("del")
                    keyboard.press_and_release("backspace")
                    for i in savedKey:
                        if asdf is 0:
                            if not i is "shift":
                                keyboard.press_and_release(i)
                            else:
                                asdf=1
                        else:
                            asdf = 0
                            keyboard.press_and_release("shift+"+i)

                    for i in range(len(savedKey)):
                        savedKey.pop()
                if eq(key, "backspace"):
                    try:
                        if savedKey[len(savedKey)-2] is "shift":
                            savedKey.pop()
                        savedKey.pop()
                    except:
                        pass
                else:
                    savedKey.append(key)
                    if shortShift is 1:
                        keyboard.press_and_release("backspace")
                        keyboard.press_and_release("shift+"+key)
                        shortShift = 0

                    keyboard.press_and_release("space")
                    keyboard.press_and_release("backspace")
                print(savedKey)
                time.sleep(DELAY_TIME)

            while not stopped:
                try:
                    while not stopped:
                        # try:
                        if keyboard.is_pressed('ctrl+q'):  # reset
                            break

                        if keyboard.is_pressed('j'):
                            if mode is 0:
                                keyboard.press_and_release('backspace+a')
                                mode = 1
                                key_pressed('a')
                            elif mode is 1:
                                mode = 0
                                key_pressed('j')

                        if keyboard.is_pressed('k'):
                            if mode is 0:
                                keyboard.press_and_release('backspace+s')
                                mode = 1
                                key_pressed('s')
                            elif mode is 1:
                                mode = 0
                                key_pressed('k')

                        if keyboard.is_pressed('l'):
                            if mode is 0:
                                keyboard.press_and_release('backspace+d')
                                mode = 1
                                key_pressed('d')
                            elif mode is 1:
                                mode = 0
                                key_pressed('l')

                        if keyboard.is_pressed(';'):
                            keyboard.press_and_release('backspace+f')
                            mode = 1
                            key_pressed('f')

                        if keyboard.is_pressed("'"):
                            if mode is 0:
                                keyboard.press_and_release('backspace+g')
                                mode = 1
                                key_pressed('g')
                            elif mode is 1:
                                mode = 0
                                key_pressed("'")

                        if keyboard.is_pressed("u"):
                            if mode is 0:
                                keyboard.press_and_release('backspace+q')
                                mode = 1
                                key_pressed('q')
                            elif mode is 1:
                                mode = 0
                                key_pressed('u')

                        if keyboard.is_pressed("i"):
                            if mode is 0:
                                keyboard.press_and_release('backspace+w')
                                mode = 1
                                key_pressed('w')
                            elif mode is 1:
                                mode = 0
                                key_pressed('i')

                        if keyboard.is_pressed("o"):
                            if mode is 0:
                                keyboard.press_and_release('backspace+e')
                                mode = 1
                                key_pressed('e')
                            elif mode is 1:
                                mode = 0
                                key_pressed('o')

                        if keyboard.is_pressed("p"):
                            if mode is 0:
                                keyboard.press_and_release('backspace+r')
                                mode = 1
                                key_pressed('r')
                            elif mode is 1:
                                mode = 0
                                key_pressed('p')

                        if keyboard.is_pressed("["):
                            keyboard.press_and_release('backspace+t')
                            mode = 1
                            key_pressed('t')

                        if keyboard.is_pressed("m"):
                            if mode is 0:
                                keyboard.press_and_release('backspace+z')
                                mode = 1
                                key_pressed('z')
                            elif mode is 1:
                                mode = 0
                                key_pressed('m')

                        if keyboard.is_pressed(","):
                            keyboard.press_and_release('backspace+x')
                            mode = 1
                            key_pressed('x')

                        if keyboard.is_pressed("."):
                            keyboard.press_and_release('backspace+c')
                            mode = 1
                            key_pressed('c')

                        if keyboard.is_pressed("/"):
                            keyboard.press_and_release('backspace+v')
                            mode = 1
                            key_pressed('v')

                        if keyboard.is_pressed('y'):
                            mode = 0
                            key_pressed('y')

                        if keyboard.is_pressed('h'):
                            mode = 0
                            key_pressed('h')

                        if keyboard.is_pressed('n'):
                            mode = 0
                            key_pressed('n')

                        if keyboard.is_pressed('b'):
                            mode = 0
                            key_pressed('b')

                        if keyboard.is_pressed(cKey):
                            print("changed")
                            if mode == 0:
                                mode = 1
                            else:
                                mode = 0
                            keyboard.press_and_release("backspace")
                            time.sleep(DELAY_TIME)

                        if keyboard.is_pressed('backspace'):
                            if mode == 0:
                                mode = 1
                            else:
                                mode = 0
                            key_pressed('backspace')
                            time.sleep(DELAY_TIME)

                        if keyboard.is_pressed('space'):
                            mode = 0
                            key_pressed('space')
                            time.sleep(DELAY_TIME)

                        if keyboard.is_pressed("t")and keyboard.is_pressed("T"):
                            if shiftMod == 1:
                                keyboard.press("shift")
                                shiftMod = 0
                            else:
                                keyboard.release("shift")
                                shiftMod = 1
                            time.sleep(DELAY_TIME)

                        if keyboard.is_pressed("right_shift"):
                            savedKey.append("shift")
                            shortShift = 1
                            print("rs")
                            time.sleep(DELAY_TIME)

                        if keyboard.is_pressed("v"):
                            if shiftMod == 1:
                                keyboard.press("ctrl")
                                shiftMod = 0
                            else:
                                keyboard.release("ctrl")
                                shiftMod = 1

                        if keyboard.is_pressed("c"):
                            keyboard.press_and_release("ctrl+c")

                        if keyboard.is_pressed("z"):
                            keyboard.press_and_release("ctrl+z")

                        if keyboard.is_pressed("enter"):
                            pass
                except:
                    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
