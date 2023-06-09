from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("contacts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "Name", "Job", "Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addContact(self, data):
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)
        self.model.submitAll()
        self.model.select()
