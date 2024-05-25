import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon


def set_image_on_button():
    app = QApplication(sys.argv)

    button = QPushButton()

    # Создание объекта QIcon с изображением
    icon = QIcon("mts_logo_cmyk.png")

    # Установка иконки на кнопку
    button.setIcon(icon)

    button.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    set_image_on_button()
