from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QWidget, QVBoxLayout,
                             QPushButton, QHBoxLayout, QLineEdit, QComboBox)
import psycopg2

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Список материалов')

        # Основной вертикальный layout
        vbox = QVBoxLayout()

        # Горизонтальный layout для поиска и фильтрации
        hbox = QHBoxLayout()

        # Поле для ввода поиска
        self.search_edit = QLineEdit(parent=self)
        self.search_edit.setPlaceholderText("Введите для поиска")
        hbox.addWidget(self.search_edit)

        # Комбобокс для сортировки
        self.sort_cbox = QComboBox(parent=self)
        self.sort_cbox.addItems(["Сортировка", "Сортировать по дате", "Сортировать по количеству"])
        hbox.addWidget(self.sort_cbox)

        self.filter_cbox = QComboBox(parent=self)
        self.filter_cbox.addItems(["Фильтрация", "Фильтр 1", "Фильтр 2"])
        hbox.addWidget(self.filter_cbox)

        vbox.addLayout(hbox)




        bbox = QHBoxLayout()



        vbox.addLayout(bbox)

        self.setLayout(vbox)




