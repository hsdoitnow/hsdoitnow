import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout

import pyautogui
from threading import Thread
from pynput import keyboard

class MacroApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.running = False
        self.buy_location = None
        self.inventory_location = None
        self.money_location = None
        self.drop_money_location = None

        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.keyboard_listener.start()

    def initUI(self):
        self.setWindowTitle('매크로 프로그램')
        self.setGeometry(100, 100, 400, 250)

        self.buy_label = QLineEdit(self)
        self.buy_label.setPlaceholderText('구매창 좌표 입력 (F1)')
        self.inventory_label = QLineEdit(self)
        self.inventory_label.setPlaceholderText('인벤창 좌표 입력 (F2)')
        self.money_label = QLineEdit(self)
        self.money_label.setPlaceholderText('인벤돈 좌표 입력 (F3)')
        self.drop_money_label = QLineEdit(self)
        self.drop_money_label.setPlaceholderText('돈버리기 좌표 입력 (F4)')

        self.start_button = QPushButton('실행', self)
        self.stop_button = QPushButton('정지', self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buy_label)
        self.layout.addWidget(self.inventory_label)
        self.layout.addWidget(self.money_label)
        self.layout.addWidget(self.drop_money_label)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.setLayout(self.layout)

        self.start_button.clicked.connect(self.start_macro)
        self.stop_button.clicked.connect(self.stop_macro)

    def on_key_press(self, key):
        try:
            if key == keyboard.Key.f1:
                self.buy_label.setText(f"{pyautogui.position().x}, {pyautogui.position().y}")
            elif key == keyboard.Key.f2:
                self.inventory_label.setText(f"{pyautogui.position().x}, {pyautogui.position().y}")
            elif key == keyboard.Key.f3:
                self.money_label.setText(f"{pyautogui.position().x}, {pyautogui.position().y}")
            elif key == keyboard.Key.f4:
                self.drop_money_label.setText(f"{pyautogui.position().x}, {pyautogui.position().y}")
            elif key == keyboard.Key.f5:
                self.start_macro()
        except AttributeError:
            pass

    def start_macro(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self.run_macro)
            self.thread.start()

    def stop_macro(self):
        self.running = False

    def run_macro(self):
        buy_location = self.buy_label.text().strip()
        inventory_location = self.inventory_label.text().strip()
        money_location = self.money_label.text().strip()
        drop_money_location = self.drop_money_label.text().strip()

        buy_x, buy_y = map(int, buy_location.split(','))
        inventory_x, inventory_y = map(int, inventory_location.split(','))
        money_x, money_y = map(int, money_location.split(','))
        drop_money_x, drop_money_y = map(int, drop_money_location.split(','))

        counter = 0

        while self.running:
            try:
                # 구매창에서 마우스 오른쪽 버튼 누르기
                pyautogui.click(x=buy_x, y=buy_y, button='right')
                time.sleep(0.5)

                # 인벤창에서 컨트롤키 누르기
                pyautogui.keyDown('ctrl')
                # 인벤창에서 마우스 왼쪽 버튼 누르기
                pyautogui.click(x=inventory_x, y=inventory_y, button='left')
                time.sleep(0.5)
                # 인벤창에서 컨트롤키 해제
                pyautogui.keyUp('ctrl')

                counter += 1

                # 41번째마다 인벤돈, 돈버리기 동작 추가
                if counter == 41:
                    # ESC 키 누르기
                    pyautogui.press('esc')
                    time.sleep(0.2)

                    # 'i' 키 누르기
                    pyautogui.press('i')
                    time.sleep(0.2)

                    # 인벤돈에 "9999999" 입력 후 마우스 왼쪽 버튼 누르기
                    pyautogui.click(x=money_x, y=money_y, button='left')
                    pyautogui.typewrite("9999999", interval=0.1)
                    time.sleep(0.5)

                    # 돈버리기에서 마우스 왼쪽 버튼 누르기
                    pyautogui.click(x=drop_money_x, y=drop_money_y, button='left')
                    time.sleep(0.5)

                    counter = 0

            except ValueError:
                pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MacroApp()
    window.show()
    sys.exit(app.exec_())
