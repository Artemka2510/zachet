from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import (QMainWindow,QTableView, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox)


class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh()
    def refresh(self):
        sql = '''
            SELECT 
                m.id_material, 
                mt.title_mtype, 
                m.title_material, 
                m.min_quantity, 
                m.storage_quantity,
                (
                    SELECT STRING_AGG(s.tittle_supplier, ', ')  -- Используем правильный алиас
                    FROM suppliers s
                    WHERE s.id_supplier IN (
                        SELECT ms.suppolier_id  -- Используем правильный алиас
                        FROM materials_suppliers ms
                        WHERE ms.material_id = m.id_material
                    )
                ) AS suppliers
            FROM 
                materials AS m
            JOIN 
                mtype AS mt ON m.mtype_id = mt.id_mtype;

        '''
        self.setQuery(sql)


class View(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        model = Model(parent=self)
        self.setModel(model)
        model.setHeaderData(1,Qt.Horizontal, 'Тип')
        model.setHeaderData(2, Qt.Horizontal, 'Наименование')
        model.setHeaderData(3, Qt.Horizontal, 'Мин кол-во')
        model.setHeaderData(4, Qt.Horizontal, 'Остаток')
        model.setHeaderData(5, Qt.Horizontal, 'Поставщики')



        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.Singleselection)

        vh = self.verticalHeader()
        vh.setSectionEesizeMode(vh.Fixed)
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeToContents)
        hh.setSectionResizeMode(2, hh.Stretch)