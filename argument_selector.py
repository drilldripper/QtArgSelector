#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import fnmatch

from PyQt5.QtWidgets import (QWidget, QPushButton, QGridLayout, QFileDialog,
                             QLabel, QTableWidget, QComboBox, QTableWidgetItem)


class ArgumentSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.file_button = QPushButton("Open Directory")
        self.file_button.clicked.connect(self.enumerate_files)

        self.cell_button = QPushButton("Select Items")
        self.cell_button.clicked.connect(self.select_argument)

        # Select extensions
        self.extention_label = QLabel("Extension")
        self.combo = QComboBox(self)
        self.combo.addItem("*")
        self.combo.addItem("png")
        self.combo.addItem("jpg")
        self.combo.addItem("bmp")
        self.combo.addItem("txt")


        # Set Table
        self.table = QTableWidget()
        self.tableItem = QTableWidgetItem()
        self.table.setRowCount(0)
        self.table.setColumnCount(1)

        # stretch table option
        self.table.horizontalHeader().setStretchLastSection(True)

        # cell name
        self.table.setHorizontalHeaderLabels(["FileList"])

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.file_button, 0, 0)
        grid.addWidget(self.combo, 0, 3)
        grid.addWidget(self.extention_label, 0, 2)
        grid.addWidget(self.table, 1, 0, 1, 4)
        grid.addWidget(self.cell_button, 2, 3)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def enumerate_files(self):
        """Set selected files in the table"""
        directory = QFileDialog.getExistingDirectory(self, 'Open directory', '/home')
        files = os.listdir(directory)

        # filter files with file extension
        files = [f for f in files if fnmatch.fnmatch(f, "*." + self.combo.currentText())]
        self.table.setRowCount(len(files))
        self.table.setColumnCount(1)

        for i, file in enumerate(files):
            self.table.setItem(0, i, QTableWidgetItem(file))

    def select_argument(self):
        """Extract data in the selected cells and add arguments to sys.arg"""
        indexes = self.table.selectionModel().selectedRows()
        for i, index in enumerate(indexes):
            row = index.row()
            rowtext = []
            for column in range(self.table.columnCount()):
                rowtext.append(self.table.item(row, column).text())
                sys.argv.append(rowtext[0])
        self.close()
