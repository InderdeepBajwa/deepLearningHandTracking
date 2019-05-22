import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

import cv2

from ui_main import *

# Importing required files
from utils import detector_utils as detector_utils
import cv2
import tensorflow as tf
import datetime
import argparse

#audio
from ffpyplayer.player import MediaPlayer

from threading import Timer

detection_graph, sess = detector_utils.load_inference_graph()

parser = argparse.ArgumentParser()
parser.add_argument(
    '-sth',
    '--scorethreshold',
    dest='score_thresh',
    type=float,
    default=0.2,
    help='Score threshold for displaying bounding boxes')
parser.add_argument(
    '-fps',
    '--fps',
    dest='fps',
    type=int,
    default=1,
    help='Show FPS on detection/display visualization')
parser.add_argument(
    '-src',
    '--source',
    dest='video_source',
    default=0,
    help='Device index of the camera.')
parser.add_argument(
    '-wd',
    '--width',
    dest='width',
    type=int,
    default=320,
    help='Width of the frames in the video stream.')
parser.add_argument(
    '-ht',
    '--height',
    dest='height',
    type=int,
    default=180,
    help='Height of the frames in the video stream.')
parser.add_argument(
    '-ds',
    '--display',
    dest='display',
    type=int,
    default=1,
    help='Display the detected images using OpenCV. This reduces FPS')
parser.add_argument(
    '-num-w',
    '--num-workers',
    dest='num_workers',
    type=int,
    default=4,
    help='Number of workers.')
parser.add_argument(
    '-q-size',
    '--queue-size',
    dest='queue_size',
    type=int,
    default=5,
    help='Size of the queue.')
args = parser.parse_args()

class MainWindow(QWidget):
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        #self.ui.control_bt.clicked.connect(self.controlTimer)
        self.controlTimer()
    
    def viewCam(self):
        start_time = datetime.datetime.now()
        num_frames = 0
        im_width, im_height = (self.cap.get(3), self.cap.get(4))
        # max number of hands we want to detect/track
        num_hands_detect = 2

        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        ret, image_np = self.cap.read()
        # image_np = cv2.flip(image_np, 1)
        try:
            image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
        except:
            print("Error converting to RGB")

        # Actual detection. Variable boxes contains the bounding box cordinates for hands detected,
        # while scores contains the confidence for each of these boxes.
        # Hint: If len(boxes) > 1 , you may assume you have found atleast one hand (within your score threshold)

        boxes, scores = detector_utils.detect_objects(image_np,
                                                    detection_graph, sess)

        # draw bounding boxes on frame
        detector_utils.draw_box_on_image(num_hands_detect, args.score_thresh,
                                        scores, boxes, im_width, im_height,
                                        image_np)

        # Calculate Frames per second (FPS)
        num_frames += 1
        elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
        fps = num_frames / elapsed_time

        detector_utils.draw_fps_on_image("FPS : " + str(int(fps)), image_np)

        # cv2.imshow('Single-Threaded Detection',
        #         cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))

        # convert image to RGB format
        image = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image_np.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image_np.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        
        #audio
        #audio_frame, val = self.player.get_frame()
        
        if self.i:
            self.player = MediaPlayer("vid1.MP4")
            self.i = False

        self.player.get_frame()
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture("vid1.MP4")
            #audio
            self.i = True
            # start timer
            self.timer.start(24)
            # update control_bt text
            #self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            #self.ui.control_bt.setText("Start")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

