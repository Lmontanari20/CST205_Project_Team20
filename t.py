import sys
import numpy as np
import cv2
#from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout,QVBoxLayout, QComboBox)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PIL import Image

display_image_list = ["Choose An Image", "Star", "Ice", "Cup", "Rock"]
filter_image_list = ["Choose A Color Filter", "B&W", "RAINBOW", "AUTUMN", "HOT"]

star = cv2.imread("star.jpg")
star_gray = cv2.imread('star.jpg', cv2.IMREAD_GRAYSCALE)

ice = cv2.imread("ice.png")
ice_gray = cv2.imread('ice.png', cv2.IMREAD_GRAYSCALE)

cup = cv2.imread("cup.png")
cup_gray = cv2.imread('cup.png', cv2.IMREAD_GRAYSCALE)

rock = cv2.imread("rock.png")
rock_gray = cv2.imread('rock.png', cv2.IMREAD_GRAYSCALE)

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
        description_label.setText("Choose an Image and Filter to display on your Webcam\n To save Webcam Image:Press 's'\n To Quit Webcam: Press 'q'")

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

        # casc_class = "haarcascade_frontalface_default.xml"
        # face_cascade = cv2.CascadeClassifier(casc_class)


        while True:
            ret, frame = my_video.read()
            if fil == 'B&W':
                if image == "Star":
                    image_ = cv2.applyColorMap(star, cv2.COLORMAP_BONE)
                elif image == "Ice":
                    image_ = cv2.applyColorMap(ice, cv2.COLORMAP_BONE)
                elif image == "Cup":
                    image_ = cv2.applyColorMap(cup, cv2.COLORMAP_BONE)
                elif image == "Rock":
                    image_ = cv2.applyColorMap(rock, cv2.COLORMAP_BONE)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_BONE)
            elif fil == 'RAINBOW':
                if image == "Star":
                    image_ = cv2.applyColorMap(star, cv2.COLORMAP_RAINBOW)
                elif image == "Ice":
                    image_ = cv2.applyColorMap(ice, cv2.COLORMAP_RAINBOW)
                elif image == "Cup":
                    image_ = cv2.applyColorMap(cup, cv2.COLORMAP_RAINBOW)
                elif image == "Rock":
                    image_ = cv2.applyColorMap(rock, cv2.COLORMAP_RAINBOW)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_RAINBOW)
            elif fil == 'AUTUMN':
                if image == "Star":
                    image_ = cv2.applyColorMap(star, cv2.COLORMAP_AUTUMN)
                elif image == "Ice":
                    image_ = cv2.applyColorMap(ice, cv2.COLORMAP_AUTUMN)
                elif image == "Cup":
                    image_ = cv2.applyColorMap(cup, cv2.COLORMAP_AUTUMN)
                elif image == "Rock":
                    image_ = cv2.applyColorMap(rock, cv2.COLORMAP_AUTUMN)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_AUTUMN)
            elif fil == 'HOT':
                if image == "Star":
                    image_ = cv2.applyColorMap(star, cv2.COLORMAP_HOT)
                elif image == "Ice":
                    image_ = cv2.applyColorMap(ice, cv2.COLORMAP_HOT)
                elif image == "Cup":
                    image_ = cv2.applyColorMap(cup, cv2.COLORMAP_HOT)
                elif image == "Rock":
                    image_ = cv2.applyColorMap(rock, cv2.COLORMAP_HOT)
                gray = cv2.applyColorMap(frame, cv2.COLORMAP_HOT)

            rows, cols, channels = image_.shape
            roi = gray[0:rows, 0:cols]
            image_gray = cv2.cvtColor(image_, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(image_gray, 10,255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)

            gray_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
            image_fg = cv2.bitwise_and(image_, image_, mask = mask)

            dst = cv2.add(gray_bg, image_fg)
            gray[0:rows, 0:cols] = dst
            cv2.imshow('', gray)

            #cv2.imshow("Gray_Version", gray)
            #result = cv2.addWeighted(image, 0.5, gray, 0.5,0)
            # cv2.imshow("", result)
            # video.write(image)
            #added this line to see if it will open in 1 Window
            if cv2.waitKey(1) == ord('s'):
                cv2.imwrite('Webcam_image.jpg', gray)
            if cv2.waitKey(1) == ord('q'):
                break

                #cv2.imwrite('Webcam_image.jpg', gray)

            #star_gray_new = cv2.applyColorMap(star, cv2.COLORMAP_RAINBOW)
            #cv2.imshow(my_video.selectedimage)
            #cv2.imshow("", gray)
            #cv2.imshow("", image)


        my_video.release()
        cv2.destroyAllWindows()



app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
