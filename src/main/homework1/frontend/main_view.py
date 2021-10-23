from fnmatch import fnmatch
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QVBoxLayout, QFileDialog
from src.main.homework1.frontend.filters_view import FiltersView
from src.main.homework1.frontend.one_picture_view import OnePictureView
from os import listdir
from os.path import isfile, join

from src.main.homework1.frontend.utils import center


class MainView(QMainWindow):
    def __init__(self):
        def configure_main_widget():
            def configure_main_layout():
                def picture_button_click():
                    picture = \
                        QFileDialog.getOpenFileName(caption="Choose a file", filter="Images (*.png *.jpg *.jpeg)")[0]
                    if picture != "":
                        OnePictureView(self, picture).show()
                        self.hide()

                def directory_button_click():
                    directory = QFileDialog.getExistingDirectory(caption="Choose a directory")
                    if directory != "":
                        pictures = []

                        for f in listdir(directory):
                            path = join(directory, f)

                            if isfile(path) and (fnmatch(f, "*.png") or fnmatch(f, "*.jpg") or fnmatch(f, "*.jpeg")):
                                pictures.append(QtGui.QPixmap(path))

                        FiltersView(self, pictures, False).show()
                        self.hide()

                picture_button = QPushButton("Work with one picture")
                picture_button.clicked.connect(picture_button_click)

                directory_button = QPushButton("Work with directory")
                directory_button.clicked.connect(directory_button_click)

                main_layout = QVBoxLayout()
                main_layout.addWidget(picture_button)
                main_layout.addWidget(directory_button)

                return main_layout

            main_widget = QWidget()
            main_widget.setLayout(configure_main_layout())

            return main_widget

        super().__init__()
        self.setWindowTitle("Filters")
        center(self)
        self.setCentralWidget(configure_main_widget())
