import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout,QVBoxLayout, QComboBox)

from PyQt5.QtCore import pyqtSlot


display_image_list = ["None", "image1", "image2", "image3", "image4"]
filter_image_list = ["None", "filter1", "filter2", "filter3", "filter4"]


class Window(QWidget):
    def __init__(self):
        rgb_value = ''
        hex_value = ''
        super().__init__()

        self.response_label = QLabel(self)


        self.image_combo_box = QComboBox()
        self.image_combo_box.addItems(display_image_list)

        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItems(filter_image_list)

        submit_button = QPushButton("Submit", self)


        description_label = QLabel(self)
        description_label.setText("Choose an Image and Filter to display on your Webcam")

        v_layout = QVBoxLayout()
        v_layout.addWidget(description_label)


        h_layout = QHBoxLayout()
        h_layout.addWidget(self.filter_combo_box)
        h_layout.addWidget(self.image_combo_box)
        h_layout.addWidget(submit_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(v_layout)
        main_layout.addLayout(h_layout)

        self.setLayout(main_layout)

        self.setWindowTitle("Webcam Fun")



app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
