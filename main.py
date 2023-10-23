import json
import os
import sys
import csv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog, QMenu
from table import Ui_TableEditor


class MyTableEditor(QMainWindow, Ui_TableEditor):
    def __init__(self, num_rows, num_columns):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_columns)

        self.row_separator = ""
        self.column_separator = ""

        self.razdel_line1.textChanged.connect(self.updateRowSeparator)
        self.razdel_line2.textChanged.connect(self.updateColumnSeparator)

        self.auto_save_enabled = False
        self.settings_file = 'settings.json'
        self.load_settings()

        # Включите сортировку для таблицы
        self.tableWidget.setSortingEnabled(True)

        # Установите обработчик события для сортировки по заголовку столбца
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortTable)

        # Установка текста на кнопке "Авто" при запуске
        if self.auto_save_enabled:
            self.pushButton.setText("Авто Вкл")
        else:
            self.pushButton.setText("Авто Выкл")

        self.pushButton.clicked.connect(self.toggle_auto_save)

        for col in range(num_columns):
            column_label = ""
            quotient = col
            while quotient >= 0:
                remainder = quotient % 26
                column_label = chr(ord('A') + remainder) + column_label
                quotient = (quotient // 26) - 1
            self.tableWidget.setHorizontalHeaderItem(col, QTableWidgetItem(column_label))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        self.tableWidget.cellChanged.connect(self.updateCellValue)
        self.save_button.clicked.connect(self.saveToCSV)

        self.path_button.clicked.connect(self.loadTableFromFile)

    def sortTable(self, logicalIndex):
        def get_first_column(self):
            column_data_numbers = []
            column_data_strings = []
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, logicalIndex)
                if item is not None:
                    value = item.text()
                    if self.sort_check.isChecked():
                        try:
                            value = float(value)
                            if value.is_integer():
                                value = int(value)
                            column_data_numbers.append(value)
                        except ValueError:
                            column_data_strings.append(value)
                    else:
                        column_data_strings.append(value)
            return column_data_numbers, column_data_strings

        def get_rows(self, reverses):
            rows = []
            for row in range(self.tableWidget.rowCount()):
                row_data = []
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    if item is not None:
                        value = item.text()
                        if self.sort_check.isChecked():
                            try:
                                value = float(value)
                                if value.is_integer():
                                    value = int(value)
                                row_data.append(value)
                            except ValueError:
                                row_data.append(value)
                        else:
                            row_data.append(value)
                if len(row_data) > logicalIndex:  # Добавьте эту строку
                    if reverses == False:
                        rows.append(row_data)
                        rows.sort(key=lambda x: x[logicalIndex])
                    elif reverses == True:
                        rows.append(row_data)
                        rows.sort(key=lambda x: x[logicalIndex], reverse=True)
            return rows

        if self.string_all.isChecked():
            if self.tableWidget.horizontalHeader().sortIndicatorOrder() == Qt.AscendingOrder:
                rows = get_rows(self, reverses = False)
            else:
                rows = get_rows(self, reverses = True)
            self.tableWidget.setSortingEnabled(False)
            for row, row_data in enumerate(rows):
                for col, value in enumerate(row_data):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))
        else:
            column_data_numbers, column_data_strings = get_first_column(self)
            if self.tableWidget.horizontalHeader().sortIndicatorOrder() == Qt.AscendingOrder:
                column_data_numbers.sort()
                column_data_strings.sort()
                column_data = column_data_numbers + column_data_strings
            else:
                column_data_numbers.sort(reverse=True)
                column_data_strings.sort(reverse=True)
                column_data = column_data_strings + column_data_numbers
            self.tableWidget.setSortingEnabled(False)
            for row, value in enumerate(column_data):
                self.tableWidget.setItem(row, logicalIndex, QTableWidgetItem(str(value)))

    def load_settings(self):
        try:
            with open(self.settings_file, 'r') as settings_file:
                settings = json.load(settings_file)
                self.auto_save_enabled = settings.get('auto_save_enabled', False)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save_settings(self):
        settings = {
            'auto_save_enabled': self.auto_save_enabled,
            'last_saved_path': self.lineEdit_path.text()
        }
        with open(self.settings_file, 'w') as settings_file:
            json.dump(settings, settings_file)

    def toggle_auto_save(self):
        self.auto_save_enabled = not self.auto_save_enabled
        self.pushButton.setText("Авто Вкл" if self.auto_save_enabled else "Авто Выкл")

    def updateRowSeparator(self):
        self.row_separator = fr"{self.razdel_line1.text()}"

    def updateColumnSeparator(self):
        self.column_separator = fr"{self.razdel_line2.text()}"

    def updateCellValue(self, row, col):
        item = self.tableWidget.item(row, col)
        if item is not None:
            cell_text = item.text()
        if self.auto_save_enabled == True:
            if self.lineEdit_path.text():
                self.saveToCSV()
        self.tableWidget.cellChanged.disconnect(self.updateCellValue)
        cell_text = self.tableWidget.item(row, col).text()
        if self.column_separator:  # Проверяем, что разделитель столбцов не пустой
            cell_values = cell_text.split(self.column_separator)
            for i, value in enumerate(cell_values):
                if col + i < self.tableWidget.columnCount():
                    if not self.tableWidget.item(row, col + i):
                        self.tableWidget.setItem(row, col + i, QTableWidgetItem(value))
                    else:
                        self.tableWidget.item(row, col + i).setText(value)
        if self.row_separator:  # Проверяем, что разделитель строк не пустой
            cell_values = cell_text.split(self.row_separator)
            for i, value in enumerate(cell_values):
                if row + i < self.tableWidget.rowCount():
                    if not self.tableWidget.item(row + i, col):
                        self.tableWidget.setItem(row + i, col, QTableWidgetItem(value))
                    else:
                        self.tableWidget.item(row + i, col).setText(value)
        self.tableWidget.cellChanged.connect(self.updateCellValue)
        # Проверяем, если первая клетка в последней строке заполнена, добавляем 100 строк
        if row == self.tableWidget.rowCount() - 1 and col == 0 and self.tableWidget.item(row, col):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 100)

        # Проверяем, если последняя ячейка в строке заполнена, добавляем 100 столбцов
        if col == self.tableWidget.columnCount() - 1 and self.tableWidget.item(row, col):
            num_columns = self.tableWidget.columnCount()
            self.tableWidget.setColumnCount(num_columns + 100)
            for new_col in range(num_columns, self.tableWidget.columnCount()):
                column_label = ""
                quotient = new_col
                while quotient >= 0:
                    remainder = quotient % 26
                    column_label = chr(ord('A') + remainder) + column_label
                    quotient = (quotient // 26) - 1
                self.tableWidget.setHorizontalHeaderItem(new_col, QTableWidgetItem(column_label))

    def saveToCSV(self):
        if not self.lineEdit_path.text():
            # Если lineEdit_path пустой, открываем диалог выбора файла
            options = QFileDialog.Options()
            filePath, _ = QFileDialog.getSaveFileName(self, "Сохранить в CSV файл", "",
                                                      "CSV Files (*.csv);;All Files (*)", options=options)
        else:
            # В противном случае используем значение lineEdit_path в качестве пути
            filePath = self.lineEdit_path.text()

        if filePath:
            try:
                with open(filePath, 'w', newline='', encoding='utf-8') as csv_file:
                    writer = csv.writer(csv_file)
                    for row in range(self.tableWidget.rowCount()):
                        row_data = [self.tableWidget.item(row, col).text() if self.tableWidget.item(row, col) else ''
                                    for col in range(self.tableWidget.columnCount())]
                        while row_data and not row_data[-1]:  # Удалить пустые значения справа в строке
                            row_data.pop()
                        writer.writerow(row_data)

                # Обновляем значение lineEdit_path
                self.lineEdit_path.setText(filePath)
            except Exception as e:
                print(f"Ошибка при сохранении файла: {str(e)}")

    def loadTableFromFile(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "CSV Files (*.csv);;All Files (*)",
                                                  options=options)

        if filePath:
            try:
                with open(filePath, 'r', newline='', encoding='utf-8') as csv_file:
                    reader = csv.reader(csv_file)
                    data = [row for row in reader]
                    num_rows = len(data)
                    # Убедимся, что число столбцов соответствует изначальному значению
                    if num_rows > self.tableWidget.rowCount():
                        self.tableWidget.setRowCount(num_rows)
                    if num_rows > 0:
                        num_columns = max(len(row) for row in data)
                        if num_columns > self.tableWidget.columnCount():
                            self.tableWidget.setColumnCount(num_columns)
                    for row, rowData in enumerate(data):
                        for col, cellData in enumerate(rowData):
                            self.tableWidget.setItem(row, col, QTableWidgetItem(cellData))

                    # Обновляем значение lineEdit_path после загрузки файла
                    self.lineEdit_path.setText(filePath)
            except Exception as e:
                print(f"Ошибка при загрузке файла: {str(e)}")

    def closeEvent(self, event):
        self.save_settings()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    TableEditor = MyTableEditor(100, 100)

    TableEditor.show()
    sys.exit(app.exec_())
