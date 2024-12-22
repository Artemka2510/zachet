import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
import psycopg2


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Список материалов')

        # Основной вертикальный layout
        vbox = QVBoxLayout()

        # Таблица для отображения материалов
        self.table_widget = QTableWidget(self)
        vbox.addWidget(self.table_widget)

        self.setLayout(vbox)

        # Подключаемся к базе данных и загружаем данные
        self.load_data()

    def load_data(self):
        try:
            # Подключение к базе данных PostgreSQL
            connection = psycopg2.connect(
                dbname='zachet123',
                user='postgres',  # замените на ваше имя пользователя
                password='artem',  # замените на ваш пароль
                host='localhost',  # или адрес вашего сервера базы данных
                port='5432'  # стандартный порт PostgreSQL
            )
            cursor = connection.cursor()

            # Получаем данные из таблицы materials
            cursor.execute("SELECT * FROM materials")
            rows = cursor.fetchall()

            # Устанавливаем количество строк и столбцов в таблице
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(3)  # id, title, quantity

            # Устанавливаем заголовки столбцов
            self.table_widget.setHorizontalHeaderLabels(['ID', 'Title', 'Quantity'])

            # Заполняем таблицу данными
            for row_index, row_data in enumerate(rows):
                for column_index, item in enumerate(row_data):
                    self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

        except Exception as e:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных: {str(e)}")

        finally:
            if connection:
                cursor.close()
                connection.close()
