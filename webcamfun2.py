# CST-205 Multimedia Design & Progming
# Final Project: "Webcam Fun"
# Authors: Reimer Koopal, Lucas Montanari, Hiren Patel
# December 11, 2017
# GitHub link: https://github.com/Lmontanari20/CST205_Project_Team20/tree/master
# Lucas worked on applying the color filter on webcam
# Hiren worked on image filter in the on_click
# Reimer worked on the on_click function

import sys
import numpy as np
import cv2
#from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout,QVBoxLayout, QComboBox)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PIL import Image

#2 lists to display in the 2 combo boxes
display_image_list = ["Choose An Image", "Christmas", "Happy Birthday", "Dragon", "Thundercat"]
filter_image_list = ["Choose A Color Filter", "B&W", "RAINBOW", "AUTUMN", "HOT"]
size_image_list = ["Choose a size", "small", "medium", "large"]

#reading the four image files

christmas = cv2.imread("christmas.jpg")
christmas_gray = cv2.imread('christmas.jpg', cv2.IMREAD_GRAYSCALE)

birthday = cv2.imread("birthday.jpg")
birthday_gray = cv2.imread('birthday.jpg', cv2.IMREAD_GRAYSCALE)

dragon = cv2.imread("dragon.jpg")
dragon_gray = cv2.imread('dragon.jpg', cv2.IMREAD_GRAYSCALE)

thundercat = cv2.imread("thundercat.jpg")
thundercat_gray = cv2.imread('thundercat.jpg', cv2.IMREAD_GRAYSCALE)





class Window(QWidget):
    def __init__(self):
        rgb_value = ''
        hex_value = ''
        super().__init__()

        self.response_label = QLabel(self)

        self.my_image = QPixmap("star.jpg")
        self.response_label.setPixmap(self.my_image)

        self.image_combo_box = QComboBox()
        self.image_combo_box.addItems(display_image_list)

        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItems(filter_image_list)

        self.size_combo_box = QComboBox()
        self.size_combo_box.addItems(size_image_list)

        self.submit_button = QPushButton("Submit", self)
        self.resize(self.my_image.width(), self.my_image.height())

        description_label = QLabel(self)
        description_label.setText("Choose an Image and Filter to display on your Webcam\n Choose a size for your image\n To save Webcam Image:Press 's'\n To Quit Webcam: Press 'q'")

        v_layout = QVBoxLayout()
        v_layout.addWidget(description_label)


        h_layout = QHBoxLayout()
        h_layout.addWidget(self.filter_combo_box)
        h_layout.addWidget(self.image_combo_box)
        h_layout.addWidget(self.size_combo_box)
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
        size_fil = self.size_combo_box.currentText()
        my_video = cv2.VideoCapture(0)

        # While statement goes through the selected filter option by the user
        # Then depending on which filter the user selects applies the same filter to the image selected by the user
        while True:
            ret, frame = my_video.read()
            if fil == 'B&W':
                if image == "Christmas":
                    image_ = cv2.applyColorMap(christmas, cv2.COLORMAP_BONE)
                elif image == "Happy Birthday":
                    image_ = cv2.applyColorMap(birthday, cv2.COLORMAP_BONE)
                elif image == "Dragon":
                    image_ = cv2.applyColorMap(dragon, cv2.COLORMAP_BONE)
                elif image == "Thundercat":
                    image_ = cv2.applyColorMap(thundercat, cv2.COLORMAP_BONE)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_BONE)
            elif fil == 'RAINBOW':
                if image == "Christmas":
                    image_ = cv2.applyColorMap(christmas, cv2.COLORMAP_RAINBOW)
                elif image == "Happy Birthday":
                    image_ = cv2.applyColorMap(birthday, cv2.COLORMAP_RAINBOW)
                elif image == "Dragon":
                    image_ = cv2.applyColorMap(dragon, cv2.COLORMAP_RAINBOW)
                elif image == "Thundercat":
                    image_ = cv2.applyColorMap(thundercat, cv2.COLORMAP_RAINBOW)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_RAINBOW)
            elif fil == 'AUTUMN':
                if image == "Christmas":
                    image_ = cv2.applyColorMap(christmas, cv2.COLORMAP_AUTUMN)
                elif image == "Happy Birthday":
                    image_ = cv2.applyColorMap(birthday, cv2.COLORMAP_AUTUMN)
                elif image == "Dragon":
                    image_ = cv2.applyColorMap(dragon, cv2.COLORMAP_AUTUMN)
                elif image == "Thundercat":
                    image_ = cv2.applyColorMap(thundercat, cv2.COLORMAP_AUTUMN)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_AUTUMN)
            elif fil == 'HOT':
                if image == "Christmas":
                    image_ = cv2.applyColorMap(christmas, cv2.COLORMAP_HOT)
                elif image == "Happy Birthday":
                    image_ = cv2.applyColorMap(birthday, cv2.COLORMAP_HOT)
                elif image == "Dragon":
                    image_ = cv2.applyColorMap(dragon, cv2.COLORMAP_HOT)
                elif image == "Thundercat":
                    image_ = cv2.applyColorMap(thundercat, cv2.COLORMAP_HOT)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_HOT)

            if size_fil == 'small':
                height, width = image_.shape[:2]
                image1_ = cv2.resize(image_,(100, 100))

            elif size_fil == 'medium':
                height, width = image_.shape[:2]
                image1_ = cv2.resize(image_,(300, 300))

            elif size_fil == 'large':
                height, width = image_.shape[:2]
                image1_ = cv2.resize(image_,(600, 600))

            rows, cols, channels = image1_.shape
            roi = gray[0:rows, 0:cols]
            image_gray = cv2.cvtColor(image1_, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(image_gray, 10,255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)

            gray_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
            image_fg = cv2.bitwise_and(image1_, image1_, mask = mask)

            dst = cv2.add(gray_bg, image_fg)
            gray[0:rows, 0:cols] = dst
            cv2.imshow('', gray)


            if cv2.waitKey(1) == ord('s'):
                cv2.imwrite('Webcam_image.jpg', gray)
            if cv2.waitKey(1) == ord('q'):
                break


        my_video.release()
        cv2.destroyAllWindows()



app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
