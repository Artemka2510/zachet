import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QLineEdit, QPushButton, QHBoxLayout

import psycopg2

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Список материалов')
        
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        # Поле для ввода поиска
        self.search_edit = QLineEdit(self)
        self.search_edit.setPlaceholderText("Поиск по материалам...")
        hbox.addWidget(self.search_edit)

        # Кнопка сортировки
        sort_button = QPushButton("Сортировка", self)
        hbox.addWidget(sort_button)

        # Кнопка фильтрации
        filter_button = QPushButton("Фильтрация", self)
        hbox.addWidget(filter_button)

        # Добавляем горизонтальный layout в основной вертикальный layout
        vbox.addLayout(hbox)

 
        self.table_widget = QTableWidget(self)
        vbox.addWidget(self.table_widget)

        self.setLayout(vbox)

 
        self.load_data()

    def load_data(self):
        try:
            
            connection = psycopg2.connect(
                dbname='zachet123',
                user='postgres',  
                password='artem', 
                host='localhost',  
                port='5432'  
            )
            cursor = connection.cursor()


            cursor.execute("SELECT * FROM materials")
            rows = cursor.fetchall()


            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(3)  # id, title, quantity

            self.table_widget.setHorizontalHeaderLabels(['ID', 'Title', 'Quantity'])

            for row_index, row_data in enumerate(rows):
                for column_index, item in enumerate(row_data):
                    self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

        except Exception as e:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных: {str(e)}")

        finally:
            if connection:
                cursor.close()
                connection.close()
