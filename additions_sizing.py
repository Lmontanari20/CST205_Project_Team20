size_image_list = ["Choose a size", "small", "medium", "large"]

self.size_combo_box = QComboBox()
self.size_combo_box.addItems(size_image_list)

description_label.setText("Choose an Image and Filter to display on your Webcam\n Choose a size for your image\n To save Webcam Image:Press 's'\n To Quit Webcam: Press 'q'")

h_layout.addWidget(self.size_combo_box)

size_fil = self.size_combo_box.currentText()

if size_fil == 'small':
          height, width = image_.shape[:2]
          image1_ = cv2.resize(image_,(100, 100))

      elif size_fil == 'medium':
          height, width = image_.shape[:2]
          image1_ = cv2.resize(image_,(300, 300))

      elif size_fil == 'large':
          height, width = image_.shape[:2]
          image1_ = cv2.resize(image_,(600, 600))

#substituted image_ with image1_
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
