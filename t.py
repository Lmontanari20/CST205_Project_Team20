import sys
import numpy as np
import cv2
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout,QVBoxLayout, QComboBox)

from PyQt5.QtCore import pyqtSlot


display_image_list = ["None", "image1", "image2", "image3", "image4"]
filter_image_list = ["None", "filter1", "filter2", "filter3", "filter4"]

star = cv2.imread("star.jpg")
star_gray = cv2.imread('star.jpg', cv2.IMREAD_GRAYSCALE)


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

        self.submit_button = QPushButton("Submit", self)


        description_label = QLabel(self)
        description_label.setText("Choose an Image and Filter to display on your Webcam")

        v_layout = QVBoxLayout()
        v_layout.addWidget(description_label)


        h_layout = QHBoxLayout()
        h_layout.addWidget(self.filter_combo_box)
        h_layout.addWidget(self.image_combo_box)
        h_layout.addWidget(self.submit_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(v_layout)
        main_layout.addLayout(h_layout)

        self.setLayout(main_layout)
        self.submit_button.clicked.connect(self.on_click)
        self.setWindowTitle("Webcam Fun")


    @pyqtSlot()
    def on_click(self):
        my_video = cv2.VideoCapture(0)
        while True:
            ret, frame = my_video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Gray_Version", gray)
            cv2.waitKey(1)
            image = self.image_combo_box.currentText()
        #if image == "image1"
            star_gray_new = cv2.applyColorMap(star, cv2.COLORMAP_RAINBOW)
            cv2.imshow("", star_gray_new)

        my_video.release()
        cv2.destroyAllWindows()



app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
