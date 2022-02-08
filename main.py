from user_info import get_user_name, get_user_item
from get_computer_item import get_computer_item
from battle_result import battle_result

import sys
from PyQt5 import QtWidgets
import Rock_paper_and_scissors


class ExampleApp(QtWidgets.QMainWindow, Rock_paper_and_scissors.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Rock_paper_and_scissors.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

user_name = get_user_name()
user_item = get_user_item()

while user_item != '0':
    computer_item = get_computer_item()
    battle_result(user_item, computer_item, user_name)
    user_item = get_user_item()
