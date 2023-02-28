import numpy as np
import cv2

black= np.zeros([600,600])

black[200:401,200:401] = 255




cv2.imshow("black",black)

cv2.waitKey(0)