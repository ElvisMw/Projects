#!/usr/bin/python

import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QStyleFactory, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal
import shutil
import qdarkstyle  # Import QDarkStyle

class FileCopyThread(QThread):
    progress_signal = pyqtSignal(int)
    result_signal = pyqtSignal(bool)

    def __init__(self, from_file, to_file):
        super().__init__()
        self.from_file = from_file
        self.to_file = to_file

    def run(self):
        try:
            total_size = os.path.getsize(self.from_file)
            copied_size = 0
            with open(self.from_file, 'rb') as src, open(self.to_file, 'wb') as dest:
                chunk_size = 4096
                while chunk := src.read(chunk_size):
                    dest.write(chunk)
                    copied_size += len(chunk)
                    progress_percentage = int((copied_size / total_size) * 100)
                    self.progress_signal.emit(progress_percentage)

            self.result_signal.emit(True)
        except Exception as e:
            print(f"An error occurred: {e}")
            self.result_signal.emit(False)

class FileCopyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create GUI components
        self.label_from = QLabel("From File:")
        self.entry_from = QLineEdit(self)

        self.label_to = QLabel("To File:")
        self.entry_to = QLineEdit(self)

        browse_from_button = QPushButton("Browse", self)
        browse_from_button.clicked.connect(self.browse_from_file)

        browse_to_button = QPushButton("Browse", self)
        browse_to_button.clicked.connect(self.browse_to_file)

        self.copy_button = QPushButton("Copy", self)
        self.copy_button.clicked.connect(self.copy_files)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setTextVisible(True)

        self.result_label = QLabel(self)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_from)
        layout.addWidget(self.entry_from)
        layout.addWidget(browse_from_button)
        layout.addWidget(self.label_to)
        layout.addWidget(self.entry_to)
        layout.addWidget(browse_to_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Set window properties
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('File Copy Tool')

        # Initialize theme
        self.current_theme = "default"  # default theme
        self.apply_theme()

        self.show()

    def browse_from_file(self):
        """
        Opens a file dialog to browse and select a file.

        This function uses the `QFileDialog` class to open a file dialog window and allows the user to select a file. The selected file path is then set as the text of the `entry_from` widget.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        file_dialog = QFileDialog()
        filename = file_dialog.getOpenFileName()[0]
        if filename:
            self.entry_from.setText(filename)

    def browse_to_file(self):
        """
        A method to browse to a file using a file dialog, set the selected file's name to an entry widget.
        """
        file_dialog = QFileDialog()
        filename = file_dialog.getSaveFileName()[0]
        if filename:
            self.entry_to.setText(filename)

    def copy_files(self):
        from_file = self.entry_from.text()
        to_file = self.entry_to.text()

        if not from_file or not to_file:
            return

        self.copy_button.setEnabled(False)

        # Create a thread for file copying
        self.copy_thread = FileCopyThread(from_file, to_file)
        self.copy_thread.progress_signal.connect(self.update_progress)
        self.copy_thread.result_signal.connect(self.show_result)
        self.copy_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def show_result(self, success):
        self.copy_button.setEnabled(True)

        if success:
            self.result_label.setText("File copy completed successfully.")
        else:
            self.result_label.setText("File copy failed.")

    def toggle_theme(self):
        if self.current_theme == "default":
            self.current_theme = "dark"
        elif self.current_theme == "dark":
            self.current_theme = "white"
        else:
            self.current_theme = "default"
        self.apply_theme()

    def apply_theme(self):
        if self.current_theme == "dark":
            QApplication.instance().setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        else:
            QApplication.instance().setStyle(QStyleFactory.create(self.current_theme))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileCopyApp()
    sys.exit(app.exec_())
