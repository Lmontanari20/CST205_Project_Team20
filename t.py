import sys
import numpy as np
import cv2
#from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout,QVBoxLayout, QComboBox)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot


display_image_list = ["Choose An Image", "Star", "Image2", "Image3", "Image4"]
filter_image_list = ["Choose A Color Filter", "B&W", "RAINBOW", "AUTUMN", "HOT"]

star = cv2.imread("star.jpg")
star_gray = cv2.imread('star.jpg', cv2.IMREAD_GRAYSCALE)


class Window(QWidget):
    def __init__(self):
        rgb_value = ''
        hex_value = ''
        super().__init__()

        self.response_label = QLabel(self)

        self.my_image = QPixmap("star.jpg")
        self.response_label.setPixmap(self.my_image)
        #imageResized = my_image.scaled(100,100)


        self.image_combo_box = QComboBox()
        self.image_combo_box.addItems(display_image_list)

        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItems(filter_image_list)

        self.submit_button = QPushButton("Submit", self)
        self.resize(self.my_image.width(), self.my_image.height())

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
        self.setGeometry(200, 200, 200, 200)


    @pyqtSlot()
    def on_click(self):
        fil = self.filter_combo_box.currentText()
        image = self.image_combo_box.currentText()
        my_video = cv2.VideoCapture(0)

        while True:
            ret, frame = my_video.read()
            if fil == 'B&W':
                if image == "Star":
                    image = cv2.applyColorMap(star, cv2.COLORMAP_BONE)
                elif image == "Ice":
                  image = cv2.applyColorMap(ice, cv2.COLORMAP_BONE)
                elif image == "Cup":
                  image = cv2.applyColorMap(cup, cv2.COLORMAP_BONE)
                elif image == "Rock":
                  image = cv2.applyColorMap(rock, cv2.COLORMAP_BONE)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_BONE)
            elif fil == 'RAINBOW':
                if image == "Star":
                    image = cv2.applyColorMap(star, cv2.COLORMAP_RAINBOW)
                elif image == "Ice":
                  image = cv2.applyColorMap(ice, cv2.COLORMAP_RAINBOW)
                elif image == "Cup":
                  image = cv2.applyColorMap(cup, cv2.COLORMAP_RAINBOW)
                elif image == "Rock":
                  image = cv2.applyColorMap(rock, cv2.COLORMAP_RAINBOW)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_RAINBOW)
            elif fil == 'AUTUMN':
                if image == "Star":
                    image = cv2.applyColorMap(star, cv2.COLORMAP_AUTUMN)
                elif image == "Ice":
                  image = cv2.applyColorMap(ice, cv2.COLORMAP_AUTUMN)
                elif image == "Cup":
                  image = cv2.applyColorMap(cup, cv2.COLORMAP_AUTUMN)
                elif image == "Rock":
                  image = cv2.applyColorMap(rock, cv2.COLORMAP_AUTUMN)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_AUTUMN)
            elif fil == 'HOT':
                if image == "Star":
                    image = cv2.applyColorMap(star, cv2.COLORMAP_HOT)
                elif image == "Ice":
                  image = cv2.applyColorMap(ice, cv2.COLORMAP_HOT)
                elif image == "Cup":
                  image = cv2.applyColorMap(cup, cv2.COLORMAP_HOT)
                elif image == "Rock":
                  image = cv2.applyColorMap(rock, cv2.COLORMAP_HOT)
                gray = cv2.cvtColor(frame, cv2.COLOR_HOT)

            cv2.imshow("Gray_Version", gray)
            if cv2.waitKey(1) == ord('q'):
                break

            #star_gray_new = cv2.applyColorMap(star, cv2.COLORMAP_RAINBOW)
            #cv2.imshow(my_video.selectedimage)
            #cv2.imshow("", gray)
            cv2.imshow("", image)

        my_video.release()
        cv2.destroyAllWindows()



app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
